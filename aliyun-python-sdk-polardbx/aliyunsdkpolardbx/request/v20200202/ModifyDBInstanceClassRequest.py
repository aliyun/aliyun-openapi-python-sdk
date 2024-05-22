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

class ModifyDBInstanceClassRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'polardbx', '2020-02-02', 'ModifyDBInstanceClass','polardbx')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_SpecifiedDNSpecMapJson(self): # String
		return self.get_query_params().get('SpecifiedDNSpecMapJson')

	def set_SpecifiedDNSpecMapJson(self, SpecifiedDNSpecMapJson):  # String
		self.add_query_param('SpecifiedDNSpecMapJson', SpecifiedDNSpecMapJson)
	def get_CnClass(self): # String
		return self.get_query_params().get('CnClass')

	def set_CnClass(self, CnClass):  # String
		self.add_query_param('CnClass', CnClass)
	def get_TargetDBInstanceClass(self): # String
		return self.get_query_params().get('TargetDBInstanceClass')

	def set_TargetDBInstanceClass(self, TargetDBInstanceClass):  # String
		self.add_query_param('TargetDBInstanceClass', TargetDBInstanceClass)
	def get_SpecifiedDNScale(self): # Boolean
		return self.get_query_params().get('SpecifiedDNScale')

	def set_SpecifiedDNScale(self, SpecifiedDNScale):  # Boolean
		self.add_query_param('SpecifiedDNScale', SpecifiedDNScale)
	def get_DBInstanceName(self): # String
		return self.get_query_params().get('DBInstanceName')

	def set_DBInstanceName(self, DBInstanceName):  # String
		self.add_query_param('DBInstanceName', DBInstanceName)
	def get_ClientToken(self): # String
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self, ClientToken):  # String
		self.add_query_param('ClientToken', ClientToken)
	def get_SwitchTimeMode(self): # String
		return self.get_query_params().get('SwitchTimeMode')

	def set_SwitchTimeMode(self, SwitchTimeMode):  # String
		self.add_query_param('SwitchTimeMode', SwitchTimeMode)
	def get_SwitchTime(self): # String
		return self.get_query_params().get('SwitchTime')

	def set_SwitchTime(self, SwitchTime):  # String
		self.add_query_param('SwitchTime', SwitchTime)
	def get_DnClass(self): # String
		return self.get_query_params().get('DnClass')

	def set_DnClass(self, DnClass):  # String
		self.add_query_param('DnClass', DnClass)
