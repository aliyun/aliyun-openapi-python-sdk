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
from aliyunsdkmse.endpoint import endpoint_data

class UpdateNacosConfigRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'mse', '2019-05-31', 'UpdateNacosConfig','mse')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_EncryptedDataKey(self): # String
		return self.get_query_params().get('EncryptedDataKey')

	def set_EncryptedDataKey(self, EncryptedDataKey):  # String
		self.add_query_param('EncryptedDataKey', EncryptedDataKey)
	def get_Type(self): # String
		return self.get_query_params().get('Type')

	def set_Type(self, Type):  # String
		self.add_query_param('Type', Type)
	def get_Content(self): # String
		return self.get_query_params().get('Content')

	def set_Content(self, Content):  # String
		self.add_query_param('Content', Content)
	def get_AppName(self): # String
		return self.get_query_params().get('AppName')

	def set_AppName(self, AppName):  # String
		self.add_query_param('AppName', AppName)
	def get_NamespaceId(self): # String
		return self.get_query_params().get('NamespaceId')

	def set_NamespaceId(self, NamespaceId):  # String
		self.add_query_param('NamespaceId', NamespaceId)
	def get_Group(self): # String
		return self.get_query_params().get('Group')

	def set_Group(self, Group):  # String
		self.add_query_param('Group', Group)
	def get_Tags(self): # String
		return self.get_query_params().get('Tags')

	def set_Tags(self, Tags):  # String
		self.add_query_param('Tags', Tags)
	def get_BetaIps(self): # String
		return self.get_query_params().get('BetaIps')

	def set_BetaIps(self, BetaIps):  # String
		self.add_query_param('BetaIps', BetaIps)
	def get_InstanceId(self): # String
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self, InstanceId):  # String
		self.add_query_param('InstanceId', InstanceId)
	def get_DataId(self): # String
		return self.get_query_params().get('DataId')

	def set_DataId(self, DataId):  # String
		self.add_query_param('DataId', DataId)
	def get_AcceptLanguage(self): # String
		return self.get_query_params().get('AcceptLanguage')

	def set_AcceptLanguage(self, AcceptLanguage):  # String
		self.add_query_param('AcceptLanguage', AcceptLanguage)
	def get_Desc(self): # String
		return self.get_query_params().get('Desc')

	def set_Desc(self, Desc):  # String
		self.add_query_param('Desc', Desc)
	def get_Md5(self): # String
		return self.get_query_params().get('Md5')

	def set_Md5(self, Md5):  # String
		self.add_query_param('Md5', Md5)
