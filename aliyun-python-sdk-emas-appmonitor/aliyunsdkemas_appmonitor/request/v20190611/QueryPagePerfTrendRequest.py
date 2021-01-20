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
from aliyunsdkemas_appmonitor.endpoint import endpoint_data

class QueryPagePerfTrendRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'emas-appmonitor', '2019-06-11', 'QueryPagePerfTrend')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_MetricType(self):
		return self.get_body_params().get('MetricType')

	def set_MetricType(self,MetricType):
		self.add_body_params('MetricType', MetricType)

	def get_AppVersionStrategy(self):
		return self.get_body_params().get('AppVersionStrategy')

	def set_AppVersionStrategy(self,AppVersionStrategy):
		self.add_body_params('AppVersionStrategy', AppVersionStrategy)

	def get_StartTime(self):
		return self.get_body_params().get('StartTime')

	def set_StartTime(self,StartTime):
		self.add_body_params('StartTime', StartTime)

	def get_DeviceLevel(self):
		return self.get_body_params().get('DeviceLevel')

	def set_DeviceLevel(self,DeviceLevel):
		self.add_body_params('DeviceLevel', DeviceLevel)

	def get_Province(self):
		return self.get_body_params().get('Province')

	def set_Province(self, Provinces):
		for depth1 in range(len(Provinces)):
			if Provinces[depth1] is not None:
				self.add_body_params('Province.' + str(depth1 + 1) , Provinces[depth1])

	def get_StatType(self):
		return self.get_body_params().get('StatType')

	def set_StatType(self,StatType):
		self.add_body_params('StatType', StatType)

	def get_IntervalMinutes(self):
		return self.get_body_params().get('IntervalMinutes')

	def set_IntervalMinutes(self,IntervalMinutes):
		self.add_body_params('IntervalMinutes', IntervalMinutes)

	def get_UniqueAppId(self):
		return self.get_body_params().get('UniqueAppId')

	def set_UniqueAppId(self,UniqueAppId):
		self.add_body_params('UniqueAppId', UniqueAppId)

	def get_EndTime(self):
		return self.get_body_params().get('EndTime')

	def set_EndTime(self,EndTime):
		self.add_body_params('EndTime', EndTime)

	def get_AppVersion(self):
		return self.get_body_params().get('AppVersion')

	def set_AppVersion(self, AppVersions):
		for depth1 in range(len(AppVersions)):
			if AppVersions[depth1] is not None:
				self.add_body_params('AppVersion.' + str(depth1 + 1) , AppVersions[depth1])

	def get_Page(self):
		return self.get_body_params().get('Page')

	def set_Page(self, Pages):
		for depth1 in range(len(Pages)):
			if Pages[depth1] is not None:
				self.add_body_params('Page.' + str(depth1 + 1) , Pages[depth1])