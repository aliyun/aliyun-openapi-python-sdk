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
class DescribeRangeDataByLocateAndIspServiceRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Cdn', '2014-11-11', 'DescribeRangeDataByLocateAndIspService')

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_SecurityToken(self):
		return self.get_query_params().get('SecurityToken')

	def set_SecurityToken(self,SecurityToken):
		self.add_query_param('SecurityToken',SecurityToken)

	def get_DomainNames(self):
		return self.get_query_params().get('DomainNames')

	def set_DomainNames(self,DomainNames):
		self.add_query_param('DomainNames',DomainNames)

	def get_LocationNames(self):
		return self.get_query_params().get('LocationNames')

	def set_LocationNames(self,LocationNames):
		self.add_query_param('LocationNames',LocationNames)

	def get_IspNames(self):
		return self.get_query_params().get('IspNames')

	def set_IspNames(self,IspNames):
		self.add_query_param('IspNames',IspNames)

	def get_startTime(self):
		return self.get_query_params().get('startTime')

	def set_startTime(self,startTime):
		self.add_query_param('startTime',startTime)

	def get_EndTime(self):
		return self.get_query_params().get('EndTime')

	def set_EndTime(self,EndTime):
		self.add_query_param('EndTime',EndTime)