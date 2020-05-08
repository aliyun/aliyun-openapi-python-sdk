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

class AddAxnTrackNoRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Dyplsapi', '2017-05-25', 'AddAxnTrackNo','dypls')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_SubsId(self):
		return self.get_query_params().get('SubsId')

	def set_SubsId(self,SubsId):
		self.add_query_param('SubsId',SubsId)

	def get_PhoneNoX(self):
		return self.get_query_params().get('PhoneNoX')

	def set_PhoneNoX(self,PhoneNoX):
		self.add_query_param('PhoneNoX',PhoneNoX)

	def get_ResourceOwnerAccount(self):
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self,ResourceOwnerAccount):
		self.add_query_param('ResourceOwnerAccount',ResourceOwnerAccount)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_trackNo(self):
		return self.get_query_params().get('trackNo')

	def set_trackNo(self,trackNo):
		self.add_query_param('trackNo',trackNo)

	def get_PoolKey(self):
		return self.get_query_params().get('PoolKey')

	def set_PoolKey(self,PoolKey):
		self.add_query_param('PoolKey',PoolKey)