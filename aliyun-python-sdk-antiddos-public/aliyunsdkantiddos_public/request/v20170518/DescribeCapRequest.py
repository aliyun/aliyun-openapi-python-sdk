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

class DescribeCapRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'antiddos-public', '2017-05-18', 'DescribeCap')
		self.set_method('POST')

	def get_InternetIp(self): # String
		return self.get_query_params().get('InternetIp')

	def set_InternetIp(self, InternetIp):  # String
		self.add_query_param('InternetIp', InternetIp)
	def get_BegTime(self): # Long
		return self.get_query_params().get('BegTime')

	def set_BegTime(self, BegTime):  # Long
		self.add_query_param('BegTime', BegTime)
	def get_DdosRegionId(self): # String
		return self.get_query_params().get('DdosRegionId')

	def set_DdosRegionId(self, DdosRegionId):  # String
		self.add_query_param('DdosRegionId', DdosRegionId)
	def get_InstanceType(self): # String
		return self.get_query_params().get('InstanceType')

	def set_InstanceType(self, InstanceType):  # String
		self.add_query_param('InstanceType', InstanceType)
	def get_InstanceId(self): # String
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self, InstanceId):  # String
		self.add_query_param('InstanceId', InstanceId)
