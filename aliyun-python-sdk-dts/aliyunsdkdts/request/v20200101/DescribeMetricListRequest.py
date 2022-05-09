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
from aliyunsdkdts.endpoint import endpoint_data

class DescribeMetricListRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Dts', '2020-01-01', 'DescribeMetricList','dts')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_MetricType(self): # String
		return self.get_body_params().get('MetricType')

	def set_MetricType(self, MetricType):  # String
		self.add_body_params('MetricType', MetricType)
	def get_ClientToken(self): # String
		return self.get_body_params().get('ClientToken')

	def set_ClientToken(self, ClientToken):  # String
		self.add_body_params('ClientToken', ClientToken)
	def get_StartTime(self): # Long
		return self.get_body_params().get('StartTime')

	def set_StartTime(self, StartTime):  # Long
		self.add_body_params('StartTime', StartTime)
	def get_AccountId(self): # String
		return self.get_body_params().get('AccountId')

	def set_AccountId(self, AccountId):  # String
		self.add_body_params('AccountId', AccountId)
	def get_Param(self): # String
		return self.get_body_params().get('Param')

	def set_Param(self, Param):  # String
		self.add_body_params('Param', Param)
	def get_DtsJobId(self): # String
		return self.get_body_params().get('DtsJobId')

	def set_DtsJobId(self, DtsJobId):  # String
		self.add_body_params('DtsJobId', DtsJobId)
	def get_MetricName(self): # String
		return self.get_body_params().get('MetricName')

	def set_MetricName(self, MetricName):  # String
		self.add_body_params('MetricName', MetricName)
	def get_Period(self): # Long
		return self.get_body_params().get('Period')

	def set_Period(self, Period):  # Long
		self.add_body_params('Period', Period)
	def get_EndTime(self): # Long
		return self.get_body_params().get('EndTime')

	def set_EndTime(self, EndTime):  # Long
		self.add_body_params('EndTime', EndTime)
	def get_Env(self): # String
		return self.get_body_params().get('Env')

	def set_Env(self, Env):  # String
		self.add_body_params('Env', Env)
	def get_OwnerID(self): # String
		return self.get_body_params().get('OwnerID')

	def set_OwnerID(self, OwnerID):  # String
		self.add_body_params('OwnerID', OwnerID)
