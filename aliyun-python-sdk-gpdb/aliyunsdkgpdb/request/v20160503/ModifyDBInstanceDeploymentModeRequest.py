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
from aliyunsdkgpdb.endpoint import endpoint_data

class ModifyDBInstanceDeploymentModeRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'gpdb', '2016-05-03', 'ModifyDBInstanceDeploymentMode','GPDB')
		self.set_protocol_type('https')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_DeployMode(self): # String
		return self.get_query_params().get('DeployMode')

	def set_DeployMode(self, DeployMode):  # String
		self.add_query_param('DeployMode', DeployMode)
	def get_DBInstanceId(self): # String
		return self.get_query_params().get('DBInstanceId')

	def set_DBInstanceId(self, DBInstanceId):  # String
		self.add_query_param('DBInstanceId', DBInstanceId)
	def get_StandbyVSwitchId(self): # String
		return self.get_query_params().get('StandbyVSwitchId')

	def set_StandbyVSwitchId(self, StandbyVSwitchId):  # String
		self.add_query_param('StandbyVSwitchId', StandbyVSwitchId)
	def get_StandbyZoneId(self): # String
		return self.get_query_params().get('StandbyZoneId')

	def set_StandbyZoneId(self, StandbyZoneId):  # String
		self.add_query_param('StandbyZoneId', StandbyZoneId)
