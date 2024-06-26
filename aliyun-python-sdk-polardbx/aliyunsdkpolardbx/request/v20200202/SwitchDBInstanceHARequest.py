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
from aliyunsdkpolardbx.endpoint import endpoint_data

class SwitchDBInstanceHARequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'polardbx', '2020-02-02', 'SwitchDBInstanceHA','polardbx')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_DBInstanceName(self): # String
		return self.get_query_params().get('DBInstanceName')

	def set_DBInstanceName(self, DBInstanceName):  # String
		self.add_query_param('DBInstanceName', DBInstanceName)
	def get_SwitchTimeMode(self): # String
		return self.get_query_params().get('SwitchTimeMode')

	def set_SwitchTimeMode(self, SwitchTimeMode):  # String
		self.add_query_param('SwitchTimeMode', SwitchTimeMode)
	def get_SwitchTime(self): # String
		return self.get_query_params().get('SwitchTime')

	def set_SwitchTime(self, SwitchTime):  # String
		self.add_query_param('SwitchTime', SwitchTime)
	def get_TargetPrimaryRegionId(self): # String
		return self.get_query_params().get('TargetPrimaryRegionId')

	def set_TargetPrimaryRegionId(self, TargetPrimaryRegionId):  # String
		self.add_query_param('TargetPrimaryRegionId', TargetPrimaryRegionId)
	def get_TargetPrimaryAzoneId(self): # String
		return self.get_query_params().get('TargetPrimaryAzoneId')

	def set_TargetPrimaryAzoneId(self, TargetPrimaryAzoneId):  # String
		self.add_query_param('TargetPrimaryAzoneId', TargetPrimaryAzoneId)
