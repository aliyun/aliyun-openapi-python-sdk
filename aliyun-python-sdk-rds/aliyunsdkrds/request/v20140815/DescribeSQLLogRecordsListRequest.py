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
class DescribeSQLLogRecordsListRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Rds', '2014-08-15', 'DescribeSQLLogRecordsList','rds')

	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_MinScanRows(self):
		return self.get_query_params().get('MinScanRows')

	def set_MinScanRows(self,MinScanRows):
		self.add_query_param('MinScanRows',MinScanRows)

	def get_StartTime(self):
		return self.get_query_params().get('StartTime')

	def set_StartTime(self,StartTime):
		self.add_query_param('StartTime',StartTime)

	def get_HostAddress(self):
		return self.get_query_params().get('HostAddress')

	def set_HostAddress(self,HostAddress):
		self.add_query_param('HostAddress',HostAddress)

	def get_SortKey(self):
		return self.get_query_params().get('SortKey')

	def set_SortKey(self,SortKey):
		self.add_query_param('SortKey',SortKey)

	def get_AccountName(self):
		return self.get_query_params().get('AccountName')

	def set_AccountName(self,AccountName):
		self.add_query_param('AccountName',AccountName)

	def get_SecurityToken(self):
		return self.get_query_params().get('SecurityToken')

	def set_SecurityToken(self,SecurityToken):
		self.add_query_param('SecurityToken',SecurityToken)

	def get_PageNumbers(self):
		return self.get_query_params().get('PageNumbers')

	def set_PageNumbers(self,PageNumbers):
		self.add_query_param('PageNumbers',PageNumbers)

	def get_PagingID(self):
		return self.get_query_params().get('PagingID')

	def set_PagingID(self,PagingID):
		self.add_query_param('PagingID',PagingID)

	def get_DBInstanceId(self):
		return self.get_query_params().get('DBInstanceId')

	def set_DBInstanceId(self,DBInstanceId):
		self.add_query_param('DBInstanceId',DBInstanceId)

	def get_State(self):
		return self.get_query_params().get('State')

	def set_State(self,State):
		self.add_query_param('State',State)

	def get_TableName(self):
		return self.get_query_params().get('TableName')

	def set_TableName(self,TableName):
		self.add_query_param('TableName',TableName)

	def get_SqlType(self):
		return self.get_query_params().get('SqlType')

	def set_SqlType(self,SqlType):
		self.add_query_param('SqlType',SqlType)

	def get_MinConsume(self):
		return self.get_query_params().get('MinConsume')

	def set_MinConsume(self,MinConsume):
		self.add_query_param('MinConsume',MinConsume)

	def get_ResourceOwnerAccount(self):
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self,ResourceOwnerAccount):
		self.add_query_param('ResourceOwnerAccount',ResourceOwnerAccount)

	def get_OwnerAccount(self):
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self,OwnerAccount):
		self.add_query_param('OwnerAccount',OwnerAccount)

	def get_MaxRecordsPerPage(self):
		return self.get_query_params().get('MaxRecordsPerPage')

	def set_MaxRecordsPerPage(self,MaxRecordsPerPage):
		self.add_query_param('MaxRecordsPerPage',MaxRecordsPerPage)

	def get_QueryKeyword(self):
		return self.get_query_params().get('QueryKeyword')

	def set_QueryKeyword(self,QueryKeyword):
		self.add_query_param('QueryKeyword',QueryKeyword)

	def get_EndTime(self):
		return self.get_query_params().get('EndTime')

	def set_EndTime(self,EndTime):
		self.add_query_param('EndTime',EndTime)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_MaxConsume(self):
		return self.get_query_params().get('MaxConsume')

	def set_MaxConsume(self,MaxConsume):
		self.add_query_param('MaxConsume',MaxConsume)

	def get_ThreadID(self):
		return self.get_query_params().get('ThreadID')

	def set_ThreadID(self,ThreadID):
		self.add_query_param('ThreadID',ThreadID)

	def get_DBName(self):
		return self.get_query_params().get('DBName')

	def set_DBName(self,DBName):
		self.add_query_param('DBName',DBName)

	def get_SortMethod(self):
		return self.get_query_params().get('SortMethod')

	def set_SortMethod(self,SortMethod):
		self.add_query_param('SortMethod',SortMethod)

	def get_MaxScanRows(self):
		return self.get_query_params().get('MaxScanRows')

	def set_MaxScanRows(self,MaxScanRows):
		self.add_query_param('MaxScanRows',MaxScanRows)