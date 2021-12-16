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

class CreateConnectionPoolRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'IoTCC', '2021-05-13', 'CreateConnectionPool','IoTCC')
		self.set_method('POST')

	def get_ClientToken(self): # String
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self, ClientToken):  # String
		self.add_query_param('ClientToken', ClientToken)
	def get_ConnectionPoolDescription(self): # String
		return self.get_query_params().get('ConnectionPoolDescription')

	def set_ConnectionPoolDescription(self, ConnectionPoolDescription):  # String
		self.add_query_param('ConnectionPoolDescription', ConnectionPoolDescription)
	def get_Cidrss(self): # RepeatList
		return self.get_query_params().get('Cidrs')

	def set_Cidrss(self, Cidrs):  # RepeatList
		for depth1 in range(len(Cidrs)):
			self.add_query_param('Cidrs.' + str(depth1 + 1), Cidrs[depth1])
	def get_ConnectionPoolName(self): # String
		return self.get_query_params().get('ConnectionPoolName')

	def set_ConnectionPoolName(self, ConnectionPoolName):  # String
		self.add_query_param('ConnectionPoolName', ConnectionPoolName)
	def get_DryRun(self): # Boolean
		return self.get_query_params().get('DryRun')

	def set_DryRun(self, DryRun):  # Boolean
		self.add_query_param('DryRun', DryRun)
	def get_Count(self): # Long
		return self.get_query_params().get('Count')

	def set_Count(self, Count):  # Long
		self.add_query_param('Count', Count)
	def get_IoTCloudConnectorId(self): # String
		return self.get_query_params().get('IoTCloudConnectorId')

	def set_IoTCloudConnectorId(self, IoTCloudConnectorId):  # String
		self.add_query_param('IoTCloudConnectorId', IoTCloudConnectorId)
