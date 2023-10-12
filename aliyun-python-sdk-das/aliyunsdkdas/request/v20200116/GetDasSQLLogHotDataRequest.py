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
from aliyunsdkdas.endpoint import endpoint_data

class GetDasSQLLogHotDataRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'DAS', '2020-01-16', 'GetDasSQLLogHotData')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_InstanceId(self): # String
		return self.get_body_params().get('InstanceId')

	def set_InstanceId(self, InstanceId):  # String
		self.add_body_params('InstanceId', InstanceId)
	def get_Start(self): # Long
		return self.get_body_params().get('Start')

	def set_Start(self, Start):  # Long
		self.add_body_params('Start', Start)
	def get_End(self): # Long
		return self.get_body_params().get('End')

	def set_End(self, End):  # Long
		self.add_body_params('End', End)
	def get_QueryKeyword(self): # String
		return self.get_body_params().get('QueryKeyword')

	def set_QueryKeyword(self, QueryKeyword):  # String
		self.add_body_params('QueryKeyword', QueryKeyword)
	def get_AccountName(self): # String
		return self.get_body_params().get('AccountName')

	def set_AccountName(self, AccountName):  # String
		self.add_body_params('AccountName', AccountName)
	def get_DBName(self): # String
		return self.get_body_params().get('DBName')

	def set_DBName(self, DBName):  # String
		self.add_body_params('DBName', DBName)
	def get_HostAddress(self): # String
		return self.get_body_params().get('HostAddress')

	def set_HostAddress(self, HostAddress):  # String
		self.add_body_params('HostAddress', HostAddress)
	def get_LogicalOperator(self): # String
		return self.get_body_params().get('LogicalOperator')

	def set_LogicalOperator(self, LogicalOperator):  # String
		self.add_body_params('LogicalOperator', LogicalOperator)
	def get_MaxLatancy(self): # Long
		return self.get_body_params().get('MaxLatancy')

	def set_MaxLatancy(self, MaxLatancy):  # Long
		self.add_body_params('MaxLatancy', MaxLatancy)
	def get_MaxScanRows(self): # Long
		return self.get_body_params().get('MaxScanRows')

	def set_MaxScanRows(self, MaxScanRows):  # Long
		self.add_body_params('MaxScanRows', MaxScanRows)
	def get_MinLatancy(self): # Long
		return self.get_body_params().get('MinLatancy')

	def set_MinLatancy(self, MinLatancy):  # Long
		self.add_body_params('MinLatancy', MinLatancy)
	def get_MinScanRows(self): # Long
		return self.get_body_params().get('MinScanRows')

	def set_MinScanRows(self, MinScanRows):  # Long
		self.add_body_params('MinScanRows', MinScanRows)
	def get_SqlType(self): # String
		return self.get_body_params().get('SqlType')

	def set_SqlType(self, SqlType):  # String
		self.add_body_params('SqlType', SqlType)
	def get_State(self): # String
		return self.get_body_params().get('State')

	def set_State(self, State):  # String
		self.add_body_params('State', State)
	def get_ThreadID(self): # String
		return self.get_body_params().get('ThreadID')

	def set_ThreadID(self, ThreadID):  # String
		self.add_body_params('ThreadID', ThreadID)
	def get_PageNumbers(self): # Long
		return self.get_body_params().get('PageNumbers')

	def set_PageNumbers(self, PageNumbers):  # Long
		self.add_body_params('PageNumbers', PageNumbers)
	def get_MaxRecordsPerPage(self): # Long
		return self.get_body_params().get('MaxRecordsPerPage')

	def set_MaxRecordsPerPage(self, MaxRecordsPerPage):  # Long
		self.add_body_params('MaxRecordsPerPage', MaxRecordsPerPage)
	def get_SortKey(self): # String
		return self.get_body_params().get('SortKey')

	def set_SortKey(self, SortKey):  # String
		self.add_body_params('SortKey', SortKey)
	def get_SortMethod(self): # String
		return self.get_body_params().get('SortMethod')

	def set_SortMethod(self, SortMethod):  # String
		self.add_body_params('SortMethod', SortMethod)
	def get_ChildDBInstanceIDs(self): # String
		return self.get_body_params().get('ChildDBInstanceIDs')

	def set_ChildDBInstanceIDs(self, ChildDBInstanceIDs):  # String
		self.add_body_params('ChildDBInstanceIDs', ChildDBInstanceIDs)
	def get_Role(self): # String
		return self.get_body_params().get('Role')

	def set_Role(self, Role):  # String
		self.add_body_params('Role', Role)
	def get_TraceId(self): # String
		return self.get_body_params().get('TraceId')

	def set_TraceId(self, TraceId):  # String
		self.add_body_params('TraceId', TraceId)
	def get_MinRows(self): # Long
		return self.get_body_params().get('MinRows')

	def set_MinRows(self, MinRows):  # Long
		self.add_body_params('MinRows', MinRows)
	def get_MaxRows(self): # Long
		return self.get_body_params().get('MaxRows')

	def set_MaxRows(self, MaxRows):  # Long
		self.add_body_params('MaxRows', MaxRows)
	def get_MinSpillCnt(self): # Long
		return self.get_body_params().get('MinSpillCnt')

	def set_MinSpillCnt(self, MinSpillCnt):  # Long
		self.add_body_params('MinSpillCnt', MinSpillCnt)
	def get_MaxSpillCnt(self): # Long
		return self.get_body_params().get('MaxSpillCnt')

	def set_MaxSpillCnt(self, MaxSpillCnt):  # Long
		self.add_body_params('MaxSpillCnt', MaxSpillCnt)
	def get_TransactionId(self): # String
		return self.get_body_params().get('TransactionId')

	def set_TransactionId(self, TransactionId):  # String
		self.add_body_params('TransactionId', TransactionId)
	def get_Fail(self): # String
		return self.get_body_params().get('Fail')

	def set_Fail(self, Fail):  # String
		self.add_body_params('Fail', Fail)
