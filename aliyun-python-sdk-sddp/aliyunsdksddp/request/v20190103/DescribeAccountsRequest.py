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
from aliyunsdksddp.endpoint import endpoint_data

class DescribeAccountsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Sddp', '2019-01-03', 'DescribeAccounts')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ProductCode(self):
		return self.get_query_params().get('ProductCode')

	def set_ProductCode(self,ProductCode):
		self.add_query_param('ProductCode',ProductCode)

	def get_PackageId(self):
		return self.get_query_params().get('PackageId')

	def set_PackageId(self,PackageId):
		self.add_query_param('PackageId',PackageId)

	def get_PageSize(self):
		return self.get_query_params().get('PageSize')

	def set_PageSize(self,PageSize):
		self.add_query_param('PageSize',PageSize)

	def get_TableId(self):
		return self.get_query_params().get('TableId')

	def set_TableId(self,TableId):
		self.add_query_param('TableId',TableId)

	def get_Lang(self):
		return self.get_query_params().get('Lang')

	def set_Lang(self,Lang):
		self.add_query_param('Lang',Lang)

	def get_Key(self):
		return self.get_query_params().get('Key')

	def set_Key(self,Key):
		self.add_query_param('Key',Key)

	def get_QueryType(self):
		return self.get_query_params().get('QueryType')

	def set_QueryType(self,QueryType):
		self.add_query_param('QueryType',QueryType)

	def get_LoginName(self):
		return self.get_query_params().get('LoginName')

	def set_LoginName(self,LoginName):
		self.add_query_param('LoginName',LoginName)

	def get_FeatureType(self):
		return self.get_query_params().get('FeatureType')

	def set_FeatureType(self,FeatureType):
		self.add_query_param('FeatureType',FeatureType)

	def get_ColumnId(self):
		return self.get_query_params().get('ColumnId')

	def set_ColumnId(self,ColumnId):
		self.add_query_param('ColumnId',ColumnId)

	def get_CurrentPage(self):
		return self.get_query_params().get('CurrentPage')

	def set_CurrentPage(self,CurrentPage):
		self.add_query_param('CurrentPage',CurrentPage)

	def get_InstanceId(self):
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self,InstanceId):
		self.add_query_param('InstanceId',InstanceId)

	def get_DepartId(self):
		return self.get_query_params().get('DepartId')

	def set_DepartId(self,DepartId):
		self.add_query_param('DepartId',DepartId)

	def get_OperationId(self):
		return self.get_query_params().get('OperationId')

	def set_OperationId(self,OperationId):
		self.add_query_param('OperationId',OperationId)