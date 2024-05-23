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
from aliyunsdkoceanbasepro.endpoint import endpoint_data

class DescribeProcessStatsCompositionRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'OceanBasePro', '2019-09-01', 'DescribeProcessStatsComposition','oceanbase')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_UId(self): # String
		return self.get_body_params().get('UId')

	def set_UId(self, UId):  # String
		self.add_body_params('UId', UId)
	def get_SqlText(self): # String
		return self.get_body_params().get('SqlText')

	def set_SqlText(self, SqlText):  # String
		self.add_body_params('SqlText', SqlText)
	def get_ClientIp(self): # String
		return self.get_body_params().get('ClientIp')

	def set_ClientIp(self, ClientIp):  # String
		self.add_body_params('ClientIp', ClientIp)
	def get_TenantId(self): # String
		return self.get_body_params().get('TenantId')

	def set_TenantId(self, TenantId):  # String
		self.add_body_params('TenantId', TenantId)
	def get_ServerIp(self): # String
		return self.get_body_params().get('ServerIp')

	def set_ServerIp(self, ServerIp):  # String
		self.add_body_params('ServerIp', ServerIp)
	def get_Users(self): # String
		return self.get_body_params().get('Users')

	def set_Users(self, Users):  # String
		self.add_body_params('Users', Users)
	def get_InstanceId(self): # String
		return self.get_body_params().get('InstanceId')

	def set_InstanceId(self, InstanceId):  # String
		self.add_body_params('InstanceId', InstanceId)
	def get_Status(self): # String
		return self.get_body_params().get('Status')

	def set_Status(self, Status):  # String
		self.add_body_params('Status', Status)
