# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
from aliyunsdkcloudapi.endpoint import endpoint_data

class ModifyApiConfigurationRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'CloudAPI', '2016-07-14', 'ModifyApiConfiguration','apigateway')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ContentTypeCategory(self): # String
		return self.get_query_params().get('ContentTypeCategory')

	def set_ContentTypeCategory(self, ContentTypeCategory):  # String
		self.add_query_param('ContentTypeCategory', ContentTypeCategory)
	def get_ModelName(self): # String
		return self.get_query_params().get('ModelName')

	def set_ModelName(self, ModelName):  # String
		self.add_query_param('ModelName', ModelName)
	def get_ErrorCodeSamples(self): # String
		return self.get_query_params().get('ErrorCodeSamples')

	def set_ErrorCodeSamples(self, ErrorCodeSamples):  # String
		self.add_query_param('ErrorCodeSamples', ErrorCodeSamples)
	def get_AppCodeAuthType(self): # String
		return self.get_query_params().get('AppCodeAuthType')

	def set_AppCodeAuthType(self, AppCodeAuthType):  # String
		self.add_query_param('AppCodeAuthType', AppCodeAuthType)
	def get_AuthType(self): # String
		return self.get_query_params().get('AuthType')

	def set_AuthType(self, AuthType):  # String
		self.add_query_param('AuthType', AuthType)
	def get_HttpConfig(self): # String
		return self.get_query_params().get('HttpConfig')

	def set_HttpConfig(self, HttpConfig):  # String
		self.add_query_param('HttpConfig', HttpConfig)
	def get_ServiceParameters(self): # String
		return self.get_query_params().get('ServiceParameters')

	def set_ServiceParameters(self, ServiceParameters):  # String
		self.add_query_param('ServiceParameters', ServiceParameters)
	def get_FailResultSample(self): # String
		return self.get_query_params().get('FailResultSample')

	def set_FailResultSample(self, FailResultSample):  # String
		self.add_query_param('FailResultSample', FailResultSample)
	def get_ContentTypeValue(self): # String
		return self.get_query_params().get('ContentTypeValue')

	def set_ContentTypeValue(self, ContentTypeValue):  # String
		self.add_query_param('ContentTypeValue', ContentTypeValue)
	def get_SecurityToken(self): # String
		return self.get_query_params().get('SecurityToken')

	def set_SecurityToken(self, SecurityToken):  # String
		self.add_query_param('SecurityToken', SecurityToken)
	def get_Visibility(self): # String
		return self.get_query_params().get('Visibility')

	def set_Visibility(self, Visibility):  # String
		self.add_query_param('Visibility', Visibility)
	def get_RequestProtocol(self): # String
		return self.get_query_params().get('RequestProtocol')

	def set_RequestProtocol(self, RequestProtocol):  # String
		self.add_query_param('RequestProtocol', RequestProtocol)
	def get_RequestMode(self): # String
		return self.get_query_params().get('RequestMode')

	def set_RequestMode(self, RequestMode):  # String
		self.add_query_param('RequestMode', RequestMode)
	def get_BackendName(self): # String
		return self.get_query_params().get('BackendName')

	def set_BackendName(self, BackendName):  # String
		self.add_query_param('BackendName', BackendName)
	def get_RequestPath(self): # String
		return self.get_query_params().get('RequestPath')

	def set_RequestPath(self, RequestPath):  # String
		self.add_query_param('RequestPath', RequestPath)
	def get_ResultType(self): # String
		return self.get_query_params().get('ResultType')

	def set_ResultType(self, ResultType):  # String
		self.add_query_param('ResultType', ResultType)
	def get_MockConfig(self): # String
		return self.get_query_params().get('MockConfig')

	def set_MockConfig(self, MockConfig):  # String
		self.add_query_param('MockConfig', MockConfig)
	def get_ResultSample(self): # String
		return self.get_query_params().get('ResultSample')

	def set_ResultSample(self, ResultSample):  # String
		self.add_query_param('ResultSample', ResultSample)
	def get_BodyModel(self): # String
		return self.get_query_params().get('BodyModel')

	def set_BodyModel(self, BodyModel):  # String
		self.add_query_param('BodyModel', BodyModel)
	def get_VpcConfig(self): # String
		return self.get_query_params().get('VpcConfig')

	def set_VpcConfig(self, VpcConfig):  # String
		self.add_query_param('VpcConfig', VpcConfig)
	def get_FunctionComputeConfig(self): # String
		return self.get_query_params().get('FunctionComputeConfig')

	def set_FunctionComputeConfig(self, FunctionComputeConfig):  # String
		self.add_query_param('FunctionComputeConfig', FunctionComputeConfig)
	def get_ApiId(self): # String
		return self.get_query_params().get('ApiId')

	def set_ApiId(self, ApiId):  # String
		self.add_query_param('ApiId', ApiId)
	def get_UseBackendService(self): # Boolean
		return self.get_query_params().get('UseBackendService')

	def set_UseBackendService(self, UseBackendService):  # Boolean
		self.add_query_param('UseBackendService', UseBackendService)
	def get_ServiceProtocol(self): # String
		return self.get_query_params().get('ServiceProtocol')

	def set_ServiceProtocol(self, ServiceProtocol):  # String
		self.add_query_param('ServiceProtocol', ServiceProtocol)
	def get_Description(self): # String
		return self.get_query_params().get('Description')

	def set_Description(self, Description):  # String
		self.add_query_param('Description', Description)
	def get_DisableInternet(self): # Boolean
		return self.get_query_params().get('DisableInternet')

	def set_DisableInternet(self, DisableInternet):  # Boolean
		self.add_query_param('DisableInternet', DisableInternet)
	def get_PostBodyDescription(self): # String
		return self.get_query_params().get('PostBodyDescription')

	def set_PostBodyDescription(self, PostBodyDescription):  # String
		self.add_query_param('PostBodyDescription', PostBodyDescription)
	def get_AllowSignatureMethod(self): # String
		return self.get_query_params().get('AllowSignatureMethod')

	def set_AllowSignatureMethod(self, AllowSignatureMethod):  # String
		self.add_query_param('AllowSignatureMethod', AllowSignatureMethod)
	def get_RequestHttpMethod(self): # String
		return self.get_query_params().get('RequestHttpMethod')

	def set_RequestHttpMethod(self, RequestHttpMethod):  # String
		self.add_query_param('RequestHttpMethod', RequestHttpMethod)
	def get_ServiceParametersMap(self): # String
		return self.get_query_params().get('ServiceParametersMap')

	def set_ServiceParametersMap(self, ServiceParametersMap):  # String
		self.add_query_param('ServiceParametersMap', ServiceParametersMap)
	def get_RequestParameters(self): # String
		return self.get_query_params().get('RequestParameters')

	def set_RequestParameters(self, RequestParameters):  # String
		self.add_query_param('RequestParameters', RequestParameters)
	def get_BodyFormat(self): # String
		return self.get_query_params().get('BodyFormat')

	def set_BodyFormat(self, BodyFormat):  # String
		self.add_query_param('BodyFormat', BodyFormat)
	def get_OssConfig(self): # String
		return self.get_query_params().get('OssConfig')

	def set_OssConfig(self, OssConfig):  # String
		self.add_query_param('OssConfig', OssConfig)
	def get_ApiName(self): # String
		return self.get_query_params().get('ApiName')

	def set_ApiName(self, ApiName):  # String
		self.add_query_param('ApiName', ApiName)
	def get_ServiceTimeout(self): # Integer
		return self.get_query_params().get('ServiceTimeout')

	def set_ServiceTimeout(self, ServiceTimeout):  # Integer
		self.add_query_param('ServiceTimeout', ServiceTimeout)
	def get_ForceNonceCheck(self): # Boolean
		return self.get_query_params().get('ForceNonceCheck')

	def set_ForceNonceCheck(self, ForceNonceCheck):  # Boolean
		self.add_query_param('ForceNonceCheck', ForceNonceCheck)
