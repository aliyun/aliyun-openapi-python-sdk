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
from aliyunsdkgpdb.endpoint import endpoint_data

class DescribeSlowSQLLogsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'gpdb', '2016-05-03', 'DescribeSlowSQLLogs','gpdb')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_StartTime(self):
		return self.get_query_params().get('StartTime')

	def set_StartTime(self,StartTime):
		self.add_query_param('StartTime',StartTime)

	def get_QueryKeywords(self):
		return self.get_query_params().get('QueryKeywords')

	def set_QueryKeywords(self,QueryKeywords):
		self.add_query_param('QueryKeywords',QueryKeywords)

	def get_PageNumber(self):
		return self.get_query_params().get('PageNumber')

	def set_PageNumber(self,PageNumber):
		self.add_query_param('PageNumber',PageNumber)

	def get_Database(self):
		return self.get_query_params().get('Database')

	def set_Database(self,Database):
		self.add_query_param('Database',Database)

	def get_SourceIP(self):
		return self.get_query_params().get('SourceIP')

	def set_SourceIP(self,SourceIP):
		self.add_query_param('SourceIP',SourceIP)

	def get_MinExecuteCost(self):
		return self.get_query_params().get('MinExecuteCost')

	def set_MinExecuteCost(self,MinExecuteCost):
		self.add_query_param('MinExecuteCost',MinExecuteCost)

	def get_PageSize(self):
		return self.get_query_params().get('PageSize')

	def set_PageSize(self,PageSize):
		self.add_query_param('PageSize',PageSize)

	def get_DBInstanceId(self):
		return self.get_query_params().get('DBInstanceId')

	def set_DBInstanceId(self,DBInstanceId):
		self.add_query_param('DBInstanceId',DBInstanceId)

	def get_MaxExecuteCost(self):
		return self.get_query_params().get('MaxExecuteCost')

	def set_MaxExecuteCost(self,MaxExecuteCost):
		self.add_query_param('MaxExecuteCost',MaxExecuteCost)

	def get_ExecuteState(self):
		return self.get_query_params().get('ExecuteState')

	def set_ExecuteState(self,ExecuteState):
		self.add_query_param('ExecuteState',ExecuteState)

	def get_EndTime(self):
		return self.get_query_params().get('EndTime')

	def set_EndTime(self,EndTime):
		self.add_query_param('EndTime',EndTime)

	def get_OperationType(self):
		return self.get_query_params().get('OperationType')

	def set_OperationType(self,OperationType):
		self.add_query_param('OperationType',OperationType)

	def get_OperationClass(self):
		return self.get_query_params().get('OperationClass')

	def set_OperationClass(self,OperationClass):
		self.add_query_param('OperationClass',OperationClass)

	def get_User(self):
		return self.get_query_params().get('User')

	def set_User(self,User):
		self.add_query_param('User',User)