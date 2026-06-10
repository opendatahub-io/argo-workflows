#syntax=docker/dockerfile:1.2
ARG GIT_COMMIT=unknown
ARG GIT_TAG=unknown
ARG GIT_TREE_STATE=unknown

FROM registry.access.redhat.com/ubi9/go-toolset:1.26.3@sha256:d36470d5258da00f618b7aca9bdaab8e05134aa938bd6c42d9bd17d50ed45e76 as builder

USER root

RUN dnf install -y \
    git \
    make \
    ca-certificates \
    wget \
    gcc \
    bash \
    mailcap \
    && dnf clean all

WORKDIR /go/src/github.com/argoproj/argo-workflows
COPY go.mod .
COPY go.sum .
RUN --mount=type=cache,target=/go/pkg/mod go mod download

COPY . .

####################################################################################################

FROM node:20-alpine as argo-ui

RUN apk update && apk add --no-cache git

COPY ui/package.json ui/yarn.lock ui/

RUN --mount=type=cache,target=/root/.yarn \
  YARN_CACHE_FOLDER=/root/.yarn JOBS=max \
  yarn --cwd ui install --network-timeout 1000000

COPY ui ui
COPY api api

RUN --mount=type=cache,target=/root/.yarn \
  YARN_CACHE_FOLDER=/root/.yarn JOBS=max \
  NODE_OPTIONS="--max-old-space-size=2048" JOBS=max yarn --cwd ui build

####################################################################################################

FROM builder as argoexec-build

ARG GIT_COMMIT
ARG GIT_TAG
ARG GIT_TREE_STATE

RUN --mount=type=cache,target=/go/pkg/mod --mount=type=cache,target=/root/.cache/go-build GOFIPS140=v1.0.0 GOFLAGS="-tags=no_openssl" make dist/argoexec GIT_COMMIT=${GIT_COMMIT} GIT_TAG=${GIT_TAG} GIT_TREE_STATE=${GIT_TREE_STATE}

####################################################################################################

FROM builder as workflow-controller-build

ARG GIT_COMMIT
ARG GIT_TAG
ARG GIT_TREE_STATE

RUN --mount=type=cache,target=/go/pkg/mod --mount=type=cache,target=/root/.cache/go-build GOFIPS140=v1.0.0 GOFLAGS="-tags=no_openssl" make dist/workflow-controller GIT_COMMIT=${GIT_COMMIT} GIT_TAG=${GIT_TAG} GIT_TREE_STATE=${GIT_TREE_STATE}

####################################################################################################

FROM builder as argocli-build

ARG GIT_COMMIT
ARG GIT_TAG
ARG GIT_TREE_STATE

RUN mkdir -p ui/dist
COPY --from=argo-ui ui/dist/app ui/dist/app
# update timestamp so that `make` doesn't try to rebuild this -- it was already built in the previous stage
RUN touch ui/dist/app/index.html

RUN --mount=type=cache,target=/go/pkg/mod --mount=type=cache,target=/root/.cache/go-build GOFIPS140=v1.0.0 GOFLAGS="-tags=no_openssl" STATIC_FILES=true make dist/argo GIT_COMMIT=${GIT_COMMIT} GIT_TAG=${GIT_TAG} GIT_TREE_STATE=${GIT_TREE_STATE}

####################################################################################################

FROM gcr.io/distroless/static as argoexec-base

COPY --from=argoexec-build /etc/mime.types /etc/mime.types
COPY hack/ssh_known_hosts /etc/ssh/
COPY hack/nsswitch.conf /etc/

####################################################################################################

FROM argoexec-base as argoexec-nonroot

USER 8737

COPY --chown=8737 --from=argoexec-build /go/src/github.com/argoproj/argo-workflows/dist/argoexec /bin/

ENTRYPOINT [ "argoexec" ]

####################################################################################################
FROM argoexec-base as argoexec

COPY --from=argoexec-build /go/src/github.com/argoproj/argo-workflows/dist/argoexec /bin/

ENTRYPOINT [ "argoexec" ]

####################################################################################################

FROM gcr.io/distroless/static as workflow-controller

USER 8737

COPY hack/ssh_known_hosts /etc/ssh/
COPY hack/nsswitch.conf /etc/
COPY --chown=8737 --from=workflow-controller-build /go/src/github.com/argoproj/argo-workflows/dist/workflow-controller /bin/

ENTRYPOINT [ "workflow-controller" ]

####################################################################################################

FROM gcr.io/distroless/static as argocli

USER 8737

WORKDIR /home/argo

COPY hack/ssh_known_hosts /etc/ssh/
COPY hack/nsswitch.conf /etc/
COPY --from=argocli-build /go/src/github.com/argoproj/argo-workflows/dist/argo /bin/

ENTRYPOINT [ "argo" ]
