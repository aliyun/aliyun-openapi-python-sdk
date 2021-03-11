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
from aliyunsdkpolardb.endpoint import endpoint_data

class DescribeSQLLogTemplatesRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'polardb', '2017-08-01', 'DescribeSQLLogTemplates','polardb')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_StartTime(self):
		return self.get_query_params().get('StartTime')

	def set_StartTime(self,StartTime):
		self.add_query_param('StartTime',StartTime)

	def get_JobId(self):
		return self.get_query_params().get('JobId')

	def set_JobId(self,JobId):
		self.add_query_param('JobId',JobId)

	def get_SortKey(self):
		return self.get_query_params().get('SortKey')

	def set_SortKey(self,SortKey):
		self.add_query_param('SortKey',SortKey)

	def get_MinAvgScanRows(self):
		return self.get_query_params().get('MinAvgScanRows')

	def set_MinAvgScanRows(self,MinAvgScanRows):
		self.add_query_param('MinAvgScanRows',MinAvgScanRows)

	def get_SecurityToken(self):
		return self.get_query_params().get('SecurityToken')

	def set_SecurityToken(self,SecurityToken):
		self.add_query_param('SecurityToken',SecurityToken)

	def get_PageNumbers(self):
		return self.get_query_params().get('PageNumbers')

	def set_PageNumbers(self,PageNumbers):
		self.add_query_param('PageNumbers',PageNumbers)

	def get_PagingId(self):
		return self.get_query_params().get('PagingId')

	def set_PagingId(self,PagingId):
		self.add_query_param('PagingId',PagingId)

	def get_DBInstanceId(self):
		return self.get_query_params().get('DBInstanceId')

	def set_DBInstanceId(self,DBInstanceId):
		self.add_query_param('DBInstanceId',DBInstanceId)

	def get_MaxAvgScanRows(self):
		return self.get_query_params().get('MaxAvgScanRows')

	def set_MaxAvgScanRows(self,MaxAvgScanRows):
		self.add_query_param('MaxAvgScanRows',MaxAvgScanRows)

	def get_SqlType(self):
		return self.get_query_params().get('SqlType')

	def set_SqlType(self,SqlType):
		self.add_query_param('SqlType',SqlType)

	def get_ResourceOwnerAccount(self):
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self,ResourceOwnerAccount):
		self.add_query_param('ResourceOwnerAccount',ResourceOwnerAccount)

	def get_MinAvgConsume(self):
		return self.get_query_params().get('MinAvgConsume')

	def set_MinAvgConsume(self,MinAvgConsume):
		self.add_query_param('MinAvgConsume',MinAvgConsume)

	def get_OwnerAccount(self):
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self,OwnerAccount):
		self.add_query_param('OwnerAccount',OwnerAccount)

	def get_MaxRecordsPerPage(self):
		return self.get_query_params().get('MaxRecordsPerPage')

	def set_MaxRecordsPerPage(self,MaxRecordsPerPage):
		self.add_query_param('MaxRecordsPerPage',MaxRecordsPerPage)

	def get_EndTime(self):
		return self.get_query_params().get('EndTime')

	def set_EndTime(self,EndTime):
		self.add_query_param('EndTime',EndTime)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_MaxAvgConsume(self):
		return self.get_query_params().get('MaxAvgConsume')

	def set_MaxAvgConsume(self,MaxAvgConsume):
		self.add_query_param('MaxAvgConsume',MaxAvgConsume)

	def get_ChildDBInstanceIDs(self):
		return self.get_query_params().get('ChildDBInstanceIDs')

	def set_ChildDBInstanceIDs(self,ChildDBInstanceIDs):
		self.add_query_param('ChildDBInstanceIDs',ChildDBInstanceIDs)

	def get_SortMethod(self):
		return self.get_query_params().get('SortMethod')

	def set_SortMethod(self,SortMethod):
		self.add_query_param('SortMethod',SortMethod)