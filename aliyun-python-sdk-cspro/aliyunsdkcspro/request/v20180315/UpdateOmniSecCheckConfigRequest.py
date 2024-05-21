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
from aliyunsdkcspro.endpoint import endpoint_data

class UpdateOmniSecCheckConfigRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'cspro', '2018-03-15', 'UpdateOmniSecCheckConfig','cspro')
		self.set_protocol_type('https')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ConfId(self):
		return self.get_body_params().get('ConfId')

	def set_ConfId(self,ConfId):
		self.add_body_params('ConfId', ConfId)

	def get_Valid(self):
		return self.get_body_params().get('Valid')

	def set_Valid(self,Valid):
		self.add_body_params('Valid', Valid)

	def get_Accessible(self):
		return self.get_body_params().get('Accessible')

	def set_Accessible(self,Accessible):
		self.add_body_params('Accessible', Accessible)

	def get_Name(self):
		return self.get_body_params().get('Name')

	def set_Name(self,Name):
		self.add_body_params('Name', Name)

	def get_CheckDetailDTOs(self):
		return self.get_body_params().get('CheckDetailDTOs')

	def set_CheckDetailDTOs(self,CheckDetailDTOs):
		for i in range(len(CheckDetailDTOs)):	
			if CheckDetailDTOs[i].get('CheckType') is not None:
				self.add_body_params('CheckDetailDTO.' + str(i + 1) + '.CheckType' , CheckDetailDTOs[i].get('CheckType'))
			if CheckDetailDTOs[i].get('CheckIntervalUnit') is not None:
				self.add_body_params('CheckDetailDTO.' + str(i + 1) + '.CheckIntervalUnit' , CheckDetailDTOs[i].get('CheckIntervalUnit'))
			if CheckDetailDTOs[i].get('CheckExtras') is not None:
				self.add_body_params('CheckDetailDTO.' + str(i + 1) + '.CheckExtras' , CheckDetailDTOs[i].get('CheckExtras'))
			if CheckDetailDTOs[i].get('CheckIntervalVal') is not None:
				self.add_body_params('CheckDetailDTO.' + str(i + 1) + '.CheckIntervalVal' , CheckDetailDTOs[i].get('CheckIntervalVal'))


	def get_Extras(self):
		return self.get_body_params().get('Extras')

	def set_Extras(self,Extras):
		self.add_body_params('Extras', Extras)