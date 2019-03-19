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
class GetCrowdListRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'cloudwf', '2017-03-28', 'GetCrowdList','cloudwf')

	def get_Gsid(self):
		return self.get_query_params().get('Gsid')

	def set_Gsid(self,Gsid):
		self.add_query_param('Gsid',Gsid)

	def get_ClassType(self):
		return self.get_query_params().get('ClassType')

	def set_ClassType(self,ClassType):
		self.add_query_param('ClassType',ClassType)

	def get_GsType(self):
		return self.get_query_params().get('GsType')

	def set_GsType(self,GsType):
		self.add_query_param('GsType',GsType)

	def get_EndTime(self):
		return self.get_query_params().get('EndTime')

	def set_EndTime(self,EndTime):
		self.add_query_param('EndTime',EndTime)

	def get_Page(self):
		return self.get_query_params().get('Page')

	def set_Page(self,Page):
		self.add_query_param('Page',Page)

	def get_StartTime(self):
		return self.get_query_params().get('StartTime')

	def set_StartTime(self,StartTime):
		self.add_query_param('StartTime',StartTime)

	def get_Per(self):
		return self.get_query_params().get('Per')

	def set_Per(self,Per):
		self.add_query_param('Per',Per)

	def get_Bid(self):
		return self.get_query_params().get('Bid')

	def set_Bid(self,Bid):
		self.add_query_param('Bid',Bid)