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

class ListIoTCloudConnectorsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'IoTCC', '2021-05-13', 'ListIoTCloudConnectors','cciot')
		self.set_method('POST')

	def get_IoTCloudConnectorStatuss(self):
		return self.get_query_params().get('IoTCloudConnectorStatus')

	def set_IoTCloudConnectorStatuss(self, IoTCloudConnectorStatuss):
		for depth1 in range(len(IoTCloudConnectorStatuss)):
			if IoTCloudConnectorStatuss[depth1] is not None:
				self.add_query_param('IoTCloudConnectorStatus.' + str(depth1 + 1) , IoTCloudConnectorStatuss[depth1])

	def get_IoTCloudConnectorIdss(self):
		return self.get_query_params().get('IoTCloudConnectorIds')

	def set_IoTCloudConnectorIdss(self, IoTCloudConnectorIdss):
		for depth1 in range(len(IoTCloudConnectorIdss)):
			if IoTCloudConnectorIdss[depth1] is not None:
				self.add_query_param('IoTCloudConnectorIds.' + str(depth1 + 1) , IoTCloudConnectorIdss[depth1])

	def get_NextToken(self):
		return self.get_query_params().get('NextToken')

	def set_NextToken(self,NextToken):
		self.add_query_param('NextToken',NextToken)

	def get_Apnss(self):
		return self.get_query_params().get('Apns')

	def set_Apnss(self, Apnss):
		for depth1 in range(len(Apnss)):
			if Apnss[depth1] is not None:
				self.add_query_param('Apns.' + str(depth1 + 1) , Apnss[depth1])

	def get_VpcIdss(self):
		return self.get_query_params().get('VpcIds')

	def set_VpcIdss(self, VpcIdss):
		for depth1 in range(len(VpcIdss)):
			if VpcIdss[depth1] is not None:
				self.add_query_param('VpcIds.' + str(depth1 + 1) , VpcIdss[depth1])

	def get_Ispss(self):
		return self.get_query_params().get('Isps')

	def set_Ispss(self, Ispss):
		for depth1 in range(len(Ispss)):
			if Ispss[depth1] is not None:
				self.add_query_param('Isps.' + str(depth1 + 1) , Ispss[depth1])

	def get_MaxResults(self):
		return self.get_query_params().get('MaxResults')

	def set_MaxResults(self,MaxResults):
		self.add_query_param('MaxResults',MaxResults)

	def get_IoTCloudConnectorNames(self):
		return self.get_query_params().get('IoTCloudConnectorName')

	def set_IoTCloudConnectorNames(self, IoTCloudConnectorNames):
		for depth1 in range(len(IoTCloudConnectorNames)):
			if IoTCloudConnectorNames[depth1] is not None:
				self.add_query_param('IoTCloudConnectorName.' + str(depth1 + 1) , IoTCloudConnectorNames[depth1])