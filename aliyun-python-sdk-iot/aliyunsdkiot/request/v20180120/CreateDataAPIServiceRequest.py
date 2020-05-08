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
from aliyunsdkiot.endpoint import endpoint_data

class CreateDataAPIServiceRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Iot', '2018-01-20', 'CreateDataAPIService','Iot')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_RequestParams(self):
		return self.get_body_params().get('RequestParams')

	def set_RequestParams(self,RequestParams):
		for i in range(len(RequestParams)):	
			if RequestParams[i].get('Name') is not None:
				self.add_body_params('RequestParam.' + str(i + 1) + '.Name' , RequestParams[i].get('Name'))
			if RequestParams[i].get('Type') is not None:
				self.add_body_params('RequestParam.' + str(i + 1) + '.Type' , RequestParams[i].get('Type'))
			if RequestParams[i].get('Desc') is not None:
				self.add_body_params('RequestParam.' + str(i + 1) + '.Desc' , RequestParams[i].get('Desc'))
			if RequestParams[i].get('Example') is not None:
				self.add_body_params('RequestParam.' + str(i + 1) + '.Example' , RequestParams[i].get('Example'))
			if RequestParams[i].get('Required') is not None:
				self.add_body_params('RequestParam.' + str(i + 1) + '.Required' , RequestParams[i].get('Required'))


	def get_FolderId(self):
		return self.get_body_params().get('FolderId')

	def set_FolderId(self,FolderId):
		self.add_body_params('FolderId', FolderId)

	def get_IotInstanceId(self):
		return self.get_body_params().get('IotInstanceId')

	def set_IotInstanceId(self,IotInstanceId):
		self.add_body_params('IotInstanceId', IotInstanceId)

	def get_ApiPath(self):
		return self.get_body_params().get('ApiPath')

	def set_ApiPath(self,ApiPath):
		self.add_body_params('ApiPath', ApiPath)

	def get_TemplateSql(self):
		return self.get_body_params().get('TemplateSql')

	def set_TemplateSql(self,TemplateSql):
		self.add_body_params('TemplateSql', TemplateSql)

	def get_ResponseParams(self):
		return self.get_body_params().get('ResponseParams')

	def set_ResponseParams(self,ResponseParams):
		for i in range(len(ResponseParams)):	
			if ResponseParams[i].get('Name') is not None:
				self.add_body_params('ResponseParam.' + str(i + 1) + '.Name' , ResponseParams[i].get('Name'))
			if ResponseParams[i].get('Type') is not None:
				self.add_body_params('ResponseParam.' + str(i + 1) + '.Type' , ResponseParams[i].get('Type'))
			if ResponseParams[i].get('Desc') is not None:
				self.add_body_params('ResponseParam.' + str(i + 1) + '.Desc' , ResponseParams[i].get('Desc'))
			if ResponseParams[i].get('Example') is not None:
				self.add_body_params('ResponseParam.' + str(i + 1) + '.Example' , ResponseParams[i].get('Example'))
			if ResponseParams[i].get('Required') is not None:
				self.add_body_params('ResponseParam.' + str(i + 1) + '.Required' , ResponseParams[i].get('Required'))


	def get_OriginSql(self):
		return self.get_body_params().get('OriginSql')

	def set_OriginSql(self,OriginSql):
		self.add_body_params('OriginSql', OriginSql)

	def get_DisplayName(self):
		return self.get_body_params().get('DisplayName')

	def set_DisplayName(self,DisplayName):
		self.add_body_params('DisplayName', DisplayName)

	def get_Desc(self):
		return self.get_body_params().get('Desc')

	def set_Desc(self,Desc):
		self.add_body_params('Desc', Desc)