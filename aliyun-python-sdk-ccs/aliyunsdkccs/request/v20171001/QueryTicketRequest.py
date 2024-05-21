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
class QueryTicketRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ccs', '2017-10-01', 'QueryTicket','ccs')

	def get_Stage(self):
		return self.get_query_params().get('Stage')

	def set_Stage(self,Stage):
		self.add_query_param('Stage',Stage)

	def get_PageSize(self):
		return self.get_query_params().get('PageSize')

	def set_PageSize(self,PageSize):
		self.add_query_param('PageSize',PageSize)

	def get_CreatorId(self):
		return self.get_query_params().get('CreatorId')

	def set_CreatorId(self,CreatorId):
		self.add_query_param('CreatorId',CreatorId)

	def get_EndTime(self):
		return self.get_query_params().get('EndTime')

	def set_EndTime(self,EndTime):
		self.add_query_param('EndTime',EndTime)

	def get_StartTime(self):
		return self.get_query_params().get('StartTime')

	def set_StartTime(self,StartTime):
		self.add_query_param('StartTime',StartTime)

	def get_PageNum(self):
		return self.get_query_params().get('PageNum')

	def set_PageNum(self,PageNum):
		self.add_query_param('PageNum',PageNum)

	def get_Type(self):
		return self.get_query_params().get('Type')

	def set_Type(self,Type):
		self.add_query_param('Type',Type)

	def get_CcsInstanceId(self):
		return self.get_query_params().get('CcsInstanceId')

	def set_CcsInstanceId(self,CcsInstanceId):
		self.add_query_param('CcsInstanceId',CcsInstanceId)