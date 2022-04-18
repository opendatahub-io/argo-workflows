"""
    Argo Workflows API

    Argo Workflows is an open source container-native workflow engine for orchestrating parallel jobs on Kubernetes. For more information, please see https://argoproj.github.io/argo-workflows/  # noqa: E501

    The version of the OpenAPI document: VERSION
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from argo_workflows.api_client import ApiClient, Endpoint as _Endpoint
from argo_workflows.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from argo_workflows.model.grpc_gateway_runtime_error import GrpcGatewayRuntimeError


class ArtifactServiceApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __get_input_artifact(
            self,
            namespace,
            name,
            node_id,
            artifact_name,
            **kwargs
        ):
            """Get an input artifact.  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_input_artifact(namespace, name, node_id, artifact_name, async_req=True)
            >>> result = thread.get()

            Args:
                namespace (str):
                name (str):
                node_id (str):
                artifact_name (str):

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                None
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['namespace'] = \
                namespace
            kwargs['name'] = \
                name
            kwargs['node_id'] = \
                node_id
            kwargs['artifact_name'] = \
                artifact_name
            return self.call_with_http_info(**kwargs)

        self.get_input_artifact = _Endpoint(
            settings={
                'response_type': None,
                'auth': [],
                'endpoint_path': '/input-artifacts/{namespace}/{name}/{nodeId}/{artifactName}',
                'operation_id': 'get_input_artifact',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'namespace',
                    'name',
                    'node_id',
                    'artifact_name',
                ],
                'required': [
                    'namespace',
                    'name',
                    'node_id',
                    'artifact_name',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'namespace':
                        (str,),
                    'name':
                        (str,),
                    'node_id':
                        (str,),
                    'artifact_name':
                        (str,),
                },
                'attribute_map': {
                    'namespace': 'namespace',
                    'name': 'name',
                    'node_id': 'nodeId',
                    'artifact_name': 'artifactName',
                },
                'location_map': {
                    'namespace': 'path',
                    'name': 'path',
                    'node_id': 'path',
                    'artifact_name': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__get_input_artifact
        )

        def __get_input_artifact_by_uid(
            self,
            namespace,
            uid,
            node_id,
            artifact_name,
            **kwargs
        ):
            """Get an input artifact by UID.  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_input_artifact_by_uid(namespace, uid, node_id, artifact_name, async_req=True)
            >>> result = thread.get()

            Args:
                namespace (str):
                uid (str):
                node_id (str):
                artifact_name (str):

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                file_type
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['namespace'] = \
                namespace
            kwargs['uid'] = \
                uid
            kwargs['node_id'] = \
                node_id
            kwargs['artifact_name'] = \
                artifact_name
            return self.call_with_http_info(**kwargs)

        self.get_input_artifact_by_uid = _Endpoint(
            settings={
                'response_type': (file_type,),
                'auth': [],
                'endpoint_path': '/input-artifacts-by-uid/{uid}/{nodeId}/{artifactName}',
                'operation_id': 'get_input_artifact_by_uid',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'namespace',
                    'uid',
                    'node_id',
                    'artifact_name',
                ],
                'required': [
                    'namespace',
                    'uid',
                    'node_id',
                    'artifact_name',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'namespace':
                        (str,),
                    'uid':
                        (str,),
                    'node_id':
                        (str,),
                    'artifact_name':
                        (str,),
                },
                'attribute_map': {
                    'namespace': 'namespace',
                    'uid': 'uid',
                    'node_id': 'nodeId',
                    'artifact_name': 'artifactName',
                },
                'location_map': {
                    'namespace': 'path',
                    'uid': 'path',
                    'node_id': 'path',
                    'artifact_name': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__get_input_artifact_by_uid
        )

        def __get_output_artifact(
            self,
            namespace,
            name,
            node_id,
            artifact_name,
            **kwargs
        ):
            """Get an output artifact.  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_output_artifact(namespace, name, node_id, artifact_name, async_req=True)
            >>> result = thread.get()

            Args:
                namespace (str):
                name (str):
                node_id (str):
                artifact_name (str):

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                file_type
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['namespace'] = \
                namespace
            kwargs['name'] = \
                name
            kwargs['node_id'] = \
                node_id
            kwargs['artifact_name'] = \
                artifact_name
            return self.call_with_http_info(**kwargs)

        self.get_output_artifact = _Endpoint(
            settings={
                'response_type': (file_type,),
                'auth': [],
                'endpoint_path': '/artifacts/{namespace}/{name}/{nodeId}/{artifactName}',
                'operation_id': 'get_output_artifact',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'namespace',
                    'name',
                    'node_id',
                    'artifact_name',
                ],
                'required': [
                    'namespace',
                    'name',
                    'node_id',
                    'artifact_name',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'namespace':
                        (str,),
                    'name':
                        (str,),
                    'node_id':
                        (str,),
                    'artifact_name':
                        (str,),
                },
                'attribute_map': {
                    'namespace': 'namespace',
                    'name': 'name',
                    'node_id': 'nodeId',
                    'artifact_name': 'artifactName',
                },
                'location_map': {
                    'namespace': 'path',
                    'name': 'path',
                    'node_id': 'path',
                    'artifact_name': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__get_output_artifact
        )

        def __get_output_artifact_by_uid(
            self,
            uid,
            node_id,
            artifact_name,
            **kwargs
        ):
            """Get an output artifact by UID.  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_output_artifact_by_uid(uid, node_id, artifact_name, async_req=True)
            >>> result = thread.get()

            Args:
                uid (str):
                node_id (str):
                artifact_name (str):

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                None
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['uid'] = \
                uid
            kwargs['node_id'] = \
                node_id
            kwargs['artifact_name'] = \
                artifact_name
            return self.call_with_http_info(**kwargs)

        self.get_output_artifact_by_uid = _Endpoint(
            settings={
                'response_type': None,
                'auth': [],
                'endpoint_path': '/artifacts-by-uid/{uid}/{nodeId}/{artifactName}',
                'operation_id': 'get_output_artifact_by_uid',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'uid',
                    'node_id',
                    'artifact_name',
                ],
                'required': [
                    'uid',
                    'node_id',
                    'artifact_name',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'uid':
                        (str,),
                    'node_id':
                        (str,),
                    'artifact_name':
                        (str,),
                },
                'attribute_map': {
                    'uid': 'uid',
                    'node_id': 'nodeId',
                    'artifact_name': 'artifactName',
                },
                'location_map': {
                    'uid': 'path',
                    'node_id': 'path',
                    'artifact_name': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__get_output_artifact_by_uid
        )
