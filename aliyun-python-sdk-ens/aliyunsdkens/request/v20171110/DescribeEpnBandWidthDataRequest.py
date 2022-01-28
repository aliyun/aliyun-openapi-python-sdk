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

class DescribeEpnBandWidthDataRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ens', '2017-11-10', 'DescribeEpnBandWidthData','ens')
		self.set_method('POST')

	def get_Isp(self): # String
		return self.get_query_params().get('Isp')

	def set_Isp(self, Isp):  # String
		self.add_query_param('Isp', Isp)
	def get_StartTime(self): # String
		return self.get_query_params().get('StartTime')

	def set_StartTime(self, StartTime):  # String
		self.add_query_param('StartTime', StartTime)
	def get_EnsRegionId(self): # String
		return self.get_query_params().get('EnsRegionId')

	def set_EnsRegionId(self, EnsRegionId):  # String
		self.add_query_param('EnsRegionId', EnsRegionId)
	def get_EPNInstanceId(self): # String
		return self.get_query_params().get('EPNInstanceId')

	def set_EPNInstanceId(self, EPNInstanceId):  # String
		self.add_query_param('EPNInstanceId', EPNInstanceId)
	def get_Period(self): # String
		return self.get_query_params().get('Period')

	def set_Period(self, Period):  # String
		self.add_query_param('Period', Period)
	def get_InstanceId(self): # String
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self, InstanceId):  # String
		self.add_query_param('InstanceId', InstanceId)
	def get_NetworkingModel(self): # String
		return self.get_query_params().get('NetworkingModel')

	def set_NetworkingModel(self, NetworkingModel):  # String
		self.add_query_param('NetworkingModel', NetworkingModel)
	def get_EndTime(self): # String
		return self.get_query_params().get('EndTime')

	def set_EndTime(self, EndTime):  # String
		self.add_query_param('EndTime', EndTime)
