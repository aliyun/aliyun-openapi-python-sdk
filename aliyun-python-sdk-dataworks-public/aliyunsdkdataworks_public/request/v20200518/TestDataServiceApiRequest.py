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
from aliyunsdkdataworks_public.endpoint import endpoint_data

class TestDataServiceApiRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'dataworks-public', '2020-05-18', 'TestDataServiceApi')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_PathParamss(self): # RepeatList
		return self.get_body_params().get('PathParams')

	def set_PathParamss(self, PathParams):  # RepeatList
		for depth1 in range(len(PathParams)):
			if PathParams[depth1].get('ParamKey') is not None:
				self.add_body_params('PathParams.' + str(depth1 + 1) + '.ParamKey', PathParams[depth1].get('ParamKey'))
			if PathParams[depth1].get('ParamValue') is not None:
				self.add_body_params('PathParams.' + str(depth1 + 1) + '.ParamValue', PathParams[depth1].get('ParamValue'))
	def get_QueryParams(self): # RepeatList
		return self.get_body_params().get('QueryParam')

	def set_QueryParams(self, QueryParam):  # RepeatList
		for depth1 in range(len(QueryParam)):
			if QueryParam[depth1].get('ParamKey') is not None:
				self.add_body_params('QueryParam.' + str(depth1 + 1) + '.ParamKey', QueryParam[depth1].get('ParamKey'))
			if QueryParam[depth1].get('ParamValue') is not None:
				self.add_body_params('QueryParam.' + str(depth1 + 1) + '.ParamValue', QueryParam[depth1].get('ParamValue'))
	def get_HeadParamss(self): # RepeatList
		return self.get_body_params().get('HeadParams')

	def set_HeadParamss(self, HeadParams):  # RepeatList
		for depth1 in range(len(HeadParams)):
			if HeadParams[depth1].get('ParamKey') is not None:
				self.add_body_params('HeadParams.' + str(depth1 + 1) + '.ParamKey', HeadParams[depth1].get('ParamKey'))
			if HeadParams[depth1].get('ParamValue') is not None:
				self.add_body_params('HeadParams.' + str(depth1 + 1) + '.ParamValue', HeadParams[depth1].get('ParamValue'))
	def get_BodyContent(self): # String
		return self.get_body_params().get('BodyContent')

	def set_BodyContent(self, BodyContent):  # String
		self.add_body_params('BodyContent', BodyContent)
	def get_BodyParamss(self): # RepeatList
		return self.get_body_params().get('BodyParams')

	def set_BodyParamss(self, BodyParams):  # RepeatList
		for depth1 in range(len(BodyParams)):
			if BodyParams[depth1].get('ParamKey') is not None:
				self.add_body_params('BodyParams.' + str(depth1 + 1) + '.ParamKey', BodyParams[depth1].get('ParamKey'))
			if BodyParams[depth1].get('ParamValue') is not None:
				self.add_body_params('BodyParams.' + str(depth1 + 1) + '.ParamValue', BodyParams[depth1].get('ParamValue'))
	def get_ApiId(self): # Long
		return self.get_query_params().get('ApiId')

	def set_ApiId(self, ApiId):  # Long
		self.add_query_param('ApiId', ApiId)
