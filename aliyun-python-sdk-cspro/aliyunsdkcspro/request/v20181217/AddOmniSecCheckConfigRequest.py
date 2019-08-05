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

class AddOmniSecCheckConfigRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'cspro', '2018-12-17', 'AddOmniSecCheckConfig','cspro')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_CheckDetailDTOLists(self):
		return self.get_body_params().get('CheckDetailDTOLists')

	def set_CheckDetailDTOLists(self,CheckDetailDTOLists):
		for i in range(len(CheckDetailDTOLists)):	
			if CheckDetailDTOLists[i].get('CheckType') is not None:
				self.add_body_params('CheckDetailDTOList.' + str(i + 1) + '.CheckType' , CheckDetailDTOLists[i].get('CheckType'))
			if CheckDetailDTOLists[i].get('CheckIntervalUnit') is not None:
				self.add_body_params('CheckDetailDTOList.' + str(i + 1) + '.CheckIntervalUnit' , CheckDetailDTOLists[i].get('CheckIntervalUnit'))
			if CheckDetailDTOLists[i].get('CheckExtras') is not None:
				self.add_body_params('CheckDetailDTOList.' + str(i + 1) + '.CheckExtras' , CheckDetailDTOLists[i].get('CheckExtras'))
			if CheckDetailDTOLists[i].get('CheckIntervalVal') is not None:
				self.add_body_params('CheckDetailDTOList.' + str(i + 1) + '.CheckIntervalVal' , CheckDetailDTOLists[i].get('CheckIntervalVal'))


	def get_Name(self):
		return self.get_body_params().get('Name')

	def set_Name(self,Name):
		self.add_body_params('Name', Name)

	def get_Extras(self):
		return self.get_body_params().get('Extras')

	def set_Extras(self,Extras):
		self.add_body_params('Extras', Extras)

	def get_CheckTarget(self):
		return self.get_body_params().get('CheckTarget')

	def set_CheckTarget(self,CheckTarget):
		self.add_body_params('CheckTarget', CheckTarget)

	def get_ConfType(self):
		return self.get_body_params().get('ConfType')

	def set_ConfType(self,ConfType):
		self.add_body_params('ConfType', ConfType)