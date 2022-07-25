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

class SubmitDiagnoseTaskForSingleCardRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'IoTCC', '2021-05-13', 'SubmitDiagnoseTaskForSingleCard','IoTCC')
		self.set_method('POST')

	def get_DestinationType(self): # String
		return self.get_query_params().get('DestinationType')

	def set_DestinationType(self, DestinationType):  # String
		self.add_query_param('DestinationType', DestinationType)
	def get_Destination(self): # String
		return self.get_query_params().get('Destination')

	def set_Destination(self, Destination):  # String
		self.add_query_param('Destination', Destination)
	def get_Source(self): # String
		return self.get_query_params().get('Source')

	def set_Source(self, Source):  # String
		self.add_query_param('Source', Source)
	def get_ResourceUid(self): # Long
		return self.get_query_params().get('ResourceUid')

	def set_ResourceUid(self, ResourceUid):  # Long
		self.add_query_param('ResourceUid', ResourceUid)
	def get_SourceType(self): # String
		return self.get_query_params().get('SourceType')

	def set_SourceType(self, SourceType):  # String
		self.add_query_param('SourceType', SourceType)
	def get_EndTime(self): # Long
		return self.get_query_params().get('EndTime')

	def set_EndTime(self, EndTime):  # Long
		self.add_query_param('EndTime', EndTime)
	def get_BeginTime(self): # Long
		return self.get_query_params().get('BeginTime')

	def set_BeginTime(self, BeginTime):  # Long
		self.add_query_param('BeginTime', BeginTime)
	def get_IoTCloudConnectorId(self): # String
		return self.get_query_params().get('IoTCloudConnectorId')

	def set_IoTCloudConnectorId(self, IoTCloudConnectorId):  # String
		self.add_query_param('IoTCloudConnectorId', IoTCloudConnectorId)
