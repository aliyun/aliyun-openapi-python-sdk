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
from aliyunsdkrds.endpoint import endpoint_data
import json

class ModifyRCInstanceAttributeRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Rds', '2014-08-15', 'ModifyRCInstanceAttribute','rds')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_SecurityGroupId(self): # String
		return self.get_query_params().get('SecurityGroupId')

	def set_SecurityGroupId(self, SecurityGroupId):  # String
		self.add_query_param('SecurityGroupId', SecurityGroupId)
	def get_DeletionProtection(self): # Boolean
		return self.get_query_params().get('DeletionProtection')

	def set_DeletionProtection(self, DeletionProtection):  # Boolean
		self.add_query_param('DeletionProtection', DeletionProtection)
	def get_Password(self): # String
		return self.get_query_params().get('Password')

	def set_Password(self, Password):  # String
		self.add_query_param('Password', Password)
	def get_HostName(self): # String
		return self.get_query_params().get('HostName')

	def set_HostName(self, HostName):  # String
		self.add_query_param('HostName', HostName)
	def get_Reboot(self): # Boolean
		return self.get_query_params().get('Reboot')

	def set_Reboot(self, Reboot):  # Boolean
		self.add_query_param('Reboot', Reboot)
	def get_SecurityGroupIds(self): # Array
		return self.get_query_params().get('SecurityGroupIds')

	def set_SecurityGroupIds(self, SecurityGroupIds):  # Array
		self.add_query_param("SecurityGroupIds", json.dumps(SecurityGroupIds))
	def get_InstanceId(self): # String
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self, InstanceId):  # String
		self.add_query_param('InstanceId', InstanceId)
	def get_InstanceIds(self): # Array
		return self.get_query_params().get('InstanceIds')

	def set_InstanceIds(self, InstanceIds):  # Array
		self.add_query_param("InstanceIds", json.dumps(InstanceIds))
