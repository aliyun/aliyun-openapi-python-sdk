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
		RpcRequest.__init__(self, 'IoTCC', '2021-05-13', 'ListIoTCloudConnectors','IoTCC')
		self.set_method('POST')

	def get_IoTCloudConnectorStatuss(self): # RepeatList
		return self.get_query_params().get('IoTCloudConnectorStatus')

	def set_IoTCloudConnectorStatuss(self, IoTCloudConnectorStatus):  # RepeatList
		for depth1 in range(len(IoTCloudConnectorStatus)):
			self.add_query_param('IoTCloudConnectorStatus.' + str(depth1 + 1), IoTCloudConnectorStatus[depth1])
	def get_ISPs(self): # RepeatList
		return self.get_query_params().get('ISP')

	def set_ISPs(self, ISP):  # RepeatList
		for depth1 in range(len(ISP)):
			self.add_query_param('ISP.' + str(depth1 + 1), ISP[depth1])
	def get_IoTCloudConnectorIdss(self): # RepeatList
		return self.get_query_params().get('IoTCloudConnectorIds')

	def set_IoTCloudConnectorIdss(self, IoTCloudConnectorIds):  # RepeatList
		for depth1 in range(len(IoTCloudConnectorIds)):
			self.add_query_param('IoTCloudConnectorIds.' + str(depth1 + 1), IoTCloudConnectorIds[depth1])
	def get_NextToken(self): # String
		return self.get_query_params().get('NextToken')

	def set_NextToken(self, NextToken):  # String
		self.add_query_param('NextToken', NextToken)
	def get_APNs(self): # RepeatList
		return self.get_query_params().get('APN')

	def set_APNs(self, APN):  # RepeatList
		for depth1 in range(len(APN)):
			self.add_query_param('APN.' + str(depth1 + 1), APN[depth1])
	def get_IoTCloudConnectorGroupId(self): # String
		return self.get_query_params().get('IoTCloudConnectorGroupId')

	def set_IoTCloudConnectorGroupId(self, IoTCloudConnectorGroupId):  # String
		self.add_query_param('IoTCloudConnectorGroupId', IoTCloudConnectorGroupId)
	def get_IsInGroup(self): # Boolean
		return self.get_query_params().get('IsInGroup')

	def set_IsInGroup(self, IsInGroup):  # Boolean
		self.add_query_param('IsInGroup', IsInGroup)
	def get_VpcIds(self): # RepeatList
		return self.get_query_params().get('VpcId')

	def set_VpcIds(self, VpcId):  # RepeatList
		for depth1 in range(len(VpcId)):
			self.add_query_param('VpcId.' + str(depth1 + 1), VpcId[depth1])
	def get_MaxResults(self): # Integer
		return self.get_query_params().get('MaxResults')

	def set_MaxResults(self, MaxResults):  # Integer
		self.add_query_param('MaxResults', MaxResults)
	def get_IoTCloudConnectorNames(self): # RepeatList
		return self.get_query_params().get('IoTCloudConnectorName')

	def set_IoTCloudConnectorNames(self, IoTCloudConnectorName):  # RepeatList
		for depth1 in range(len(IoTCloudConnectorName)):
			self.add_query_param('IoTCloudConnectorName.' + str(depth1 + 1), IoTCloudConnectorName[depth1])
