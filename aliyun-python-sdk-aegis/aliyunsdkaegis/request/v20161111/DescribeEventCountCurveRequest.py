# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
class DescribeEventCountCurveRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'aegis', '2016-11-11', 'DescribeEventCountCurve','vipaegis')

	def get_Types(self):
		return self.get_query_params().get('Types')

	def set_Types(self,Types):
		self.add_query_param('Types',Types)

	def get_SourceIp(self):
		return self.get_query_params().get('SourceIp')

	def set_SourceIp(self,SourceIp):
		self.add_query_param('SourceIp',SourceIp)

	def get_VulEventLevels(self):
		return self.get_query_params().get('VulEventLevels')

	def set_VulEventLevels(self,VulEventLevels):
		self.add_query_param('VulEventLevels',VulEventLevels)

	def get_LastDays(self):
		return self.get_query_params().get('LastDays')

	def set_LastDays(self,LastDays):
		self.add_query_param('LastDays',LastDays)

	def get_HealthEventLevels(self):
		return self.get_query_params().get('HealthEventLevels')

	def set_HealthEventLevels(self,HealthEventLevels):
		self.add_query_param('HealthEventLevels',HealthEventLevels)

	def get_SuspiciousEventLevels(self):
		return self.get_query_params().get('SuspiciousEventLevels')

	def set_SuspiciousEventLevels(self,SuspiciousEventLevels):
		self.add_query_param('SuspiciousEventLevels',SuspiciousEventLevels)