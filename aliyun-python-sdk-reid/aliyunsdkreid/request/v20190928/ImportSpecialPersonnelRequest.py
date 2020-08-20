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
from aliyunsdkreid.endpoint import endpoint_data

class ImportSpecialPersonnelRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'reid', '2019-09-28', 'ImportSpecialPersonnel','1.1.8.3')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_UkId(self):
		return self.get_body_params().get('UkId')

	def set_UkId(self,UkId):
		self.add_body_params('UkId', UkId)

	def get_Description(self):
		return self.get_body_params().get('Description')

	def set_Description(self,Description):
		self.add_body_params('Description', Description)

	def get_ExternalId(self):
		return self.get_body_params().get('ExternalId')

	def set_ExternalId(self,ExternalId):
		self.add_body_params('ExternalId', ExternalId)

	def get_PersonType(self):
		return self.get_body_params().get('PersonType')

	def set_PersonType(self,PersonType):
		self.add_body_params('PersonType', PersonType)

	def get_Urls(self):
		return self.get_body_params().get('Urls')

	def set_Urls(self,Urls):
		self.add_body_params('Urls', Urls)

	def get_PersonName(self):
		return self.get_body_params().get('PersonName')

	def set_PersonName(self,PersonName):
		self.add_body_params('PersonName', PersonName)

	def get_StoreIds(self):
		return self.get_body_params().get('StoreIds')

	def set_StoreIds(self,StoreIds):
		self.add_body_params('StoreIds', StoreIds)

	def get_Status(self):
		return self.get_body_params().get('Status')

	def set_Status(self,Status):
		self.add_body_params('Status', Status)