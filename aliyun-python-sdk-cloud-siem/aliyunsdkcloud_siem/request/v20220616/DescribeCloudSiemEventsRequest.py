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

class DescribeCloudSiemEventsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'cloud-siem', '2022-06-16', 'DescribeCloudSiemEvents','cloud-siem')
		self.set_method('POST')

	def get_StartTime(self): # Long
		return self.get_body_params().get('StartTime')

	def set_StartTime(self, StartTime):  # Long
		self.add_body_params('StartTime', StartTime)
	def get_EventName(self): # String
		return self.get_body_params().get('EventName')

	def set_EventName(self, EventName):  # String
		self.add_body_params('EventName', EventName)
	def get_PageSize(self): # Integer
		return self.get_body_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Integer
		self.add_body_params('PageSize', PageSize)
	def get_OrderField(self): # String
		return self.get_body_params().get('OrderField')

	def set_OrderField(self, OrderField):  # String
		self.add_body_params('OrderField', OrderField)
	def get_Order(self): # String
		return self.get_body_params().get('Order')

	def set_Order(self, Order):  # String
		self.add_body_params('Order', Order)
	def get_EndTime(self): # Long
		return self.get_body_params().get('EndTime')

	def set_EndTime(self, EndTime):  # Long
		self.add_body_params('EndTime', EndTime)
	def get_CurrentPage(self): # Integer
		return self.get_body_params().get('CurrentPage')

	def set_CurrentPage(self, CurrentPage):  # Integer
		self.add_body_params('CurrentPage', CurrentPage)
	def get_ThreadLevels(self): # RepeatList
		return self.get_body_params().get('ThreadLevel')

	def set_ThreadLevels(self, ThreadLevel):  # RepeatList
		for depth1 in range(len(ThreadLevel)):
			self.add_body_params('ThreadLevel.' + str(depth1 + 1), ThreadLevel[depth1])
	def get_AssetId(self): # String
		return self.get_body_params().get('AssetId')

	def set_AssetId(self, AssetId):  # String
		self.add_body_params('AssetId', AssetId)
	def get_IncidentUuid(self): # String
		return self.get_body_params().get('IncidentUuid')

	def set_IncidentUuid(self, IncidentUuid):  # String
		self.add_body_params('IncidentUuid', IncidentUuid)
	def get_Status(self): # Integer
		return self.get_body_params().get('Status')

	def set_Status(self, Status):  # Integer
		self.add_body_params('Status', Status)
