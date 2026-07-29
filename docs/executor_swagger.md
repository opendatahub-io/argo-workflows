


# The API for an executor plugin.
  

## Informations

### Version

0.0.1

## Content negotiation

### URI Schemes
  * http

### Consumes
  * application/json

### Produces
  * application/json

## All endpoints

###  operations

| Method  | URI     | Name   | Summary |
|---------|---------|--------|---------|
| POST | /api/v1/template.execute | [execute template](#execute-template) |  |
  


## Paths

### <span id="execute-template"></span> execute template (*executeTemplate*)

```
POST /api/v1/template.execute
```

#### Parameters

| Name | Source | Type | Go type | Separator | Required | Default | Description |
|------|--------|------|---------|-----------| :------: |---------|-------------|
| Body | `body` | [ExecuteTemplateArgs](#execute-template-args) | `models.ExecuteTemplateArgs` | | ✓ | |  |

#### All responses
| Code | Status | Description | Has headers | Schema |
|------|--------|-------------|:-----------:|--------|
| [200](#execute-template-200) | OK |  |  | [schema](#execute-template-200-schema) |

#### Responses


##### <span id="execute-template-200"></span> 200
Status: OK

###### <span id="execute-template-200-schema"></span> Schema
   
  

[ExecuteTemplateReply](#execute-template-reply)

## Models

### <span id="a-w-s-elastic-block-store-volume-source"></span> AWSElasticBlockStoreVolumeSource


> An AWS EBS disk must exist before mounting to a container. The disk
must also be in the same AWS zone as the kubelet. An AWS EBS disk
can only be mounted as read/write once. AWS EBS volumes support
ownership management and SELinux relabeling.
  





**Properties**

| Name | Type | Go type | Required | Default | Description | Example |
|------|------|---------|:--------:| ------- |-------------|---------|
| fsType | string| `string` |  | | fsType is the filesystem type of the volume that you want to mount.</br>Tip: Ensure that the filesystem type is supported by the host operating system.</br>Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified.</br>More info: https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore</br>TODO: how do we prevent errors in the filesystem from compromising the machine |  |
| partition | int32 (formatted integer)| `int32` |  | | partition is the partition in the volume that you want to mount.</br>If omitted, the default is to mount by volume name.</br>Examples: For volume /dev/sda1, you specify the partition as "1".</br>Similarly, the volume partition for /dev/sda is "0" (or you can leave the property empty). |  |
| readOnly | boolean| `bool` |  | | readOnly value true will force the readOnly setting in VolumeMounts.</br>More info: https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore |  |
| volumeID | string| `string` |  | | volumeID is unique ID of the persistent disk resource in AWS (Amazon EBS volume).</br>More info: https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore |  |



### <span id="affinity"></span> Affinity


  



**Properties**

| Name | Type | Go type | Required | Default | Description | Example |
|------|------|---------|:--------:| ------- |-------------|---------|
| nodeAffinity | [NodeAffinity](#node-affinity)| `NodeAffinity` |  | |  |  |
| podAffinity | [PodAffinity](#pod-affinity)| `PodAffinity` |  | |  |  |
| podAntiAffinity | [PodAntiAffinity](#pod-anti-affinity)| `PodAntiAffinity` |  | |  |  |



### <span id="amount"></span> Amount


  



[any](#any)

### <span id="parameter"></span> Parameter


> Parameter indicate a passed string parameter to a service template with an optional default value
  





**Properties**

| Name | Type | Go type | Required | Default | Description | Example |
|------|------|---------|:--------:| ------- |-------------|---------|
| default | [AnyString](#any-string)| `AnyString` |  | |  |  |
| description | [AnyString](#any-string)| `AnyString` |  | |  |  |
| enum | [][AnyString](#any-string)| `[]AnyString` |  | | Enum holds a list of string values to choose from, for the actual value of the parameter |  |
| globalName | string| `string` |  | | GlobalName exports an output parameter to the global scope, making it available as</br>'{{workflow.outputs.parameters.XXXX}} and in workflow.status.outputs.parameters |  |
| name | string| `string` |  | | Name is the parameter name |  |
| value | [AnyString](#any-string)| `AnyString` |  | |  |  |
| valueFrom | [ValueFrom](#value-from)| `ValueFrom` |  | |  |  |



### <span id="persistent-volume-access-mode"></span> PersistentVolumeAccessMode


  

| Name | Type | Go type | Default | Description | Example |
|------|------|---------| ------- |-------------|---------|
| PersistentVolumeAccessMode | string| string | |  |  |



### <span id="persistent-volume-claim-spec"></span> PersistentVolumeClaimSpec


> PersistentVolumeClaimSpec describes the common attributes of storage devices
and allows a Source for provider-specific attributes
  





**Properties**

| Name | Type | Go type | Required | Default | Description | Example |
|------|------|---------|:--------:| ------- |-------------|---------|
| accessModes | [][PersistentVolumeAccessMode](#persistent-volume-access-mode)| `[]PersistentVolumeAccessMode` |  | | accessModes contains the desired access modes the volume should have.</br>More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#access-modes-1 |  |
| dataSource | [TypedLocalObjectReference](#typed-local-object-reference)| `TypedLocalObjectReference` |  | |  |  |
| dataSourceRef | [TypedObjectReference](#typed-object-reference)| `TypedObjectReference` |  | |  |  |
| resources | [VolumeResourceRequirements](#volume-resource-requirements)| `VolumeResourceRequirements` |  | |  |  |
| selector | [LabelSelector](#label-selector)| `LabelSelector` |  | |  |  |
| storageClassName | string| `string` |  | | storageClassName is the name of the StorageClass required by the claim.</br>More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#class-1 |  |
| volumeAttributesClassName | string| `string` |  | | volumeAttributesClassName may be used to set the VolumeAttributesClass used by this claim.</br>If specified, the CSI driver will create or update the volume with the attributes defined</br>in the corresponding VolumeAttributesClass. This has a different purpose than storageClassName,</br>it can be changed after the claim is created. An empty string value means that no VolumeAttributesClass</br>will be applied to the claim but it's not allowed to reset this field to empty string once it is set.</br>If unspecified and the PersistentVolumeClaim is unbound, the default VolumeAttributesClass</br>will be set by the persistentvolume controller if it exists.</br>If the resource referred to by volumeAttributesClass does not exist, this PersistentVolumeClaim will be</br>set to a Pending state, as reflected by the modifyVolumeStatus field, until such as a resource</br>exists.</br>More info: https://kubernetes.io/docs/concepts/storage/volume-attributes-classes/</br>(Beta) Using this field requires the VolumeAttributesClass feature gate to be enabled (off by default). |  |
| volumeMode | [PersistentVolumeMode](#persistent-volume-mode)| `PersistentVolumeMode` |  | |  |  |
| volumeName | string| `string` |  | | volumeName is the binding reference to the PersistentVolume backing this claim. |  |



### <span id="persistent-volume-claim-template"></span> PersistentVolumeClaimTemplate


> PersistentVolumeClaimTemplate is used to produce
PersistentVolumeClaim objects as part of an EphemeralVolumeSource.
  





**Properties**

| Name | Type | Go type | Required | Default | Description | Example |
|------|------|---------|:--------:| ------- |-------------|---------|
| metadata | [V1ObjectMeta](#v1-object-meta)| `V1ObjectMeta` |  | |  |  |
| spec | [PersistentVolumeClaimSpec](#persistent-volume-claim-spec)| `PersistentVolumeClaimSpec` |  | |  |  |



### <span id="persistent-volume-claim-volume-source"></span> PersistentVolumeClaimVolumeSource


> This volume finds the bound PV and mounts that volume for the pod. A
PersistentVolumeClaimVolumeSource is, essentially, a wrapper around another
type of volume that is owned by someone else (the system).
  





**Properties**

| Name | Type | Go type | Required | Default | Description | Example |
|------|------|---------|:--------:| ------- |-------------|---------|
| claimName | string| `string` |  | | claimName is the name of a PersistentVolumeClaim in the same namespace as the pod using this volume.</br>More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#persistentvolumeclaims |  |
| readOnly | boolean| `bool` |  | | readOnly Will force the ReadOnly setting in VolumeMounts.</br>Default false. |  |



### <span id="persistent-volume-mode"></span> PersistentVolumeMode


  

| Name | Type | Go type | Default | Description | Example |
|------|------|---------| ------- |-------------|---------|
| PersistentVolumeMode | string| string | |  |  |



### <span id="photon-persistent-disk-volume-source"></span> PhotonPersistentDiskVolumeSource


  



**Properties**

| Name | Type | Go type | Required | Default | Description | Example |
|------|------|---------|:--------:| ------- |-------------|---------|
| fsType | string| `string` |  | | fsType is the filesystem type to mount.</br>Must be a filesystem type supported by the host operating system.</br>Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. |  |
| pdID | string| `string` |  | | pdID is the ID that identifies Photon Controller persistent disk |  |



### <span id="plugin"></span> Plugin


> Plugin is an Object with exactly one key
  



[any](#any)

### <span id="pod-affinity"></span> PodAffinity


  



**Properties**

| Name | Type | Go type | Required | Default | Description | Example |
|------|------|---------|:--------:| ------- |-------------|---------|
| preferredDuringSchedulingIgnoredDuringExecution | [][WeightedPodAffinityTerm](#weighted-pod-affinity-term)| `[]*WeightedPodAffinityTerm` |  | | The scheduler will prefer to schedule pods to nodes that satisfy</br>the affinity expressions specified by this field, but it may choose</br>a node that violates one or more of the expressions. The node that is</br>most preferred is the one with the greatest sum of weights, i.e.</br>for each node that meets all of the scheduling requirements (resource</br>request, requiredDuringScheduling affinity expressions, etc.),</br>compute a sum by iterating through the elements of this field and adding</br>"weight" to the sum if the node has pods which matches the corresponding podAffinityTerm; the</br>node(s) with the highest sum are the most preferred. |  |
| requiredDuringSchedulingIgnoredDuringExecution | [][PodAffinityTerm](#pod-affinity-term)| `[]*PodAffinityTerm` |  | | If the affinity requirements specified by this field are not met at</br>scheduling time, the pod will not be scheduled onto the node.</br>If the affinity requirements specified by this field cease to be met</br>at some point during pod execution (e.g. due to a pod label update), the</br>system may or may not try to eventually evict the pod from its node.</br>When there are multiple elements, the lists of nodes corresponding to each</br>podAffinityTerm are intersected, i.e. all terms must be satisfied. |  |



### <span id="pod-affinity-term"></span> PodAffinityTerm


> Defines a set of pods (namely those matching the labelSelector
relative to the given namespace(s)) that this pod should be
co-located (affinity) or not co-located (anti-affinity) with,
where co-located is defined as running on a node whose value of
the label with key <topologyKey> matches that of any node on which
a pod of the set of pods is running
  





**Properties**

| Name | Type | Go type | Required | Default | Description | Example |
|------|------|---------|:--------:| ------- |-------------|---------|
| labelSelector | [LabelSelector](#label-selector)| `LabelSelector` |  | |  |  |
| matchLabelKeys | []string| `[]string` |  | | MatchLabelKeys is a set of pod label keys to select which pods will</br>be taken into consideration. The keys are used to lookup values from the</br>incoming pod labels, those key-value labels are merged with `labelSelector` as `key in (value)`</br>to select the group of existing pods which pods will be taken into consideration</br>for the incoming pod's pod (anti) affinity. Keys that don't exist in the incoming</br>pod labels will be ignored. The default value is empty.</br>The same key is forbidden to exist in both matchLabelKeys and labelSelector.</br>Also, matchLabelKeys cannot be set when labelSelector isn't set.</br>This is a beta field and requires enabling MatchLabelKeysInPodAffinity feature gate (enabled by default). |  |
| mismatchLabelKeys | []string| `[]string` |  | | MismatchLabelKeys is a set of pod label keys to select which pods will</br>be taken into consideration. The keys are used to lookup values from the</br>incoming pod labels, those key-value labels are merged with `labelSelector` as `key notin (value)`</br>to select the group of existing pods which pods will be taken into consideration</br>for the incoming pod's pod (anti) affinity. Keys that don't exist in the incoming</br>pod labels will be ignored. The default value is empty.</br>The same key is forbidden to exist in both mismatchLabelKeys and labelSelector.</br>Also, mismatchLabelKeys cannot be set when labelSelector isn't set.</br>This is a beta field and requires enabling MatchLabelKeysInPodAffinity feature gate (enabled by default). |  |
| namespaceSelector | [LabelSelector](#label-selector)| `LabelSelector` |  | |  |  |
| namespaces | []string| `[]string` |  | | namespaces specifies a static list of namespace names that the term applies to.</br>The term is applied to the union of the namespaces listed in this field</br>and the ones selected by namespaceSelector.</br>null or empty namespaces list and null namespaceSelector means "this pod's namespace". |  |
| topologyKey | string| `string` |  | | This pod should be co-located (affinity) or not co-located (anti-affinity) with the pods matching</br>the labelSelector in the specified namespaces, where co-located is defined as running on a node</br>whose value of the label with key topologyKey matches that of any node on which any of the</br>selected pods is running.</br>Empty topologyKey is not allowed. |  |



### <span id="pod-anti-affinity"></span> PodAntiAffinity


  



**Properties**

| Name | Type | Go type | Required | Default | Description | Example |
|------|------|---------|:--------:| ------- |-------------|---------|
| preferredDuringSchedulingIgnoredDuringExecution | [][WeightedPodAffinityTerm](#weighted-pod-affinity-term)| `[]*WeightedPodAffinityTerm` |  | | The scheduler will prefer to schedule pods to nodes that satisfy</br>the anti-affinity expressions specified by this field, but it may choose</br>a node that violates one or more of the expressions. The node that is</br>most preferred is the one with the greatest sum of weights, i.e.</br>for each node that meets all of the scheduling requirements (resource</br>request, requiredDuringScheduling anti-affinity expressions, etc.),</br>compute a sum by iterating through the elements of this field and adding</br>"weight" to the sum if the node has pods which matches the corresponding podAffinityTerm; the</br>node(s) with the highest sum are the most preferred. |  |
| requiredDuringSchedulingIgnoredDuringExecution | [][PodAffinityTerm](#pod-affinity-term)| `[]*PodAffinityTerm` |  | | If the anti-affinity requirements specified by this field are not met at</br>scheduling time, the pod will not be scheduled onto the node.</br>If the anti-affinity requirements specified by this field cease to be met</br>at some point during pod execution (e.g. due to a pod label update), the</br>system may or may not try to eventually evict the pod from its node.</br>When there are multiple elements, the lists of nodes corresponding to each</br>podAffinityTerm are intersected, i.e. all terms must be satisfied. |  |



### <span id="pod-f-s-group-change-policy"></span> PodFSGroupChangePolicy


> PodFSGroupChangePolicy holds policies that will be used for applying fsGroup to a volume
when volume is mounted.
  



| Name | Type | Go type | Default | Description | Example |
|------|------|---------| ------- |-------------|---------|
| PodFSGroupChangePolicy | string| string | | PodFSGroupChangePolicy holds policies that will be used for applying fsGroup to a volume</br>when volume is mounted. |  |



### <span id="pod-s-e-linux-change-policy"></span> PodSELinuxChangePolicy


  

| Name | Type | Go type | Default | Description | Example |
|------|------|---------| ------- |-------------|---------|
| PodSELinuxChangePolicy | string| string | |  |  |



### <span id="pod-security-context"></span> PodSecurityContext


> Some fields are also present in container.securityContext.  Field values of
container.securityContext take precedence over field values of PodSecurityContext.
  





**Properties**

| Name | Type | Go type | Required | Default | Description | Example |
|------|------|---------|:--------:| ------- |-------------|---------|
| appArmorProfile | [AppArmorProfile](#app-armor-profile)| `AppArmorProfile` |  | |  |  |
| fsGroup | int64 (formatted integer)| `int64` |  | | A special supplemental group that applies to all containers in a pod.</br>Some volume types allow the Kubelet to change the ownership of that volume</br>to be owned by the pod:</br></br>1. The owning GID will be the FSGroup</br>2. The setgid bit is set (new files created in the volume will be owned by FSGroup)</br>3. The permission bits are OR'd with rw-rw----</br></br>If unset, the Kubelet will not modify the ownership and permissions of any volume.</br>Note that this field cannot be set when spec.os.name is windows. |  |
| fsGroupChangePolicy | [PodFSGroupChangePolicy](#pod-f-s-group-change-policy)| `PodFSGroupChangePolicy` |  | |  |  |
| runAsGroup | int64 (formatted integer)| `int64` |  | | The GID to run the entrypoint of the container process.</br>Uses runtime default if unset.</br>May also be set in SecurityContext.  If set in both SecurityContext and</br>PodSecurityContext, the value specified in SecurityContext takes precedence</br>for that container.</br>Note that this field cannot be set when spec.os.name is windows. |  |
| runAsNonRoot | boolean| `bool` |  | | Indicates that the container must run as a non-root user.</br>If true, the Kubelet will validate the image at runtime to ensure that it</br>does not run as UID 0 (root) and fail to start the container if it does.</br>If unset or false, no such validation will be performed.</br>May also be set in SecurityContext.  If set in both SecurityContext and</br>PodSecurityContext, the value specified in SecurityContext takes precedence. |  |
| runAsUser | int64 (formatted integer)| `int64` |  | | The UID to run the entrypoint of the container process.</br>Defaults to user specified in image metadata if unspecified.</br>May also be set in SecurityContext.  If set in both SecurityContext and</br>PodSecurityContext, the value specified in SecurityContext takes precedence</br>for that container.</br>Note that this field cannot be set when spec.os.name is windows. |  |
| seLinuxChangePolicy | [PodSELinuxChangePolicy](#pod-s-e-linux-change-policy)| `PodSELinuxChangePolicy` |  | |  |  |
| seLinuxOptions | [SELinuxOptions](#s-e-linux-options)| `SELinuxOptions` |  | |  |  |
| seccompProfile | [SeccompProfile](#seccomp-profile)| `SeccompProfile` |  | |  |  |
| supplementalGroups | []int64 (formatted integer)| `[]int64` |  | | A list of groups applied to the first process run in each container, in</br>addition to the container's primary GID and fsGroup (if specified).  If</br>the SupplementalGroupsPolicy feature is enabled, the</br>supplementalGroupsPolicy field determines whether these are in addition</br>to or instead of any group memberships defined in the container image.</br>If unspecified, no additional groups are added, though group memberships</br>defined in the container image may still be used, depending on the</br>supplementalGroupsPolicy field.</br>Note that this field cannot be set when spec.os.name is windows. |  |
| supplementalGroupsPolicy | [SupplementalGroupsPolicy](#supplemental-groups-policy)| `SupplementalGroupsPolicy` |  | |  |  |
| sysctls | [][Sysctl](#sysctl)| `[]*Sysctl` |  | | Sysctls hold a list of namespaced sysctls used for the pod. Pods with unsupported</br>sysctls (by the container runtime) might fail to launch.</br>Note that this field cannot be set when spec.os.name is windows. |  |
| windowsOptions | [WindowsSecurityContextOptions](#windows-security-context-options)| `WindowsSecurityContextOptions` |  | |  |  |



### <span id="portworx-volume-source"></span> PortworxVolumeSource


  



**Properties**

| Name | Type | Go type | Required | Default | Description | Example |
|------|------|---------|:--------:| ------- |-------------|---------|
| fsType | string| `string` |  | | fSType represents the filesystem type to mount</br>Must be a filesystem type supported by the host operating system.</br>Ex. "ext4", "xfs". Implicitly inferred to be "ext4" if unspecified. |  |
| readOnly | boolean| `bool` |  | | readOnly defaults to false (read/write). ReadOnly here will force</br>the ReadOnly setting in VolumeMounts. |  |
| volumeID | string| `string` |  | | volumeID uniquely identifies a Portworx volume |  |



### <span id="preferred-scheduling-term"></span> PreferredSchedulingTerm


> An empty preferred scheduling term matches all objects with implicit weight 0
(i.e. it's a no-op). A null preferred scheduling term matches no objects (i.e. is also a no-op).
  





**Properties**

| Name | Type | Go type | Required | Default | Description | Example |
|------|------|---------|:--------:| ------- |-------------|---------|
| preference | [NodeSelectorTerm](#node-selector-term)| `NodeSelectorTerm` |  | |  |  |
| weight | int32 (formatted integer)| `int32` |  | | Weight associated with matching the corresponding nodeSelectorTerm, in the range 1-100. |  |



### <span id="probe"></span> Probe


> Probe describes a health check to be performed against a container to determine whether it is
alive or ready to receive traffic.
  





**Properties**

| Name | Type | Go type | Required | Default | Description | Example |
|------|------|---------|:--------:| ------- |-------------|---------|
| exec | [ExecAction](#exec-action)| `ExecAction` |  | |  |  |
| failureThreshold | int32 (formatted integer)| `int32` |  | | Minimum consecutive failures for the probe to be considered failed after having succeeded.</br>Defaults to 3. Minimum value is 1. |  |
| grpc | [GRPCAction](#g-rpc-action)| `GRPCAction` |  | |  |  |
| httpGet | [HTTPGetAction](#http-get-action)| `HTTPGetAction` |  | |  |  |
| initialDelaySeconds | int32 (formatted integer)| `int32` |  | | Number of seconds after the container has started before liveness probes are initiated.</br>More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes |  |
| periodSeconds | int32 (formatted integer)| `int32` |  | | How often (in seconds) to perform the probe.</br>Default to 10 seconds. Minimum value is 1. |  |
| successThreshold | int32 (formatted integer)| `int32` |  | | Minimum consecutive successes for the probe to be considered successful after having failed.</br>Defaults to 1. Must be 1 for liveness and startup. Minimum value is 1. |  |
| tcpSocket | [TCPSocketAction](#tcp-socket-action)| `TCPSocketAction` |  | |  |  |
| terminationGracePeriodSeconds | int64 (formatted integer)| `int64` |  | | Optional duration in seconds the pod needs to terminate gracefully upon probe failure.</br>The grace period is the duration in seconds after the processes running in the pod are sent</br>a termination signal and the time when the processes are forcibly halted with a kill signal.</br>Set this value longer than the expected cleanup time for your process.</br>If this value is nil, the pod's terminationGracePeriodSeconds will be used. Otherwise, this</br>value overrides the value provided by the pod spec.</br>Value must be non-negative integer. The value zero indicates stop immediately via</br>the kill signal (no opportunity to shut down).</br>This is a beta field and requires enabling ProbeTerminationGracePeriod feature gate.</br>Minimum value is 1. spec.terminationGracePeriodSeconds is used if unset. |  |
| timeoutSeconds | int32 (formatted integer)| `int32` |  | | Number of seconds after which the probe times out.</br>Defaults to 1 second. Minimum value is 1.</br>More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes |  |



### <span id="proc-mount-type"></span> ProcMountType


  

| Name | Type | Go type | Default | Description | Example |
|------|------|---------| ------- |-------------|---------|
| ProcMountType | string| string | |  |  |



### <span id="progress"></span> Progress


  

| Name | Type | Go type | Default | Description | Example |
|------|------|---------| ------- |-------------|---------|
| Progress | string| string | |  |  |



### <span id="projected-volume-source"></span> ProjectedVolumeSource


> Represents a projected volume source
  





**Properties**

| Name | Type | Go type | Required | Default | Description | Example |
|------|------|---------|:--------:| ------- |-------------|---------|
| defaultMode | int32 (formatted integer)| `int32` |  | | defaultMode are the mode bits used to set permissions on created files by default.</br>Must be an octal value between 0000 and 0777 or a decimal value between 0 and 511.</br>YAML accepts both octal and decimal values, JSON requires decimal values for mode bits.</br>Directories within the path are not affected by this setting.</br>This might be in conflict with other options that affect the file</br>mode, like fsGroup, and the result can be other mode bits set. |  |
| sources | [][VolumeProjection](#volume-projection)| `[]*VolumeProjection` |  | | sources is the list of volume projections. Each entry in this list</br>handles one source. |  |



### <span id="prometheus"></span> Prometheus


> Prometheus is a prometheus metric to be emitted
  





**Properties**

| Name | Type | Go type | Required | Default | Description | Example |
|------|------|---------|:--------:| ------- |-------------|---------|
| counter | [Counter](#counter)| `Counter` |  | |  |  |
| gauge | [Gauge](#gauge)| `Gauge` |  | |  |  |
| help | string| `string` |  | | Help is a string that describes the metric |  |
| histogram | [Histogram](#histogram)| `Histogram` |  | |  |  |
| labels | [][MetricLabel](#metric-label)| `[]*MetricLabel` |  | | Labels is a list of metric labels |  |
| name | string| `string` |  | | Name is the name of the metric |  |
| when | string| `string` |  | | When is a conditional statement that decides when to emit the metric |  |



### <span id="protocol"></span> Protocol


  

| Name | Type | Go type | Default | Description | Example |
|------|------|---------| ------- |-------------|---------|
| Protocol | string| string | |  |  |



### <span id="pull-policy"></span> PullPolicy


> PullPolicy describes a policy for if/when to pull a container image
  



| Name | Type | Go type | Default | Description | Example |
|------|------|---------| ------- |-------------|---------|
| PullPolicy | string| string | | PullPolicy describes a policy for if/when to pull a container image |  |



### <span id="quantity"></span> Quantity


> The serialization format is:

```
<quantity>        ::= <signedNumber><suffix>

(Note that <suffix> may be empty, from the "" case in <decimalSI>.)

<digit>           ::= 0 | 1 | ... | 9
<digits>          ::= <digit> | <digit><digits>
<number>          ::= <digits> | <digits>.<digits> | <digits>. | .<digits>
<sign>            ::= "+" | "-"
<signedNumber>    ::= <number> | <sign><number>
<suffix>          ::= <binarySI> | <decimalExponent> | <decimalSI>
<binarySI>        ::= Ki | Mi | Gi | Ti | Pi | Ei

(International System of units; See: http://physics.nist.gov/cuu/Units/binary.html)

<decimalSI>       ::= m | "" | k | M | G | T | P | E

(Note that 1024 = 1Ki but 1000 = 1k; I didn't choose the capitalization.)

<decimalExponent> ::= "e" <signedNumber> | "E" <signedNumber>
```

No matter which of the three exponent forms is used, no quantity may represent
a number greater than 2^63-1 in magnitude, nor may it have more than 3 decimal
places. Numbers larger or more precise will be capped or rounded up.
(E.g.: 0.1m will rounded up to 1m.)
This may be extended in the future if we require larger or smaller quantities.

When a Quantity is parsed from a string, it will remember the type of suffix
it had, and will use the same type again when it is serialized.

Before serializing, Quantity will be put in "canonical form".
This means that Exponent/suffix will be adjusted up or down (with a
corresponding increase or decrease in Mantissa) such that:

- No precision is lost
- No fractional digits will be emitted
- The exponent (or suffix) is as large as possible.

The sign will be omitted unless the number is negative.

Examples:

- 1.5 will be serialized as "1500m"
- 1.5Gi will be serialized as "1536Mi"

Note that the quantity will NEVER be internally represented by a
floating point number. That is the whole point of this exercise.

Non-canonical values will still parse as long as they are well formed,
but will be re-emitted in their canonical form. (So always use canonical
form, or don't diff.)

This format is intended to make it difficult to use these numbers without
writing some sort of special handling code in the hopes that that will
cause implementors to also use a fixed point implementation.
  



[any](#any)

### <span id="quobyte-volume-source"></span> QuobyteVolumeSource


> Quobyte volumes do not support ownership management or SELinux relabeling.
  





**Properties**

| Name | Type | Go type | Required | Default | Description | Example |
|------|------|---------|:--------:| ------- |-------------|---------|
| group | string| `string` |  | | group to map volume access to</br>Default is no group |  |
| readOnly | boolean| `bool` |  | | readOnly here will force the Quobyte volume to be mounted with read-only permissions.</br>Defaults to false. |  |
| registry | string| `string` |  | | registry represents a single or multiple Quobyte Registry services</br>specified as a string as host:port pair (multiple entries are separated with commas)</br>which acts as the central registry for volumes |  |
| tenant | string| `string` |  | | tenant owning the given Quobyte volume in the Backend</br>Used with dynamically provisioned Quobyte volumes, value is set by the plugin |  |
| user | string| `string` |  | | user to map volume access to</br>Defaults to serivceaccount user |  |
| volume | string| `string` |  | | volume is a string that references an already created Quobyte volume by name. |  |



### <span id="r-b-d-volume-source"></span> RBDVolumeSource


> RBD volumes support ownership management and SELinux relabeling.
  





**Properties**

| Name | Type | Go type | Required | Default | Description | Example |
|------|------|---------|:--------:| ------- |-------------|---------|
| fsType | string| `string` |  | | fsType is the filesystem type of the volume that you want to mount.</br>Tip: Ensure that the filesystem type is supported by the host operating system.</br>Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified.</br>More info: https://kubernetes.io/docs/concepts/storage/volumes#rbd</br>TODO: how do we prevent errors in the filesystem from compromising the machine |  |
| image | string| `string` |  | | image is the rados image name.</br>More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it |  |
| keyring | string| `string` |  | | keyring is the path to key ring for RBDUser.</br>Default is /etc/ceph/keyring.</br>More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it |  |
| monitors | []string| `[]string` |  | | monitors is a collection of Ceph monitors.</br>More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it |  |
| pool | string| `string` |  | | pool is the rados pool name.</br>Default is rbd.</br>More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it |  |
| readOnly | boolean| `bool` |  | | readOnly here will force the ReadOnly setting in VolumeMounts.</br>Defaults to false.</br>More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it |  |
| secretRef | [LocalObjectReference](#local-object-reference)| `LocalObjectReference` |  | |  |  |
| user | string| `string` |  | | user is the rados user name.</br>Default is admin.</br>More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it |  |



### <span id="raw-artifact"></span> RawArtifact


> RawArtifact allows raw string content to be placed as an artifact in a container
  





**Properties**

| Name | Type | Go type | Required | Default | Description | Example |
|------|------|---------|:--------:| ------- |-------------|---------|
| data | string| `string` |  | | Data is the string contents of the artifact |  |



### <span id="recursive-read-only-mode"></span> RecursiveReadOnlyMode


  

| Name | Type | Go type | Default | Description | Example |
|------|------|---------| ------- |-------------|---------|
| RecursiveReadOnlyMode | string| string | |  |  |



### <span id="resource-claim"></span> ResourceClaim


  



**Properties**

| Name | Type | Go type | Required | Default | Description | Example |
|------|------|---------|:--------:| ------- |-------------|---------|
| name | string| `string` |  | | Name must match the name of one entry in pod.spec.resourceClaims of</br>the Pod where this field is used. It makes that resource available</br>inside a container. |  |
| request | string| `string` |  | | Request is the name chosen for a request in the referenced claim.</br>If empty, everything from the claim is made available, otherwise</br>only the result of this request. |  |



### <span id="resource-field-selector"></span> ResourceFieldSelector


> ResourceFieldSelector represents container resources (cpu, memory) and their output format
  





**Properties**

| Name | Type | Go type | Required | Default | Description | Example |
|------|------|---------|:--------:| ------- |-------------|---------|
| containerName | string| `string` |  | | Container name: required for volumes, optional for env vars |  |
| divisor | [Quantity](#quantity)| `Quantity` |  | |  |  |
| resource | string| `string` |  | |  |  |



### <span id="resource-list"></span> ResourceList


  

[ResourceList](#resource-list)

### <span id="resource-name"></span> ResourceName


  

| Name | Type | Go type | Default | Description | Example |
|------|------|---------| ------- |-------------|---------|
| ResourceName | string| string | |  |  |



### <span id="resource-requirements"></span> ResourceRequirements


  



**Properties**

| Name | Type | Go type | Required | Default | Description | Example |
|------|------|---------|:--------:| ------- |-------------|---------|
| claims | [][ResourceClaim](#resource-claim)| `[]*ResourceClaim` |  | | Claims lists the names of resources, defined in spec.resourceClaims,</br>that are used by this container.</br></br>This is an alpha field and requires enabling the</br>DynamicResourceAllocation feature gate.</br></br>This field is immutable. It can only be set for containers. |  |
| limits | [ResourceList](#resource-list)| `ResourceList` |  | |  |  |
| requests | [ResourceList](#resource-list)| `ResourceList` |  | |  |  |



### <span id="resource-resize-restart-policy"></span> ResourceResizeRestartPolicy


  

| Name | Type | Go type | Default | Description | Example |
|------|------|---------| ------- |-------------|---------|
| ResourceResizeRestartPolicy | string| string | |  |  |



### <span id="resource-template"></span> ResourceTemplate


> ResourceTemplate is a template subtype to manipulate kubernetes resources
  





**Properties**

| Name | Type | Go type | Required | Default | Description | Example |
|------|------|---------|:--------:| ------- |-------------|---------|
| action | string| `string` |  | | Action is the action to perform to the resource.</br>Must be one of: get, create, apply, delete, replace, patch |  |
| failureCondition | string| `string` |  | | FailureCondition is a label selector expression which describes the conditions</br>of the k8s resource in which the step was considered failed |  |
| flags | []string| `[]string` |  | | Flags is a set of additional options passed to kubectl before submitting a resource</br>I.e. to disable resource validation:</br>flags: [</br>"--validate=false"  # disable resource validation</br>] |  |
| manifest | string| `string` |  | | Manifest contains the kubernetes manifest |  |
| manifestFrom | [ManifestFrom](#manifest-from)| `ManifestFrom` |  | |  |  |
| mergeStrategy | string| `string` |  | | MergeStrategy is the strategy used to merge a patch. It defaults to "strategic"</br>Must be one of: strategic, merge, json |  |
| setOwnerReference | boolean| `bool` |  | | SetOwnerReference sets the reference to the workflow on the OwnerReference of generated resource. |  |
| successCondition | string| `string` |  | | SuccessCondition is a label selector expression which describes the conditions</br>of the k8s resource in which it is acceptable to proceed to the following step |  |



### <span id="retry-affinity"></span> RetryAffinity


  



**Properties**

| Name | Type | Go type | Required | Default | Description | Example |
|------|------|---------|:--------:| ------- |-------------|---------|
| nodeAntiAffinity | [RetryNodeAntiAffinity](#retry-node-anti-affinity)| `RetryNodeAntiAffinity` |  | |  |  |



### <span id="retry-node-anti-affinity"></span> RetryNodeAntiAffinity


> In order to prevent running steps on the same host, it uses "kubernetes.io/hostname".
  



[any](#any)

### <span id="retry-policy"></span> RetryPolicy


  

| Name | Type | Go type | Default | Description | Example |
|------|------|---------| ------- |-------------|---------|
| RetryPolicy | string| string | |  |  |



### <span id="retry-strategy"></span> RetryStrategy


> RetryStrategy provides controls on how to retry a workflow step
  





**Properties**

| Name | Type | Go type | Required | Default | Description | Example |
|------|------|---------|:--------:| ------- |-------------|---------|
| affinity | [RetryAffinity](#retry-affinity)| `RetryAffinity` |  | |  |  |
| backoff | [Backoff](#backoff)| `Backoff` |  | |  |  |
| expression | string| `string` |  | | Expression is a condition expression for when a node will be retried. If it evaluates to false, the node will not</br>be retried and the retry strategy will be ignored |  |
| limit | [IntOrString](#int-or-string)| `IntOrString` |  | |  |  |
| retryPolicy | [RetryPolicy](#retry-policy)| `RetryPolicy` |  | |  |  |



### <span id="s3-artifact"></span> S3Artifact


> S3Artifact is the location of an S3 artifact
  





**Properties**

| Name | Type | Go type | Required | Default | Description | Example |
|------|------|---------|:--------:| ------- |-------------|---------|
| accessKeySecret | [SecretKeySelector](#secret-key-selector)| `SecretKeySelector` |  | |  |  |
| bucket | string| `string` |  | | Bucket is the name of the bucket |  |
| caSecret | [SecretKeySelector](#secret-key-selector)| `SecretKeySelector` |  | |  |  |
| createBucketIfNotPresent | [CreateS3BucketOptions](#create-s3-bucket-options)| `CreateS3BucketOptions` |  | |  |  |
| encryptionOptions | [S3EncryptionOptions](#s3-encryption-options)| `S3EncryptionOptions` |  | |  |  |
| endpoint | string| `string` |  | | Endpoint is the hostname of the bucket endpoint |  |
| insecure | boolean| `bool` |  | | Insecure will connect to the service with TLS |  |
| key | string| `string` |  | | Key is the key in the bucket where the artifact resides |  |
| region | string| `string` |  | | Region contains the optional bucket region |  |
| roleARN | string| `string` |  | | RoleARN is the Amazon Resource Name (ARN) of the role to assume. |  |
| secretKeySecret | [SecretKeySelector](#secret-key-selector)| `SecretKeySelector` |  | |  |  |
| sessionTokenSecret | [SecretKeySelector](#secret-key-selector)| `SecretKeySelector` |  | |  |  |
| useSDKCreds | boolean| `bool` |  | | UseSDKCreds tells the driver to figure out credentials based on sdk defaults. |  |



### <span id="s3-encryption-options"></span> S3EncryptionOptions


> S3EncryptionOptions used to determine encryption options during s3 operations
  





**Properties**

| Name | Type | Go type | Required | Default | Description | Example |
|------|------|---------|:--------:| ------- |-------------|---------|
| enableEncryption | boolean| `bool` |  | | EnableEncryption tells the driver to encrypt objects if set to true. If kmsKeyId and serverSideCustomerKeySecret are not set, SSE-S3 will be used |  |
| kmsEncryptionContext | string| `string` |  | | KmsEncryptionContext is a json blob that contains an encryption context. See https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#encrypt_context for more information |  |
| kmsKeyId | string| `string` |  | | KMSKeyId tells the driver to encrypt the object using the specified KMS Key. |  |
| serverSideCustomerKeySecret | [SecretKeySelector](#secret-key-selector)| `SecretKeySelector` |  | |  |  |



### <span id="s-e-linux-options"></span> SELinuxOptions


> SELinuxOptions are the labels to be applied to the container
  





**Properties**

| Name | Type | Go type | Required | Default | Description | Example |
|------|------|---------|:--------:| ------- |-------------|---------|
| level | string| `string` |  | | Level is SELinux level label that applies to the container. |  |
| role | string| `string` |  | | Role is a SELinux role label that applies to the container. |  |
| type | string| `string` |  | | Type is a SELinux type label that applies to the container. |  |
| user | string| `string` |  | | User is a SELinux user label that applies to the container. |  |



### <span id="scale-i-o-volume-source"></span> ScaleIOVolumeSource


> ScaleIOVolumeSource represents a persistent ScaleIO volume
  





**Properties**

| Name | Type | Go type | Required | Default | Description | Example |
|------|------|---------|:--------:| ------- |-------------|---------|
| fsType | string| `string` |  | | fsType is the filesystem type to mount.</br>Must be a filesystem type supported by the host operating system.</br>Ex. "ext4", "xfs", "ntfs".</br>Default is "xfs". |  |
| gateway | string| `string` |  | | gateway is the host address of the ScaleIO API Gateway. |  |
| protectionDomain | string| `string` |  | | protectionDomain is the name of the ScaleIO Protection Domain for the configured storage. |  |
| readOnly | boolean| `bool` |  | | readOnly Defaults to false (read/write). ReadOnly here will force</br>the ReadOnly setting in VolumeMounts. |  |
| secretRef | [LocalObjectReference](#local-object-reference)| `LocalObjectReference` |  | |  |  |
| sslEnabled | boolean| `bool` |  | | sslEnabled Flag enable/disable SSL communication with Gateway, default false |  |
| storageMode | string| `string` |  | | storageMode indicates whether the storage for a volume should be ThickProvisioned or ThinProvisioned.</br>Default is ThinProvisioned. |  |
| storagePool | string| `string` |  | | storagePool is the ScaleIO Storage Pool associated with the protection domain. |  |
| system | string| `string` |  | | system is the name of the storage system as configured in ScaleIO. |  |
| volumeName | string| `string` |  | | volumeName is the name of a volume already created in the ScaleIO system</br>that is associated with this volume source. |  |



### <span id="script-template"></span> ScriptTemplate


> ScriptTemplate is a template subtype to enable scripting through code steps
  





**Properties**

| Name | Type | Go type | Required | Default | Description | Example |
|------|------|---------|:--------:| ------- |-------------|---------|
| args | []string| `[]string` |  | | Arguments to the entrypoint.</br>The container image's CMD is used if this is not provided.</br>Variable references $(VAR_NAME) are expanded using the container's environment. If a variable</br>cannot be resolved, the reference in the input string will be unchanged. Double $$ are reduced</br>to a single $, which allows for escaping the $(VAR_NAME) syntax: i.e. "$$(VAR_NAME)" will</br>produce the string literal "$(VAR_NAME)". Escaped references will never be expanded, regardless</br>of whether the variable exists or not. Cannot be updated.</br>More info: https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell |  |
| command | []string| `[]string` |  | | Entrypoint array. Not executed within a shell.</br>The container image's ENTRYPOINT is used if this is not provided.</br>Variable references $(VAR_NAME) are expanded using the container's environment. If a variable</br>cannot be resolved, the reference in the input string will be unchanged. Double $$ are reduced</br>to a single $, which allows for escaping the $(VAR_NAME) syntax: i.e. "$$(VAR_NAME)" will</br>produce the string literal "$(VAR_NAME)". Escaped references will never be expanded, regardless</br>of whether the variable exists or not. Cannot be updated.</br>More info: https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell |  |
| env | [][EnvVar](#env-var)| `[]*EnvVar` |  | | List of environment variables to set in the container.</br>Cannot be updated. |  |
| envFrom | [][EnvFromSource](#env-from-source)| `[]*EnvFromSource` |  | | List of sources to populate environment variables in the container.</br>The keys defined within a source must be a C_IDENTIFIER. All invalid keys</br>will be reported as an event when the container is starting. When a key exists in multiple</br>sources, the value associated with the last source will take precedence.</br>Values defined by an Env with a duplicate key will take precedence.</br>Cannot be updated. |  |
| image | string| `string` |  | | Container image name.</br>More info: https://kubernetes.io/docs/concepts/containers/images</br>This field is optional to allow higher level config management to default or override</br>container images in workload controllers like Deployments and StatefulSets. |  |
| imagePullPolicy | [PullPolicy](#pull-policy)| `PullPolicy` |  | |  |  |
| lifecycle | [Lifecycle](#lifecycle)| `Lifecycle` |  | |  |  |
| livenessProbe | [Probe](#probe)| `Probe` |  | |  |  |
| name | string| `string` |  | | Name of the container specified as a DNS_LABEL.</br>Each container in a pod must have a unique name (DNS_LABEL).</br>Cannot be updated. |  |
| ports | [][ContainerPort](#container-port)| `[]*ContainerPort` |  | | List of ports to expose from the container. Not specifying a port here</br>DOES NOT prevent that port from being exposed. Any port which is</br>listening on the default "0.0.0.0" address inside a container will be</br>accessible from the network.</br>Modifying this array with strategic merge patch may corrupt the data.</br>For more information See https://github.com/kubernetes/kubernetes/issues/108255.</br>Cannot be updated. |  |
| readinessProbe | [Probe](#probe)| `Probe` |  | |  |  |
| resizePolicy | [][ContainerResizePolicy](#container-resize-policy)| `[]*ContainerResizePolicy` |  | | Resources resize policy for the container. |  |
| resources | [ResourceRequirements](#resource-requirements)| `ResourceRequirements` |  | |  |  |
| restartPolicy | [ContainerRestartPolicy](#container-restart-policy)| `ContainerRestartPolicy` |  | |  |  |
| securityContext | [SecurityContext](#security-context)| `SecurityContext` |  | |  |  |
| source | string| `string` |  | | Source contains the source code of the script to execute |  |
| startupProbe | [Probe](#probe)| `Probe` |  | |  |  |
| stdin | boolean| `bool` |  | | Whether this container should allocate a buffer for stdin in the container runtime. If this</br>is not set, reads from stdin in the container will always result in EOF.</br>Default is false. |  |
| stdinOnce | boolean| `bool` |  | | Whether the container runtime should close the stdin channel after it has been opened by</br>a single attach. When stdin is true the stdin stream will remain open across multiple attach</br>sessions. If stdinOnce is set to true, stdin is opened on container start, is empty until the</br>first client attaches to stdin, and then remains open and accepts data until the client disconnects,</br>at which time stdin is closed and remains closed until the container is restarted. If this</br>flag is false, a container processes that reads from stdin will never receive an EOF.</br>Default is false |  |
| terminationMessagePath | string| `string` |  | | Optional: Path at which the file to which the container's termination message</br>will be written is mounted into the container's filesystem.</br>Message written is intended to be brief final status, such as an assertion failure message.</br>Will be truncated by the node if greater than 4096 bytes. The total message length across</br>all containers will be limited to 12kb.</br>Defaults to /dev/termination-log.</br>Cannot be updated. |  |
| terminationMessagePolicy | [TerminationMessagePolicy](#termination-message-policy)| `TerminationMessagePolicy` |  | |  |  |
| tty | boolean| `bool` |  | | Whether this container should allocate a TTY for itself, also requires 'stdin' to be true.</br>Default is false. |  |
| volumeDevices | [][VolumeDevice](#volume-device)| `[]*VolumeDevice` |  | | volumeDevices is the list of block devices to be used by the container. |  |
| volumeMounts | [][VolumeMount](#volume-mount)| `[]*VolumeMount` |  | | Pod volumes to mount into the container's filesystem.</br>Cannot be updated. |  |
| workingDir | string| `string` |  | | Container's working directory.</br>If not specified, the container runtime's default will be used, which</br>might be configured in the container image.</br>Cannot be updated. |  |



### <span id="seccomp-profile"></span> SeccompProfile


> Only one profile source may be set.
  





**Properties**

| Name | Type | Go type | Required | Default | Description | Example |
|------|------|---------|:--------:| ------- |-------------|---------|
| localhostProfile | string| `string` |  | | localhostProfile indicates a profile defined in a file on the node should be used.</br>The profile must be preconfigured on the node to work.</br>Must be a descending path, relative to the kubelet's configured seccomp profile location.</br>Must be set if type is "Localhost". Must NOT be set for any other type. |  |
| type | [SeccompProfileType](#seccomp-profile-type)| `SeccompProfileType` |  | |  |  |



### <span id="seccomp-profile-type"></span> SeccompProfileType


  

| Name | Type | Go type | Default | Description | Example |
|------|------|---------| ------- |-------------|---------|
| SeccompProfileType | string| string | |  |  |



### <span id="secret-env-source"></span> SecretEnvSource


> The contents of the target Secret's Data field will represent the
key-value pairs as environment variables.
  





**Properties**

| Name | Type | Go type | Required | Default | Description | Example |
|------|------|---------|:--------:| ------- |-------------|---------|
| name | string| `string` |  | | Name of the referent.</br>This field is effectively required, but due to backwards compatibility is</br>allowed to be empty. Instances of this type with an empty value here are</br>almost certainly wrong.</br>More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names</br>TODO: Drop `kubebuilder:default` when controller-gen doesn't need it https://github.com/kubernetes-sigs/kubebuilder/issues/3896. |  |
| optional | boolean| `bool` |  | | Specify whether the Secret must be defined |  |



### <span id="secret-key-selector"></span> SecretKeySelector


  



**Properties**

| Name | Type | Go type | Required | Default | Description | Example |
|------|------|---------|:--------:| ------- |-------------|---------|
| key | string| `string` |  | | The key of the secret to select from.  Must be a valid secret key. |  |
| name | string| `string` |  | | Name of the referent.</br>This field is effectively required, but due to backwards compatibility is</br>allowed to be empty. Instances of this type with an empty value here are</br>almost certainly wrong.</br>More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names</br>TODO: Drop `kubebuilder:default` when controller-gen doesn't need it https://github.com/kubernetes-sigs/kubebuilder/issues/3896. |  |
| optional | boolean| `bool` |  | | Specify whether the Secret or its key must be defined |  |



### <span id="secret-projection"></span> SecretProjection


> The contents of the target Secret's Data field will be presented in a
projected volume as files using the keys in the Data field as the file names.
Note that this is identical to a secret volume source without the default
mode.
  





**Properties**

| Name | Type | Go type | Required | Default | Description | Example |
|------|------|---------|:--------:| ------- |-------------|---------|
| items | [][KeyToPath](#key-to-path)| `[]*KeyToPath` |  | | items if unspecified, each key-value pair in the Data field of the referenced</br>Secret will be projected into the volume as a file whose name is the</br>key and content is the value. If specified, the listed keys will be</br>projected into the specified paths, and unlisted keys will not be</br>present. If a key is specified which is not present in the Secret,</br>the volume setup will error unless it is marked optional. Paths must be</br>relative and may not contain the '..' path or start with '..'. |  |
| name | string| `string` |  | | Name of the referent.</br>This field is effectively required, but due to backwards compatibility is</br>allowed to be empty. Instances of this type with an empty value here are</br>almost certainly wrong.</br>More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names</br>TODO: Drop `kubebuilder:default` when controller-gen doesn't need it https://github.com/kubernetes-sigs/kubebuilder/issues/3896. |  |
| optional | boolean| `bool` |  | | optional field specify whether the Secret or its key must be defined |  |



### <span id="secret-volume-source"></span> SecretVolumeSource


> The contents of the target Secret's Data field will be presented in a volume
as files using the keys in the Data field as the file names.
Secret volumes support ownership management and SELinux relabeling.
  





**Properties**

| Name | Type | Go type | Required | Default | Description | Example |
|------|------|---------|:--------:| ------- |-------------|---------|
| defaultMode | int32 (formatted integer)| `int32` |  | | defaultMode is Optional: mode bits used to set permissions on created files by default.</br>Must be an octal value between 0000 and 0777 or a decimal value between 0 and 511.</br>YAML accepts both octal and decimal values, JSON requires decimal values</br>for mode bits. Defaults to 0644.</br>Directories within the path are not affected by this setting.</br>This might be in conflict with other options that affect the file</br>mode, like fsGroup, and the result can be other mode bits set. |  |
| items | [][KeyToPath](#key-to-path)| `[]*KeyToPath` |  | | items If unspecified, each key-value pair in the Data field of the referenced</br>Secret will be projected into the volume as a file whose name is the</br>key and content is the value. If specified, the listed keys will be</br>projected into the specified paths, and unlisted keys will not be</br>present. If a key is specified which is not present in the Secret,</br>the volume setup will error unless it is marked optional. Paths must be</br>relative and may not contain the '..' path or start with '..'. |  |
| optional | boolean| `bool` |  | | optional field specify whether the Secret or its keys must be defined |  |
| secretName | string| `string` |  | | secretName is the name of the secret in the pod's namespace to use.</br>More info: https://kubernetes.io/docs/concepts/storage/volumes#secret |  |



### <span id="security-context"></span> SecurityContext


> Some fields are present in both SecurityContext and PodSecurityContext.  When both
are set, the values in SecurityContext take precedence.
  





**Properties**

| Name | Type | Go type | Required | Default | Description | Example |
|------|------|---------|:--------:| ------- |-------------|---------|
| allowPrivilegeEscalation | boolean| `bool` |  | | AllowPrivilegeEscalation controls whether a process can gain more</br>privileges than its parent process. This bool directly controls if</br>the no_new_privs flag will be set on the container process.</br>AllowPrivilegeEscalation is true always when the container is:</br>1) run as Privileged</br>2) has CAP_SYS_ADMIN</br>Note that this field cannot be set when spec.os.name is windows. |  |
| appArmorProfile | [AppArmorProfile](#app-armor-profile)| `AppArmorProfile` |  | |  |  |
| capabilities | [Capabilities](#capabilities)| `Capabilities` |  | |  |  |
| privileged | boolean| `bool` |  | | Run container in privileged mode.</br>Processes in privileged containers are essentially equivalent to root on the host.</br>Defaults to false.</br>Note that this field cannot be set when spec.os.name is windows. |  |
| procMount | [ProcMountType](#proc-mount-type)| `ProcMountType` |  | |  |  |
| readOnlyRootFilesystem | boolean| `bool` |  | | Whether this container has a read-only root filesystem.</br>Default is false.</br>Note that this field cannot be set when spec.os.name is windows. |  |
| runAsGroup | int64 (formatted integer)| `int64` |  | | The GID to run the entrypoint of the container process.</br>Uses runtime default if unset.</br>May also be set in PodSecurityContext.  If set in both SecurityContext and</br>PodSecurityContext, the value specified in SecurityContext takes precedence.</br>Note that this field cannot be set when spec.os.name is windows. |  |
| runAsNonRoot | boolean| `bool` |  | | Indicates that the container must run as a non-root user.</br>If true, the Kubelet will validate the image at runtime to ensure that it</br>does not run as UID 0 (root) and fail to start the container if it does.</br>If unset or false, no such validation will be performed.</br>May also be set in PodSecurityContext.  If set in both SecurityContext and</br>PodSecurityContext, the value specified in SecurityContext takes precedence. |  |
| runAsUser | int64 (formatted integer)| `int64` |  | | The UID to run the entrypoint of the container process.</br>Defaults to user specified in image metadata if unspecified.</br>May also be set in PodSecurityContext.  If set in both SecurityContext and</br>PodSecurityContext, the value specified in SecurityContext takes precedence.</br>Note that this field cannot be set when spec.os.name is windows. |  |
| seLinuxOptions | [SELinuxOptions](#s-e-linux-options)| `SELinuxOptions` |  | |  |  |
| seccompProfile | [SeccompProfile](#seccomp-profile)| `SeccompProfile` |  | |  |  |
| windowsOptions | [WindowsSecurityContextOptions](#windows-security-context-options)| `WindowsSecurityContextOptions` |  | |  |  |



### <span id="semaphore-ref"></span> SemaphoreRef


> SemaphoreRef is a reference of Semaphore
  





**Properties**

| Name | Type | Go type | Required | Default | Description | Example |
|------|------|---------|:--------:| ------- |-------------|---------|
| configMapKeyRef | [ConfigMapKeySelector](#config-map-key-selector)| `ConfigMapKeySelector` |  | |  |  |
| namespace | string| `string` |  | | Namespace is the namespace of the configmap, default: [namespace of workflow] |  |



### <span id="sequence"></span> Sequence


> Sequence expands a workflow step into numeric range
  





**Properties**

| Name | Type | Go type | Required | Default | Description | Example |
|------|------|---------|:--------:| ------- |-------------|---------|
| count | [IntOrString](#int-or-string)| `IntOrString` |  | |  |  |
| end | [IntOrString](#int-or-string)| `IntOrString` |  | |  |  |
| format | string| `string` |  | | Format is a printf format string to format the value in the sequence |  |
| start | [IntOrString](#int-or-string)| `IntOrString` |  | |  |  |



### <span id="service-account-token-projection"></span> ServiceAccountTokenProjection


> ServiceAccountTokenProjection represents a projected service account token
volume. This projection can be used to insert a service account token into
the pods runtime filesystem for use against APIs (Kubernetes API Server or
otherwise).
  





**Properties**

| Name | Type | Go type | Required | Default | Description | Example |
|------|------|---------|:--------:| ------- |-------------|---------|
| audience | string| `string` |  | | audience is the intended audience of the token. A recipient of a token</br>must identify itself with an identifier specified in the audience of the</br>token, and otherwise should reject the token. The audience defaults to the</br>identifier of the apiserver. |  |
| expirationSeconds | int64 (formatted integer)| `int64` |  | | expirationSeconds is the requested duration of validity of the service</br>account token. As the token approaches expiration, the kubelet volume</br>plugin will proactively rotate the service account token. The kubelet will</br>start trying to rotate the token if the token is older than 80 percent of</br>its time to live or if the token is older than 24 hours.Defaults to 1 hour</br>and must be at least 10 minutes. |  |
| path | string| `string` |  | | path is the path relative to the mount point of the file to project the</br>token into. |  |



### <span id="sleep-action"></span> SleepAction


  



**Properties**

| Name | Type | Go type | Required | Default | Description | Example |
|------|------|---------|:--------:| ------- |-------------|---------|
| seconds | int64 (formatted integer)| `int64` |  | | Seconds is the number of seconds to sleep. |  |



### <span id="storage-medium"></span> StorageMedium


  

| Name | Type | Go type | Default | Description | Example |
|------|------|---------| ------- |-------------|---------|
| StorageMedium | string| string | |  |  |



### <span id="storage-o-s-volume-source"></span> StorageOSVolumeSource


  



**Properties**

| Name | Type | Go type | Required | Default | Description | Example |
|------|------|---------|:--------:| ------- |-------------|---------|
| fsType | string| `string` |  | | fsType is the filesystem type to mount.</br>Must be a filesystem type supported by the host operating system.</br>Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. |  |
| readOnly | boolean| `bool` |  | | readOnly defaults to false (read/write). ReadOnly here will force</br>the ReadOnly setting in VolumeMounts. |  |
| secretRef | [LocalObjectReference](#local-object-reference)| `LocalObjectReference` |  | |  |  |
| volumeName | string| `string` |  | | volumeName is the human-readable name of the StorageOS volume.  Volume</br>names are only unique within a namespace. |  |
| volumeNamespace | string| `string` |  | | volumeNamespace specifies the scope of the volume within StorageOS.  If no</br>namespace is specified then the Pod's namespace will be used.  This allows the</br>Kubernetes name scoping to be mirrored within StorageOS for tighter integration.</br>Set VolumeName to any name to override the default behaviour.</br>Set to "default" if you are not using namespaces within StorageOS.</br>Namespaces that do not pre-exist within StorageOS will be created. |  |



### <span id="supplemental-groups-policy"></span> SupplementalGroupsPolicy


> SupplementalGroupsPolicy defines how supplemental groups
of the first container processes are calculated.
  



| Name | Type | Go type | Default | Description | Example |
|------|------|---------| ------- |-------------|---------|
| SupplementalGroupsPolicy | string| string | | SupplementalGroupsPolicy defines how supplemental groups</br>of the first container processes are calculated. |  |



### <span id="supplied-value-from"></span> SuppliedValueFrom


  

[any](#any)

### <span id="suspend-template"></span> SuspendTemplate


> SuspendTemplate is a template subtype to suspend a workflow at a predetermined point in time
  





**Properties**

| Name | Type | Go type | Required | Default | Description | Example |
|------|------|---------|:--------:| ------- |-------------|---------|
| duration | string| `string` |  | | Duration is the seconds to wait before automatically resuming a template. Must be a string. Default unit is seconds.</br>Could also be a Duration, e.g.: "2m", "6h" |  |



### <span id="synchronization"></span> Synchronization


> Synchronization holds synchronization lock configuration
  





**Properties**

| Name | Type | Go type | Required | Default | Description | Example |
|------|------|---------|:--------:| ------- |-------------|---------|
| mutex | [Mutex](#mutex)| `Mutex` |  | |  |  |
| mutexes | [][Mutex](#mutex)| `[]*Mutex` |  | | v3.6 and after: Mutexes holds the list of Mutex lock details |  |
| semaphore | [SemaphoreRef](#semaphore-ref)| `SemaphoreRef` |  | |  |  |
| semaphores | [][SemaphoreRef](#semaphore-ref)| `[]*SemaphoreRef` |  | | v3.6 and after: Semaphores holds the list of Semaphores configuration |  |



### <span id="sysctl"></span> Sysctl


> Sysctl defines a kernel parameter to be set
  





**Properties**

| Name | Type | Go type | Required | Default | Description | Example |
|------|------|---------|:--------:| ------- |-------------|---------|
| name | string| `string` |  | | Name of a property to set |  |
| value | string| `string` |  | | Value of a property to set |  |



### <span id="tcp-socket-action"></span> TCPSocketAction


> TCPSocketAction describes an action based on opening a socket
  





**Properties**

| Name | Type | Go type | Required | Default | Description | Example |
|------|------|---------|:--------:| ------- |-------------|---------|
| host | string| `string` |  | | Optional: Host name to connect to, defaults to the pod IP. |  |
| port | [IntOrString](#int-or-string)| `IntOrString` |  | |  |  |



### <span id="taint-effect"></span> TaintEffect


  

| Name | Type | Go type | Default | Description | Example |
|------|------|---------| ------- |-------------|---------|
| TaintEffect | string| string | |  |  |



### <span id="tar-strategy"></span> TarStrategy


> TarStrategy will tar and gzip the file or directory when saving
  





**Properties**

| Name | Type | Go type | Required | Default | Description | Example |
|------|------|---------|:--------:| ------- |-------------|---------|
| compressionLevel | int32 (formatted integer)| `int32` |  | | CompressionLevel specifies the gzip compression level to use for the artifact.</br>Defaults to gzip.DefaultCompression. |  |



### <span id="template"></span> Template


> Template is a reusable and composable unit of execution in a workflow
  





**Properties**

| Name | Type | Go type | Required | Default | Description | Example |
|------|------|---------|:--------:| ------- |-------------|---------|
| activeDeadlineSeconds | [IntOrString](#int-or-string)| `IntOrString` |  | |  |  |
| affinity | [Affinity](#affinity)| `Affinity` |  | |  |  |
| archiveLocation | [ArtifactLocation](#artifact-location)| `ArtifactLocation` |  | |  |  |
| automountServiceAccountToken | boolean| `bool` |  | | AutomountServiceAccountToken indicates whether a service account token should be automatically mounted in pods.</br>ServiceAccountName of ExecutorConfig must be specified if this value is false. |  |
| container | [Container](#container)| `Container` |  | |  |  |
| containerSet | [ContainerSetTemplate](#container-set-template)| `ContainerSetTemplate` |  | |  |  |
| daemon | boolean| `bool` |  | | Daemon will allow a workflow to proceed to the next step so long as the container reaches readiness |  |
| dag | [DAGTemplate](#d-a-g-template)| `DAGTemplate` |  | |  |  |
| data | [Data](#data)| `Data` |  | |  |  |
| executor | [ExecutorConfig](#executor-config)| `ExecutorConfig` |  | |  |  |
| failFast | boolean| `bool` |  | | FailFast, if specified, will fail this template if any of its child pods has failed. This is useful for when this</br>template is expanded with `withItems`, etc. |  |
| hostAliases | [][HostAlias](#host-alias)| `[]*HostAlias` |  | | HostAliases is an optional list of hosts and IPs that will be injected into the pod spec |  |
| http | [HTTP](#http)| `HTTP` |  | |  |  |
| initContainers | [][UserContainer](#user-container)| `[]*UserContainer` |  | | InitContainers is a list of containers which run before the main container. |  |
| inputs | [Inputs](#inputs)| `Inputs` |  | |  |  |
| memoize | [Memoize](#memoize)| `Memoize` |  | |  |  |
| metadata | [Metadata](#metadata)| `Metadata` |  | |  |  |
| metrics | [Metrics](#metrics)| `Metrics` |  | |  |  |
| name | string| `string` |  | | Name is the name of the template |  |
| nodeSelector | map of string| `map[string]string` |  | | NodeSelector is a selector to schedule this step of the workflow to be</br>run on the selected node(s). Overrides the selector set at the workflow level. |  |
| outputs | [Outputs](#outputs)| `Outputs` |  | |  |  |
| parallelism | int64 (formatted integer)| `int64` |  | | Parallelism limits the max total parallel pods that can execute at the same time within the</br>boundaries of this template invocation. If additional steps/dag templates are invoked, the</br>pods created by those templates will not be counted towards this total. |  |
| plugin | [Plugin](#plugin)| `Plugin` |  | |  |  |
| podSpecPatch | string| `string` |  | | PodSpecPatch holds strategic merge patch to apply against the pod spec. Allows parameterization of</br>container fields which are not strings (e.g. resource limits). |  |
| priority | int32 (formatted integer)| `int32` |  | | Priority to apply to workflow pods. |  |
| priorityClassName | string| `string` |  | | PriorityClassName to apply to workflow pods. |  |
| resource | [ResourceTemplate](#resource-template)| `ResourceTemplate` |  | |  |  |
| retryStrategy | [RetryStrategy](#retry-strategy)| `RetryStrategy` |  | |  |  |
| schedulerName | string| `string` |  | | If specified, the pod will be dispatched by specified scheduler.</br>Or it will be dispatched by workflow scope scheduler if specified.</br>If neither specified, the pod will be dispatched by default scheduler. |  |
| script | [ScriptTemplate](#script-template)| `ScriptTemplate` |  | |  |  |
| securityContext | [PodSecurityContext](#pod-security-context)| `PodSecurityContext` |  | |  |  |
| serviceAccountName | string| `string` |  | | ServiceAccountName to apply to workflow pods |  |
| sidecars | [][UserContainer](#user-container)| `[]*UserContainer` |  | | Sidecars is a list of containers which run alongside the main container</br>Sidecars are automatically killed when the main container completes |  |
| steps | [][ParallelSteps](#parallel-steps)| `[]ParallelSteps` |  | | Steps define a series of sequential/parallel workflow steps |  |
| suspend | [SuspendTemplate](#suspend-template)| `SuspendTemplate` |  | |  |  |
| synchronization | [Synchronization](#synchronization)| `Synchronization` |  | |  |  |
| timeout | string| `string` |  | | Timeout allows to set the total node execution timeout duration counting from the node's start time.</br>This duration also includes time in which the node spends in Pending state. This duration may not be applied to Step or DAG templates. |  |
| tolerations | [][Toleration](#toleration)| `[]*Toleration` |  | | Tolerations to apply to workflow pods. |  |
| volumes | [][Volume](#volume)| `[]*Volume` |  | | Volumes is a list of volumes that can be mounted by containers in a template. |  |



### <span id="template-ref"></span> TemplateRef


  



**Properties**

| Name | Type | Go type | Required | Default | Description | Example |
|------|------|---------|:--------:| ------- |-------------|---------|
| clusterScope | boolean| `bool` |  | | ClusterScope indicates the referred template is cluster scoped (i.e. a ClusterWorkflowTemplate). |  |
| name | string| `string` |  | | Name is the resource name of the template. |  |
| template | string| `string` |  | | Template is the name of referred template in the resource. |  |



### <span id="termination-message-policy"></span> TerminationMessagePolicy


  

| Name | Type | Go type | Default | Description | Example |
|------|------|---------| ------- |-------------|---------|
| TerminationMessagePolicy | string| string | |  |  |



### <span id="toleration"></span> Toleration


> The pod this Toleration is attached to tolerates any taint that matches
the triple <key,value,effect> using the matching operator <operator>.
  





**Properties**

| Name | Type | Go type | Required | Default | Description | Example |
|------|------|---------|:--------:| ------- |-------------|---------|
| effect | [TaintEffect](#taint-effect)| `TaintEffect` |  | |  |  |
| key | string| `string` |  | | Key is the taint key that the toleration applies to. Empty means match all taint keys.</br>If the key is empty, operator must be Exists; this combination means to match all values and all keys. |  |
| operator | [TolerationOperator](#toleration-operator)| `TolerationOperator` |  | |  |  |
| tolerationSeconds | int64 (formatted integer)| `int64` |  | | TolerationSeconds represents the period of time the toleration (which must be</br>of effect NoExecute, otherwise this field is ignored) tolerates the taint. By default,</br>it is not set, which means tolerate the taint forever (do not evict). Zero and</br>negative values will be treated as 0 (evict immediately) by the system. |  |
| value | string| `string` |  | | Value is the taint value the toleration matches to.</br>If the operator is Exists, the value should be empty, otherwise just a regular string. |  |



### <span id="toleration-operator"></span> TolerationOperator


  

| Name | Type | Go type | Default | Description | Example |
|------|------|---------| ------- |-------------|---------|
| TolerationOperator | string| string | |  |  |



### <span id="transformation"></span> Transformation


  

[][TransformationStep](#transformation-step)

### <span id="transformation-step"></span> TransformationStep


  



**Properties**

| Name | Type | Go type | Required | Default | Description | Example |
|------|------|---------|:--------:| ------- |-------------|---------|
| expression | string| `string` |  | | Expression defines an expr expression to apply |  |



### <span id="type"></span> Type


  

| Name | Type | Go type | Default | Description | Example |
|------|------|---------| ------- |-------------|---------|
| Type | int64 (formatted integer)| int64 | |  |  |



### <span id="typed-local-object-reference"></span> TypedLocalObjectReference


> TypedLocalObjectReference contains enough information to let you locate the
typed referenced object inside the same namespace.
  





**Properties**

| Name | Type | Go type | Required | Default | Description | Example |
|------|------|---------|:--------:| ------- |-------------|---------|
| apiGroup | string| `string` |  | | APIGroup is the group for the resource being referenced.</br>If APIGroup is not specified, the specified Kind must be in the core API group.</br>For any other third-party types, APIGroup is required. |  |
| kind | string| `string` |  | | Kind is the type of resource being referenced |  |
| name | string| `string` |  | | Name is the name of resource being referenced |  |



### <span id="typed-object-reference"></span> TypedObjectReference


> TypedObjectReference contains enough information to let you locate the typed referenced object
  





**Properties**

| Name | Type | Go type | Required | Default | Description | Example |
|------|------|---------|:--------:| ------- |-------------|---------|
| apiGroup | string| `string` |  | | APIGroup is the group for the resource being referenced.</br>If APIGroup is not specified, the specified Kind must be in the core API group.</br>For any other third-party types, APIGroup is required. |  |
| kind | string| `string` |  | | Kind is the type of resource being referenced |  |
| name | string| `string` |  | | Name is the name of resource being referenced |  |
| namespace | string| `string` |  | | Namespace is the namespace of resource being referenced</br>Note that when a namespace is specified, a gateway.networking.k8s.io/ReferenceGrant object is required in the referent namespace to allow that namespace's owner to accept the reference. See the ReferenceGrant documentation for details.</br>(Alpha) This field requires the CrossNamespaceVolumeDataSource feature gate to be enabled. |  |



### <span id="uid"></span> UID


> UID is a type that holds unique ID values, including UUIDs.  Because we
don't ONLY use UUIDs, this is an alias to string.  Being a type captures
intent and helps make sure that UIDs and names do not get conflated.
  



| Name | Type | Go type | Default | Description | Example |
|------|------|---------| ------- |-------------|---------|
| UID | string| string | | UID is a type that holds unique ID values, including UUIDs.  Because we</br>don't ONLY use UUIDs, this is an alias to string.  Being a type captures</br>intent and helps make sure that UIDs and names do not get conflated. |  |



### <span id="uri-scheme"></span> URIScheme


> URIScheme identifies the scheme used for connection to a host for Get actions
  



| Name | Type | Go type | Default | Description | Example |
|------|------|---------| ------- |-------------|---------|
| URIScheme | string| string | | URIScheme identifies the scheme used for connection to a host for Get actions |  |



### <span id="user-container"></span> UserContainer


  



**Properties**

| Name | Type | Go type | Required | Default | Description | Example |
|------|------|---------|:--------:| ------- |-------------|---------|
| args | []string| `[]string` |  | | Arguments to the entrypoint.</br>The container image's CMD is used if this is not provided.</br>Variable references $(VAR_NAME) are expanded using the container's environment. If a variable</br>cannot be resolved, the reference in the input string will be unchanged. Double $$ are reduced</br>to a single $, which allows for escaping the $(VAR_NAME) syntax: i.e. "$$(VAR_NAME)" will</br>produce the string literal "$(VAR_NAME)". Escaped references will never be expanded, regardless</br>of whether the variable exists or not. Cannot be updated.</br>More info: https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell |  |
| command | []string| `[]string` |  | | Entrypoint array. Not executed within a shell.</br>The container image's ENTRYPOINT is used if this is not provided.</br>Variable references $(VAR_NAME) are expanded using the container's environment. If a variable</br>cannot be resolved, the reference in the input string will be unchanged. Double $$ are reduced</br>to a single $, which allows for escaping the $(VAR_NAME) syntax: i.e. "$$(VAR_NAME)" will</br>produce the string literal "$(VAR_NAME)". Escaped references will never be expanded, regardless</br>of whether the variable exists or not. Cannot be updated.</br>More info: https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell |  |
| env | [][EnvVar](#env-var)| `[]*EnvVar` |  | | List of environment variables to set in the container.</br>Cannot be updated. |  |
| envFrom | [][EnvFromSource](#env-from-source)| `[]*EnvFromSource` |  | | List of sources to populate environment variables in the container.</br>The keys defined within a source must be a C_IDENTIFIER. All invalid keys</br>will be reported as an event when the container is starting. When a key exists in multiple</br>sources, the value associated with the last source will take precedence.</br>Values defined by an Env with a duplicate key will take precedence.</br>Cannot be updated. |  |
| image | string| `string` |  | | Container image name.</br>More info: https://kubernetes.io/docs/concepts/containers/images</br>This field is optional to allow higher level config management to default or override</br>container images in workload controllers like Deployments and StatefulSets. |  |
| imagePullPolicy | [PullPolicy](#pull-policy)| `PullPolicy` |  | |  |  |
| lifecycle | [Lifecycle](#lifecycle)| `Lifecycle` |  | |  |  |
| livenessProbe | [Probe](#probe)| `Probe` |  | |  |  |
| mirrorVolumeMounts | boolean| `bool` |  | | MirrorVolumeMounts will mount the same volumes specified in the main container</br>to the container (including artifacts), at the same mountPaths. This enables</br>dind daemon to partially see the same filesystem as the main container in</br>order to use features such as docker volume binding |  |
| name | string| `string` |  | | Name of the container specified as a DNS_LABEL.</br>Each container in a pod must have a unique name (DNS_LABEL).</br>Cannot be updated. |  |
| ports | [][ContainerPort](#container-port)| `[]*ContainerPort` |  | | List of ports to expose from the container. Not specifying a port here</br>DOES NOT prevent that port from being exposed. Any port which is</br>listening on the default "0.0.0.0" address inside a container will be</br>accessible from the network.</br>Modifying this array with strategic merge patch may corrupt the data.</br>For more information See https://github.com/kubernetes/kubernetes/issues/108255.</br>Cannot be updated. |  |
| readinessProbe | [Probe](#probe)| `Probe` |  | |  |  |
| resizePolicy | [][ContainerResizePolicy](#container-resize-policy)| `[]*ContainerResizePolicy` |  | | Resources resize policy for the container. |  |
| resources | [ResourceRequirements](#resource-requirements)| `ResourceRequirements` |  | |  |  |
| restartPolicy | [ContainerRestartPolicy](#container-restart-policy)| `ContainerRestartPolicy` |  | |  |  |
| securityContext | [SecurityContext](#security-context)| `SecurityContext` |  | |  |  |
| startupProbe | [Probe](#probe)| `Probe` |  | |  |  |
| stdin | boolean| `bool` |  | | Whether this container should allocate a buffer for stdin in the container runtime. If this</br>is not set, reads from stdin in the container will always result in EOF.</br>Default is false. |  |
| stdinOnce | boolean| `bool` |  | | Whether the container runtime should close the stdin channel after it has been opened by</br>a single attach. When stdin is true the stdin stream will remain open across multiple attach</br>sessions. If stdinOnce is set to true, stdin is opened on container start, is empty until the</br>first client attaches to stdin, and then remains open and accepts data until the client disconnects,</br>at which time stdin is closed and remains closed until the container is restarted. If this</br>flag is false, a container processes that reads from stdin will never receive an EOF.</br>Default is false |  |
| terminationMessagePath | string| `string` |  | | Optional: Path at which the file to which the container's termination message</br>will be written is mounted into the container's filesystem.</br>Message written is intended to be brief final status, such as an assertion failure message.</br>Will be truncated by the node if greater than 4096 bytes. The total message length across</br>all containers will be limited to 12kb.</br>Defaults to /dev/termination-log.</br>Cannot be updated. |  |
| terminationMessagePolicy | [TerminationMessagePolicy](#termination-message-policy)| `TerminationMessagePolicy` |  | |  |  |
| tty | boolean| `bool` |  | | Whether this container should allocate a TTY for itself, also requires 'stdin' to be true.</br>Default is false. |  |
| volumeDevices | [][VolumeDevice](#volume-device)| `[]*VolumeDevice` |  | | volumeDevices is the list of block devices to be used by the container. |  |
| volumeMounts | [][VolumeMount](#volume-mount)| `[]*VolumeMount` |  | | Pod volumes to mount into the container's filesystem.</br>Cannot be updated. |  |
| workingDir | string| `string` |  | | Container's working directory.</br>If not specified, the container runtime's default will be used, which</br>might be configured in the container image.</br>Cannot be updated. |  |



### <span id="v1-http-header"></span> V1HTTPHeader


> HTTPHeader describes a custom header to be used in HTTP probes
  





**Properties**

| Name | Type | Go type | Required | Default | Description | Example |
|------|------|---------|:--------:| ------- |-------------|---------|
| name | string| `string` |  | | The header field name.</br>This will be canonicalized upon output, so case-variant names will be understood as the same header. |  |
| value | string| `string` |  | | The header field value |  |



### <span id="v1-object-meta"></span> V1ObjectMeta


> ObjectMeta is metadata that all persisted resources must have, which includes all objects
users must create.
  





**Properties**

| Name | Type | Go type | Required | Default | Description | Example |
|------|------|---------|:--------:| ------- |-------------|---------|
| annotations | map of string| `map[string]string` |  | | Annotations is an unstructured key value map stored with a resource that may be</br>set by external tools to store and retrieve arbitrary metadata. They are not</br>queryable and should be preserved when modifying objects.</br>More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations |  |
| creationTimestamp | string| `string` |  | | CreationTimestamp is a timestamp representing the server time when this object was</br>created. It is not guaranteed to be set in happens-before order across separate operations.</br>Clients may not set this value. It is represented in RFC3339 form and is in UTC.</br></br>Populated by the system.</br>Read-only.</br>Null for lists.</br>More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata |  |
| deletionGracePeriodSeconds | int64 (formatted integer)| `int64` |  | | Number of seconds allowed for this object to gracefully terminate before</br>it will be removed from the system. Only set when deletionTimestamp is also set.</br>May only be shortened.</br>Read-only. |  |
| deletionTimestamp | string| `string` |  | | DeletionTimestamp is RFC 3339 date and time at which this resource will be deleted. This</br>field is set by the server when a graceful deletion is requested by the user, and is not</br>directly settable by a client. The resource is expected to be deleted (no longer visible</br>from resource lists, and not reachable by name) after the time in this field, once the</br>finalizers list is empty. As long as the finalizers list contains items, deletion is blocked.</br>Once the deletionTimestamp is set, this value may not be unset or be set further into the</br>future, although it may be shortened or the resource may be deleted prior to this time.</br>For example, a user may request that a pod is deleted in 30 seconds. The Kubelet will react</br>by sending a graceful termination signal to the containers in the pod. After that 30 seconds,</br>the Kubelet will send a hard termination signal (SIGKILL) to the container and after cleanup,</br>remove the pod from the API. In the presence of network partitions, this object may still</br>exist after this timestamp, until an administrator or automated process can determine the</br>resource is fully terminated.</br>If not set, graceful deletion of the object has not been requested.</br></br>Populated by the system when a graceful deletion is requested.</br>Read-only.</br>More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata |  |
| finalizers | []string| `[]string` |  | | Must be empty before the object is deleted from the registry. Each entry</br>is an identifier for the responsible component that will remove the entry</br>from the list. If the deletionTimestamp of the object is non-nil, entries</br>in this list can only be removed.</br>Finalizers may be processed and removed in any order.  Order is NOT enforced</br>because it introduces significant risk of stuck finalizers.</br>finalizers is a shared field, any actor with permission can reorder it.</br>If the finalizer list is processed in order, then this can lead to a situation</br>in which the component responsible for the first finalizer in the list is</br>waiting for a signal (field value, external system, or other) produced by a</br>component responsible for a finalizer later in the list, resulting in a deadlock.</br>Without enforced ordering finalizers are free to order amongst themselves and</br>are not vulnerable to ordering changes in the list. |  |
| generateName | string| `string` |  | | GenerateName is an optional prefix, used by the server, to generate a unique</br>name ONLY IF the Name field has not been provided.</br>If this field is used, the name returned to the client will be different</br>than the name passed. This value will also be combined with a unique suffix.</br>The provided value has the same validation rules as the Name field,</br>and may be truncated by the length of the suffix required to make the value</br>unique on the server.</br></br>If this field is specified and the generated name exists, the server will return a 409.</br></br>Applied only if Name is not specified.</br>More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#idempotency |  |
| generation | int64 (formatted integer)| `int64` |  | | A sequence number representing a specific generation of the desired state.</br>Populated by the system. Read-only. |  |
| labels | map of string| `map[string]string` |  | | Map of string keys and values that can be used to organize and categorize</br>(scope and select) objects. May match selectors of replication controllers</br>and services.</br>More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/labels |  |
| managedFields | [][ManagedFieldsEntry](#managed-fields-entry)| `[]*ManagedFieldsEntry` |  | | ManagedFields maps workflow-id and version to the set of fields</br>that are managed by that workflow. This is mostly for internal</br>housekeeping, and users typically shouldn't need to set or</br>understand this field. A workflow can be the user's name, a</br>controller's name, or the name of a specific apply path like</br>"ci-cd". The set of fields is always in the version that the</br>workflow used when modifying the object. |  |
| name | string| `string` |  | | Name must be unique within a namespace. Is required when creating resources, although</br>some resources may allow a client to request the generation of an appropriate name</br>automatically. Name is primarily intended for creation idempotence and configuration</br>definition.</br>Cannot be updated.</br>More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names#names |  |
| namespace | string| `string` |  | | Namespace defines the space within which each name must be unique. An empty namespace is</br>equivalent to the "default" namespace, but "default" is the canonical representation.</br>Not all objects are required to be scoped to a namespace - the value of this field for</br>those objects will be empty.</br></br>Must be a DNS_LABEL.</br>Cannot be updated.</br>More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces |  |
| ownerReferences | [][OwnerReference](#owner-reference)| `[]*OwnerReference` |  | | List of objects depended by this object. If ALL objects in the list have</br>been deleted, this object will be garbage collected. If this object is managed by a controller,</br>then an entry in this list will point to this controller, with the controller field set to true.</br>There cannot be more than one managing controller. |  |
| resourceVersion | string| `string` |  | | An opaque value that represents the internal version of this object that can</br>be used by clients to determine when objects have changed. May be used for optimistic</br>concurrency, change detection, and the watch operation on a resource or set of resources.</br>Clients must treat these values as opaque and passed unmodified back to the server.</br>They may only be valid for a particular resource or set of resources.</br></br>Populated by the system.</br>Read-only.</br>Value must be treated as opaque by clients and .</br>More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#concurrency-control-and-consistency |  |
| selfLink | string| `string` |  | | Deprecated: selfLink is a legacy read-only field that is no longer populated by the system. |  |
| uid | [UID](#uid)| `UID` |  | |  |  |



### <span id="v1alpha1-http-header"></span> V1alpha1HTTPHeader


  



**Properties**

| Name | Type | Go type | Required | Default | Description | Example |
|------|------|---------|:--------:| ------- |-------------|---------|
| name | string| `string` |  | |  |  |
| value | string| `string` |  | |  |  |
| valueFrom | [HTTPHeaderSource](#http-header-source)| `HTTPHeaderSource` |  | |  |  |



### <span id="value-from"></span> ValueFrom


> ValueFrom describes a location in which to obtain the value to a parameter
  





**Properties**

| Name | Type | Go type | Required | Default | Description | Example |
|------|------|---------|:--------:| ------- |-------------|---------|
| configMapKeyRef | [ConfigMapKeySelector](#config-map-key-selector)| `ConfigMapKeySelector` |  | |  |  |
| default | [AnyString](#any-string)| `AnyString` |  | |  |  |
| event | string| `string` |  | | Selector (https://github.com/expr-lang/expr) that is evaluated against the event to get the value of the parameter. E.g. `payload.message` |  |
| expression | string| `string` |  | | Expression, if defined, is evaluated to specify the value for the parameter |  |
| jqFilter | string| `string` |  | | JQFilter expression against the resource object in resource templates |  |
| jsonPath | string| `string` |  | | JSONPath of a resource to retrieve an output parameter value from in resource templates |  |
| parameter | string| `string` |  | | Parameter reference to a step or dag task in which to retrieve an output parameter value from</br>(e.g. '{{steps.mystep.outputs.myparam}}') |  |
| path | string| `string` |  | | Path in the container to retrieve an output parameter value from in container templates |  |
| supplied | [SuppliedValueFrom](#supplied-value-from)| `SuppliedValueFrom` |  | |  |  |



### <span id="volume"></span> Volume


  



**Properties**

| Name | Type | Go type | Required | Default | Description | Example |
|------|------|---------|:--------:| ------- |-------------|---------|
| awsElasticBlockStore | [AWSElasticBlockStoreVolumeSource](#a-w-s-elastic-block-store-volume-source)| `AWSElasticBlockStoreVolumeSource` |  | |  |  |
| azureDisk | [AzureDiskVolumeSource](#azure-disk-volume-source)| `AzureDiskVolumeSource` |  | |  |  |
| azureFile | [AzureFileVolumeSource](#azure-file-volume-source)| `AzureFileVolumeSource` |  | |  |  |
| cephfs | [CephFSVolumeSource](#ceph-f-s-volume-source)| `CephFSVolumeSource` |  | |  |  |
| cinder | [CinderVolumeSource](#cinder-volume-source)| `CinderVolumeSource` |  | |  |  |
| configMap | [ConfigMapVolumeSource](#config-map-volume-source)| `ConfigMapVolumeSource` |  | |  |  |
| csi | [CSIVolumeSource](#c-s-i-volume-source)| `CSIVolumeSource` |  | |  |  |
| downwardAPI | [DownwardAPIVolumeSource](#downward-api-volume-source)| `DownwardAPIVolumeSource` |  | |  |  |
| emptyDir | [EmptyDirVolumeSource](#empty-dir-volume-source)| `EmptyDirVolumeSource` |  | |  |  |
| ephemeral | [EphemeralVolumeSource](#ephemeral-volume-source)| `EphemeralVolumeSource` |  | |  |  |
| fc | [FCVolumeSource](#f-c-volume-source)| `FCVolumeSource` |  | |  |  |
| flexVolume | [FlexVolumeSource](#flex-volume-source)| `FlexVolumeSource` |  | |  |  |
| flocker | [FlockerVolumeSource](#flocker-volume-source)| `FlockerVolumeSource` |  | |  |  |
| gcePersistentDisk | [GCEPersistentDiskVolumeSource](#g-c-e-persistent-disk-volume-source)| `GCEPersistentDiskVolumeSource` |  | |  |  |
| gitRepo | [GitRepoVolumeSource](#git-repo-volume-source)| `GitRepoVolumeSource` |  | |  |  |
| glusterfs | [GlusterfsVolumeSource](#glusterfs-volume-source)| `GlusterfsVolumeSource` |  | |  |  |
| hostPath | [HostPathVolumeSource](#host-path-volume-source)| `HostPathVolumeSource` |  | |  |  |
| image | [ImageVolumeSource](#image-volume-source)| `ImageVolumeSource` |  | |  |  |
| iscsi | [ISCSIVolumeSource](#i-s-c-s-i-volume-source)| `ISCSIVolumeSource` |  | |  |  |
| name | string| `string` |  | | name of the volume.</br>Must be a DNS_LABEL and unique within the pod.</br>More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names |  |
| nfs | [NFSVolumeSource](#n-f-s-volume-source)| `NFSVolumeSource` |  | |  |  |
| persistentVolumeClaim | [PersistentVolumeClaimVolumeSource](#persistent-volume-claim-volume-source)| `PersistentVolumeClaimVolumeSource` |  | |  |  |
| photonPersistentDisk | [PhotonPersistentDiskVolumeSource](#photon-persistent-disk-volume-source)| `PhotonPersistentDiskVolumeSource` |  | |  |  |
| portworxVolume | [PortworxVolumeSource](#portworx-volume-source)| `PortworxVolumeSource` |  | |  |  |
| projected | [ProjectedVolumeSource](#projected-volume-source)| `ProjectedVolumeSource` |  | |  |  |
| quobyte | [QuobyteVolumeSource](#quobyte-volume-source)| `QuobyteVolumeSource` |  | |  |  |
| rbd | [RBDVolumeSource](#r-b-d-volume-source)| `RBDVolumeSource` |  | |  |  |
| scaleIO | [ScaleIOVolumeSource](#scale-i-o-volume-source)| `ScaleIOVolumeSource` |  | |  |  |
| secret | [SecretVolumeSource](#secret-volume-source)| `SecretVolumeSource` |  | |  |  |
| storageos | [StorageOSVolumeSource](#storage-o-s-volume-source)| `StorageOSVolumeSource` |  | |  |  |
| vsphereVolume | [VsphereVirtualDiskVolumeSource](#vsphere-virtual-disk-volume-source)| `VsphereVirtualDiskVolumeSource` |  | |  |  |



### <span id="volume-device"></span> VolumeDevice


  



**Properties**

| Name | Type | Go type | Required | Default | Description | Example |
|------|------|---------|:--------:| ------- |-------------|---------|
| devicePath | string| `string` |  | | devicePath is the path inside of the container that the device will be mapped to. |  |
| name | string| `string` |  | | name must match the name of a persistentVolumeClaim in the pod |  |



### <span id="volume-mount"></span> VolumeMount


  



**Properties**

| Name | Type | Go type | Required | Default | Description | Example |
|------|------|---------|:--------:| ------- |-------------|---------|
| mountPath | string| `string` |  | | Path within the container at which the volume should be mounted.  Must</br>not contain ':'. |  |
| mountPropagation | [MountPropagationMode](#mount-propagation-mode)| `MountPropagationMode` |  | |  |  |
| name | string| `string` |  | | This must match the Name of a Volume. |  |
| readOnly | boolean| `bool` |  | | Mounted read-only if true, read-write otherwise (false or unspecified).</br>Defaults to false. |  |
| recursiveReadOnly | [RecursiveReadOnlyMode](#recursive-read-only-mode)| `RecursiveReadOnlyMode` |  | |  |  |
| subPath | string| `string` |  | | Path within the volume from which the container's volume should be mounted.</br>Defaults to "" (volume's root). |  |
| subPathExpr | string| `string` |  | | Expanded path within the volume from which the container's volume should be mounted.</br>Behaves similarly to SubPath but environment variable references $(VAR_NAME) are expanded using the container's environment.</br>Defaults to "" (volume's root).</br>SubPathExpr and SubPath are mutually exclusive. |  |



### <span id="volume-projection"></span> VolumeProjection


> Exactly one of these fields must be set.
  





**Properties**

| Name | Type | Go type | Required | Default | Description | Example |
|------|------|---------|:--------:| ------- |-------------|---------|
| clusterTrustBundle | [ClusterTrustBundleProjection](#cluster-trust-bundle-projection)| `ClusterTrustBundleProjection` |  | |  |  |
| configMap | [ConfigMapProjection](#config-map-projection)| `ConfigMapProjection` |  | |  |  |
| downwardAPI | [DownwardAPIProjection](#downward-api-projection)| `DownwardAPIProjection` |  | |  |  |
| secret | [SecretProjection](#secret-projection)| `SecretProjection` |  | |  |  |
| serviceAccountToken | [ServiceAccountTokenProjection](#service-account-token-projection)| `ServiceAccountTokenProjection` |  | |  |  |



### <span id="volume-resource-requirements"></span> VolumeResourceRequirements


  



**Properties**

| Name | Type | Go type | Required | Default | Description | Example |
|------|------|---------|:--------:| ------- |-------------|---------|
| limits | [ResourceList](#resource-list)| `ResourceList` |  | |  |  |
| requests | [ResourceList](#resource-list)| `ResourceList` |  | |  |  |



### <span id="vsphere-virtual-disk-volume-source"></span> VsphereVirtualDiskVolumeSource


  



**Properties**

| Name | Type | Go type | Required | Default | Description | Example |
|------|------|---------|:--------:| ------- |-------------|---------|
| fsType | string| `string` |  | | fsType is filesystem type to mount.</br>Must be a filesystem type supported by the host operating system.</br>Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. |  |
| storagePolicyID | string| `string` |  | | storagePolicyID is the storage Policy Based Management (SPBM) profile ID associated with the StoragePolicyName. |  |
| storagePolicyName | string| `string` |  | | storagePolicyName is the storage Policy Based Management (SPBM) profile name. |  |
| volumePath | string| `string` |  | | volumePath is the path that identifies vSphere volume vmdk |  |



### <span id="weighted-pod-affinity-term"></span> WeightedPodAffinityTerm


> The weights of all of the matched WeightedPodAffinityTerm fields are added per-node to find the most preferred node(s)
  





**Properties**

| Name | Type | Go type | Required | Default | Description | Example |
|------|------|---------|:--------:| ------- |-------------|---------|
| podAffinityTerm | [PodAffinityTerm](#pod-affinity-term)| `PodAffinityTerm` |  | |  |  |
| weight | int32 (formatted integer)| `int32` |  | | weight associated with matching the corresponding podAffinityTerm,</br>in the range 1-100. |  |



### <span id="windows-security-context-options"></span> WindowsSecurityContextOptions


  



**Properties**

| Name | Type | Go type | Required | Default | Description | Example |
|------|------|---------|:--------:| ------- |-------------|---------|
| gmsaCredentialSpec | string| `string` |  | | GMSACredentialSpec is where the GMSA admission webhook</br>(https://github.com/kubernetes-sigs/windows-gmsa) inlines the contents of the</br>GMSA credential spec named by the GMSACredentialSpecName field. |  |
| gmsaCredentialSpecName | string| `string` |  | | GMSACredentialSpecName is the name of the GMSA credential spec to use. |  |
| hostProcess | boolean| `bool` |  | | HostProcess determines if a container should be run as a 'Host Process' container.</br>All of a Pod's containers must have the same effective HostProcess value</br>(it is not allowed to have a mix of HostProcess containers and non-HostProcess containers).</br>In addition, if HostProcess is true then HostNetwork must also be set to true. |  |
| runAsUserName | string| `string` |  | | The UserName in Windows to run the entrypoint of the container process.</br>Defaults to the user specified in image metadata if unspecified.</br>May also be set in PodSecurityContext. If set in both SecurityContext and</br>PodSecurityContext, the value specified in SecurityContext takes precedence. |  |



### <span id="workflow"></span> Workflow


  



**Properties**

| Name | Type | Go type | Required | Default | Description | Example |
|------|------|---------|:--------:| ------- |-------------|---------|
| metadata | [ExecutorObjectMeta](#executor-object-meta)| `ExecutorObjectMeta` | ✓ | |  |  |



### <span id="zip-strategy"></span> ZipStrategy


> ZipStrategy will unzip zipped input artifacts
  



[any](#any)
