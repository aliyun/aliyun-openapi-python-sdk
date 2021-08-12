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
from aliyunsdkdms_enterprise.endpoint import endpoint_data

class CreateProxyAccessRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'dms-enterprise', '2018-11-01', 'CreateProxyAccess','dms-enterprise')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_IndepAccount(self): # String
		return self.get_query_params().get('IndepAccount')

	def set_IndepAccount(self, IndepAccount):  # String
		self.add_query_param('IndepAccount', IndepAccount)
	def get_UserId(self): # Long
		return self.get_query_params().get('UserId')

	def set_UserId(self, UserId):  # Long
		self.add_query_param('UserId', UserId)
	def get_Tid(self): # Long
		return self.get_query_params().get('Tid')

	def set_Tid(self, Tid):  # Long
		self.add_query_param('Tid', Tid)
	def get_IndepPassword(self): # String
		return self.get_query_params().get('IndepPassword')

	def set_IndepPassword(self, IndepPassword):  # String
		self.add_query_param('IndepPassword', IndepPassword)
	def get_ProxyId(self): # Long
		return self.get_query_params().get('ProxyId')

	def set_ProxyId(self, ProxyId):  # Long
		self.add_query_param('ProxyId', ProxyId)
