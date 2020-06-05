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
from aliyunsdkemr.endpoint import endpoint_data

class ListBackupsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Emr', '2016-04-08', 'ListBackups','emr')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_PageCount(self):
		return self.get_query_params().get('PageCount')

	def set_PageCount(self,PageCount):
		self.add_query_param('PageCount',PageCount)

	def get_OrderMode(self):
		return self.get_query_params().get('OrderMode')

	def set_OrderMode(self,OrderMode):
		self.add_query_param('OrderMode',OrderMode)

	def get_BackupPlanId(self):
		return self.get_query_params().get('BackupPlanId')

	def set_BackupPlanId(self,BackupPlanId):
		self.add_query_param('BackupPlanId',BackupPlanId)

	def get_PageNumber(self):
		return self.get_query_params().get('PageNumber')

	def set_PageNumber(self,PageNumber):
		self.add_query_param('PageNumber',PageNumber)

	def get_Limit(self):
		return self.get_query_params().get('Limit')

	def set_Limit(self,Limit):
		self.add_query_param('Limit',Limit)

	def get_PageSize(self):
		return self.get_query_params().get('PageSize')

	def set_PageSize(self,PageSize):
		self.add_query_param('PageSize',PageSize)

	def get_ServiceName(self):
		return self.get_query_params().get('ServiceName')

	def set_ServiceName(self,ServiceName):
		self.add_query_param('ServiceName',ServiceName)

	def get_Id(self):
		return self.get_query_params().get('Id')

	def set_Id(self,Id):
		self.add_query_param('Id',Id)

	def get_CurrentSize(self):
		return self.get_query_params().get('CurrentSize')

	def set_CurrentSize(self,CurrentSize):
		self.add_query_param('CurrentSize',CurrentSize)

	def get_BackupIds(self):
		return self.get_query_params().get('BackupIds')

	def set_BackupIds(self, BackupIds):
		for depth1 in range(len(BackupIds)):
			if BackupIds[depth1] is not None:
				self.add_query_param('BackupId.' + str(depth1 + 1) , BackupIds[depth1])

	def get_ClusterId(self):
		return self.get_query_params().get('ClusterId')

	def set_ClusterId(self,ClusterId):
		self.add_query_param('ClusterId',ClusterId)

	def get_MetadataType(self):
		return self.get_query_params().get('MetadataType')

	def set_MetadataType(self,MetadataType):
		self.add_query_param('MetadataType',MetadataType)

	def get_BizId(self):
		return self.get_query_params().get('BizId')

	def set_BizId(self,BizId):
		self.add_query_param('BizId',BizId)

	def get_Status(self):
		return self.get_query_params().get('Status')

	def set_Status(self,Status):
		self.add_query_param('Status',Status)