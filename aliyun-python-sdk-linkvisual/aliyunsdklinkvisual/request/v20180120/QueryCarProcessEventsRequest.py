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
from aliyunsdklinkvisual.endpoint import endpoint_data

class QueryCarProcessEventsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Linkvisual', '2018-01-20', 'QueryCarProcessEvents','Linkvisual')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ActionType(self): # Integer
		return self.get_query_params().get('ActionType')

	def set_ActionType(self, ActionType):  # Integer
		self.add_query_param('ActionType', ActionType)
	def get_SubProductKey(self): # String
		return self.get_query_params().get('SubProductKey')

	def set_SubProductKey(self, SubProductKey):  # String
		self.add_query_param('SubProductKey', SubProductKey)
	def get_PlateNo(self): # String
		return self.get_query_params().get('PlateNo')

	def set_PlateNo(self, PlateNo):  # String
		self.add_query_param('PlateNo', PlateNo)
	def get_SubDeviceName(self): # String
		return self.get_query_params().get('SubDeviceName')

	def set_SubDeviceName(self, SubDeviceName):  # String
		self.add_query_param('SubDeviceName', SubDeviceName)
	def get_IotInstanceId(self): # String
		return self.get_query_params().get('IotInstanceId')

	def set_IotInstanceId(self, IotInstanceId):  # String
		self.add_query_param('IotInstanceId', IotInstanceId)
	def get_PageSize(self): # Integer
		return self.get_query_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Integer
		self.add_query_param('PageSize', PageSize)
	def get_EndTime(self): # Long
		return self.get_query_params().get('EndTime')

	def set_EndTime(self, EndTime):  # Long
		self.add_query_param('EndTime', EndTime)
	def get_BeginTime(self): # Long
		return self.get_query_params().get('BeginTime')

	def set_BeginTime(self, BeginTime):  # Long
		self.add_query_param('BeginTime', BeginTime)
	def get_CurrentPage(self): # Integer
		return self.get_query_params().get('CurrentPage')

	def set_CurrentPage(self, CurrentPage):  # Integer
		self.add_query_param('CurrentPage', CurrentPage)
	def get_AreaIndex(self): # Integer
		return self.get_query_params().get('AreaIndex')

	def set_AreaIndex(self, AreaIndex):  # Integer
		self.add_query_param('AreaIndex', AreaIndex)
	def get_SubIotId(self): # String
		return self.get_query_params().get('SubIotId')

	def set_SubIotId(self, SubIotId):  # String
		self.add_query_param('SubIotId', SubIotId)
