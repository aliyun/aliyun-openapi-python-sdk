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
from aliyunsdkmarket.endpoint import endpoint_data

class AutoRenewInstanceRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Market', '2015-11-01', 'AutoRenewInstance','yunmarket')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_Type(self): # String
		return self.get_body_params().get('Type')

	def set_Type(self, Type):  # String
		self.add_body_params('Type', Type)
	def get_OwnerId(self): # Long
		return self.get_body_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_body_params('OwnerId', OwnerId)
	def get_AutoRenewDuration(self): # Integer
		return self.get_body_params().get('AutoRenewDuration')

	def set_AutoRenewDuration(self, AutoRenewDuration):  # Integer
		self.add_body_params('AutoRenewDuration', AutoRenewDuration)
	def get_AutoRenewCycle(self): # String
		return self.get_body_params().get('AutoRenewCycle')

	def set_AutoRenewCycle(self, AutoRenewCycle):  # String
		self.add_body_params('AutoRenewCycle', AutoRenewCycle)
	def get_OrderBizId(self): # Long
		return self.get_body_params().get('OrderBizId')

	def set_OrderBizId(self, OrderBizId):  # Long
		self.add_body_params('OrderBizId', OrderBizId)
