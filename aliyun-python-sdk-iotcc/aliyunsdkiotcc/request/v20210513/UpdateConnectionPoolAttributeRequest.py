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

class UpdateConnectionPoolAttributeRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'IoTCC', '2021-05-13', 'UpdateConnectionPoolAttribute','cciot')
		self.set_method('POST')

	def get_ClientToken(self):
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self,ClientToken):
		self.add_query_param('ClientToken',ClientToken)

	def get_ConnectionPoolDescription(self):
		return self.get_query_params().get('ConnectionPoolDescription')

	def set_ConnectionPoolDescription(self,ConnectionPoolDescription):
		self.add_query_param('ConnectionPoolDescription',ConnectionPoolDescription)

	def get_ConnectionPoolId(self):
		return self.get_query_params().get('ConnectionPoolId')

	def set_ConnectionPoolId(self,ConnectionPoolId):
		self.add_query_param('ConnectionPoolId',ConnectionPoolId)

	def get_Cidrss(self):
		return self.get_query_params().get('Cidrs')

	def set_Cidrss(self, Cidrss):
		for depth1 in range(len(Cidrss)):
			if Cidrss[depth1] is not None:
				self.add_query_param('Cidrs.' + str(depth1 + 1) , Cidrss[depth1])

	def get_ConnectionPoolName(self):
		return self.get_query_params().get('ConnectionPoolName')

	def set_ConnectionPoolName(self,ConnectionPoolName):
		self.add_query_param('ConnectionPoolName',ConnectionPoolName)

	def get_DryRun(self):
		return self.get_query_params().get('DryRun')

	def set_DryRun(self,DryRun):
		self.add_query_param('DryRun',DryRun)

	def get_Count(self):
		return self.get_query_params().get('Count')

	def set_Count(self,Count):
		self.add_query_param('Count',Count)

	def get_IoTCloudConnectorId(self):
		return self.get_query_params().get('IoTCloudConnectorId')

	def set_IoTCloudConnectorId(self,IoTCloudConnectorId):
		self.add_query_param('IoTCloudConnectorId',IoTCloudConnectorId)