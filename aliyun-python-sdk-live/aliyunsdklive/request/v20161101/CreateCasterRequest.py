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
from aliyunsdklive.endpoint import endpoint_data

class CreateCasterRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'live', '2016-11-01', 'CreateCaster','live')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ClientToken(self): # String
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self, ClientToken):  # String
		self.add_query_param('ClientToken', ClientToken)
	def get_CasterName(self): # String
		return self.get_query_params().get('CasterName')

	def set_CasterName(self, CasterName):  # String
		self.add_query_param('CasterName', CasterName)
	def get_CasterTemplate(self): # String
		return self.get_query_params().get('CasterTemplate')

	def set_CasterTemplate(self, CasterTemplate):  # String
		self.add_query_param('CasterTemplate', CasterTemplate)
	def get_ExpireTime(self): # String
		return self.get_query_params().get('ExpireTime')

	def set_ExpireTime(self, ExpireTime):  # String
		self.add_query_param('ExpireTime', ExpireTime)
	def get_NormType(self): # Integer
		return self.get_query_params().get('NormType')

	def set_NormType(self, NormType):  # Integer
		self.add_query_param('NormType', NormType)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_PurchaseTime(self): # String
		return self.get_query_params().get('PurchaseTime')

	def set_PurchaseTime(self, PurchaseTime):  # String
		self.add_query_param('PurchaseTime', PurchaseTime)
	def get_ChargeType(self): # String
		return self.get_query_params().get('ChargeType')

	def set_ChargeType(self, ChargeType):  # String
		self.add_query_param('ChargeType', ChargeType)
