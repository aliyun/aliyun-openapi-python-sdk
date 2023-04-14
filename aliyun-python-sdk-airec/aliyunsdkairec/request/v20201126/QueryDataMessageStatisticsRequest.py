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

from aliyunsdkcore.request import RoaRequest
from aliyunsdkairec.endpoint import endpoint_data

class QueryDataMessageStatisticsRequest(RoaRequest):

	def __init__(self):
		RoaRequest.__init__(self, 'Airec', '2020-11-26', 'QueryDataMessageStatistics','airec')
		self.set_uri_pattern('/v2/openapi/instances/[instanceId]/tables/[table]/data-message-statistics')
		self.set_method('GET')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_traceId(self): # String
		return self.get_query_params().get('traceId')

	def set_traceId(self, traceId):  # String
		self.add_query_param('traceId', traceId)
	def get_messageSource(self): # String
		return self.get_query_params().get('messageSource')

	def set_messageSource(self, messageSource):  # String
		self.add_query_param('messageSource', messageSource)
	def get_endTime(self): # Long
		return self.get_query_params().get('endTime')

	def set_endTime(self, endTime):  # Long
		self.add_query_param('endTime', endTime)
	def get_userType(self): # String
		return self.get_query_params().get('userType')

	def set_userType(self, userType):  # String
		self.add_query_param('userType', userType)
	def get_startTime(self): # Long
		return self.get_query_params().get('startTime')

	def set_startTime(self, startTime):  # Long
		self.add_query_param('startTime', startTime)
	def get_userId(self): # String
		return self.get_query_params().get('userId')

	def set_userId(self, userId):  # String
		self.add_query_param('userId', userId)
	def get_itemId(self): # String
		return self.get_query_params().get('itemId')

	def set_itemId(self, itemId):  # String
		self.add_query_param('itemId', itemId)
	def get_instanceId(self): # String
		return self.get_path_params().get('instanceId')

	def set_instanceId(self, instanceId):  # String
		self.add_path_param('instanceId', instanceId)
	def get_itemType(self): # String
		return self.get_query_params().get('itemType')

	def set_itemType(self, itemType):  # String
		self.add_query_param('itemType', itemType)
	def get_cmdType(self): # String
		return self.get_query_params().get('cmdType')

	def set_cmdType(self, cmdType):  # String
		self.add_query_param('cmdType', cmdType)
	def get_sceneId(self): # String
		return self.get_query_params().get('sceneId')

	def set_sceneId(self, sceneId):  # String
		self.add_query_param('sceneId', sceneId)
	def get_imei(self): # String
		return self.get_query_params().get('imei')

	def set_imei(self, imei):  # String
		self.add_query_param('imei', imei)
	def get_bhvType(self): # String
		return self.get_query_params().get('bhvType')

	def set_bhvType(self, bhvType):  # String
		self.add_query_param('bhvType', bhvType)
	def get_table(self): # String
		return self.get_path_params().get('table')

	def set_table(self, table):  # String
		self.add_path_param('table', table)
