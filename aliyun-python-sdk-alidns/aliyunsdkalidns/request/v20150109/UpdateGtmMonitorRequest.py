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
from aliyunsdkalidns.endpoint import endpoint_data

class UpdateGtmMonitorRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Alidns', '2015-01-09', 'UpdateGtmMonitor','alidns')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_MonitorExtendInfo(self):
		return self.get_query_params().get('MonitorExtendInfo')

	def set_MonitorExtendInfo(self,MonitorExtendInfo):
		self.add_query_param('MonitorExtendInfo',MonitorExtendInfo)

	def get_MonitorConfigId(self):
		return self.get_query_params().get('MonitorConfigId')

	def set_MonitorConfigId(self,MonitorConfigId):
		self.add_query_param('MonitorConfigId',MonitorConfigId)

	def get_Timeout(self):
		return self.get_query_params().get('Timeout')

	def set_Timeout(self,Timeout):
		self.add_query_param('Timeout',Timeout)

	def get_EvaluationCount(self):
		return self.get_query_params().get('EvaluationCount')

	def set_EvaluationCount(self,EvaluationCount):
		self.add_query_param('EvaluationCount',EvaluationCount)

	def get_ProtocolType(self):
		return self.get_query_params().get('ProtocolType')

	def set_ProtocolType(self,ProtocolType):
		self.add_query_param('ProtocolType',ProtocolType)

	def get_Interval(self):
		return self.get_query_params().get('Interval')

	def set_Interval(self,Interval):
		self.add_query_param('Interval',Interval)

	def get_Lang(self):
		return self.get_query_params().get('Lang')

	def set_Lang(self,Lang):
		self.add_query_param('Lang',Lang)

	def get_IspCityNodes(self):
		return self.get_query_params().get('IspCityNodes')

	def set_IspCityNodes(self,IspCityNodes):
		for i in range(len(IspCityNodes)):	
			if IspCityNodes[i].get('CityCode') is not None:
				self.add_query_param('IspCityNode.' + str(i + 1) + '.CityCode' , IspCityNodes[i].get('CityCode'))
			if IspCityNodes[i].get('IspCode') is not None:
				self.add_query_param('IspCityNode.' + str(i + 1) + '.IspCode' , IspCityNodes[i].get('IspCode'))
