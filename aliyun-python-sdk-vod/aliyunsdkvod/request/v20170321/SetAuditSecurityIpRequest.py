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
from aliyunsdkvod.endpoint import endpoint_data

class SetAuditSecurityIpRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'vod', '2017-03-21', 'SetAuditSecurityIp','vod')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_SecurityGroupName(self): # String
		return self.get_query_params().get('SecurityGroupName')

	def set_SecurityGroupName(self, SecurityGroupName):  # String
		self.add_query_param('SecurityGroupName', SecurityGroupName)
	def get_OperateMode(self): # String
		return self.get_query_params().get('OperateMode')

	def set_OperateMode(self, OperateMode):  # String
		self.add_query_param('OperateMode', OperateMode)
	def get_Ips(self): # String
		return self.get_query_params().get('Ips')

	def set_Ips(self, Ips):  # String
		self.add_query_param('Ips', Ips)
