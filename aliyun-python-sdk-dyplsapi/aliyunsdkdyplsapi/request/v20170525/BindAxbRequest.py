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
from aliyunsdkdyplsapi.endpoint import endpoint_data

class BindAxbRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Dyplsapi', '2017-05-25', 'BindAxb','dypls')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_CallDisplayType(self):
		return self.get_query_params().get('CallDisplayType')

	def set_CallDisplayType(self,CallDisplayType):
		self.add_query_param('CallDisplayType',CallDisplayType)

	def get_PhoneNoX(self):
		return self.get_query_params().get('PhoneNoX')

	def set_PhoneNoX(self,PhoneNoX):
		self.add_query_param('PhoneNoX',PhoneNoX)

	def get_RingConfig(self):
		return self.get_query_params().get('RingConfig')

	def set_RingConfig(self,RingConfig):
		self.add_query_param('RingConfig',RingConfig)

	def get_PhoneNoB(self):
		return self.get_query_params().get('PhoneNoB')

	def set_PhoneNoB(self,PhoneNoB):
		self.add_query_param('PhoneNoB',PhoneNoB)

	def get_PhoneNoA(self):
		return self.get_query_params().get('PhoneNoA')

	def set_PhoneNoA(self,PhoneNoA):
		self.add_query_param('PhoneNoA',PhoneNoA)

	def get_ExpectCity(self):
		return self.get_query_params().get('ExpectCity')

	def set_ExpectCity(self,ExpectCity):
		self.add_query_param('ExpectCity',ExpectCity)

	def get_ResourceOwnerAccount(self):
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self,ResourceOwnerAccount):
		self.add_query_param('ResourceOwnerAccount',ResourceOwnerAccount)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_OutOrderId(self):
		return self.get_query_params().get('OutOrderId')

	def set_OutOrderId(self,OutOrderId):
		self.add_query_param('OutOrderId',OutOrderId)

	def get_PoolKey(self):
		return self.get_query_params().get('PoolKey')

	def set_PoolKey(self,PoolKey):
		self.add_query_param('PoolKey',PoolKey)

	def get_Expiration(self):
		return self.get_query_params().get('Expiration')

	def set_Expiration(self,Expiration):
		self.add_query_param('Expiration',Expiration)

	def get_IsRecordingEnabled(self):
		return self.get_query_params().get('IsRecordingEnabled')

	def set_IsRecordingEnabled(self,IsRecordingEnabled):
		self.add_query_param('IsRecordingEnabled',IsRecordingEnabled)

	def get_OutId(self):
		return self.get_query_params().get('OutId')

	def set_OutId(self,OutId):
		self.add_query_param('OutId',OutId)

	def get_CallRestrict(self):
		return self.get_query_params().get('CallRestrict')

	def set_CallRestrict(self,CallRestrict):
		self.add_query_param('CallRestrict',CallRestrict)