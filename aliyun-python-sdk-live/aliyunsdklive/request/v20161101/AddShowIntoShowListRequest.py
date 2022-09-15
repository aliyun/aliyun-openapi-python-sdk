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
from aliyunsdklive.endpoint import endpoint_data

class AddShowIntoShowListRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'live', '2016-11-01', 'AddShowIntoShowList','live')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_showLists(self): # RepeatList
		return self.get_query_params().get('showList')

	def set_showLists(self, showList):  # RepeatList
		for depth1 in range(len(showList)):
			if showList[depth1].get('showName') is not None:
				self.add_query_param('showList.' + str(depth1 + 1) + '.showName', showList[depth1].get('showName'))
			if showList[depth1].get('repeatTimes') is not None:
				self.add_query_param('showList.' + str(depth1 + 1) + '.repeatTimes', showList[depth1].get('repeatTimes'))
			if showList[depth1].get('resourceType') is not None:
				self.add_query_param('showList.' + str(depth1 + 1) + '.resourceType', showList[depth1].get('resourceType'))
			if showList[depth1].get('resourceUrl') is not None:
				self.add_query_param('showList.' + str(depth1 + 1) + '.resourceUrl', showList[depth1].get('resourceUrl'))
			if showList[depth1].get('liveInputType') is not None:
				self.add_query_param('showList.' + str(depth1 + 1) + '.liveInputType', showList[depth1].get('liveInputType'))
			if showList[depth1].get('duration') is not None:
				self.add_query_param('showList.' + str(depth1 + 1) + '.duration', showList[depth1].get('duration'))
			if showList[depth1].get('resourceId') is not None:
				self.add_query_param('showList.' + str(depth1 + 1) + '.resourceId', showList[depth1].get('resourceId'))
	def get_LiveInputType(self): # Integer
		return self.get_query_params().get('LiveInputType')

	def set_LiveInputType(self, LiveInputType):  # Integer
		self.add_query_param('LiveInputType', LiveInputType)
	def get_isBatchMode(self): # Boolean
		return self.get_query_params().get('isBatchMode')

	def set_isBatchMode(self, isBatchMode):  # Boolean
		self.add_query_param('isBatchMode', isBatchMode)
	def get_Duration(self): # Long
		return self.get_query_params().get('Duration')

	def set_Duration(self, Duration):  # Long
		self.add_query_param('Duration', Duration)
	def get_RepeatTimes(self): # Integer
		return self.get_query_params().get('RepeatTimes')

	def set_RepeatTimes(self, RepeatTimes):  # Integer
		self.add_query_param('RepeatTimes', RepeatTimes)
	def get_ShowName(self): # String
		return self.get_query_params().get('ShowName')

	def set_ShowName(self, ShowName):  # String
		self.add_query_param('ShowName', ShowName)
	def get_ResourceId(self): # String
		return self.get_query_params().get('ResourceId')

	def set_ResourceId(self, ResourceId):  # String
		self.add_query_param('ResourceId', ResourceId)
	def get_CasterId(self): # String
		return self.get_query_params().get('CasterId')

	def set_CasterId(self, CasterId):  # String
		self.add_query_param('CasterId', CasterId)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_ResourceType(self): # String
		return self.get_query_params().get('ResourceType')

	def set_ResourceType(self, ResourceType):  # String
		self.add_query_param('ResourceType', ResourceType)
	def get_ResourceUrl(self): # String
		return self.get_query_params().get('ResourceUrl')

	def set_ResourceUrl(self, ResourceUrl):  # String
		self.add_query_param('ResourceUrl', ResourceUrl)
	def get_Spot(self): # Integer
		return self.get_query_params().get('Spot')

	def set_Spot(self, Spot):  # Integer
		self.add_query_param('Spot', Spot)
