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

class DescribeWorkflowRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ens', '2017-11-10', 'DescribeWorkflow','ens')
		self.set_method('POST')

	def get_PageNum(self): # String
		return self.get_query_params().get('PageNum')

	def set_PageNum(self, PageNum):  # String
		self.add_query_param('PageNum', PageNum)
	def get_StartDate(self): # String
		return self.get_query_params().get('StartDate')

	def set_StartDate(self, StartDate):  # String
		self.add_query_param('StartDate', StartDate)
	def get_EnsRegionId(self): # String
		return self.get_query_params().get('EnsRegionId')

	def set_EnsRegionId(self, EnsRegionId):  # String
		self.add_query_param('EnsRegionId', EnsRegionId)
	def get_Id(self): # String
		return self.get_query_params().get('Id')

	def set_Id(self, Id):  # String
		self.add_query_param('Id', Id)
	def get_WorkFlowId(self): # String
		return self.get_query_params().get('WorkFlowId')

	def set_WorkFlowId(self, WorkFlowId):  # String
		self.add_query_param('WorkFlowId', WorkFlowId)
	def get_BusinessId(self): # String
		return self.get_query_params().get('BusinessId')

	def set_BusinessId(self, BusinessId):  # String
		self.add_query_param('BusinessId', BusinessId)
	def get_InstanceId(self): # String
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self, InstanceId):  # String
		self.add_query_param('InstanceId', InstanceId)
	def get_EndDate(self): # String
		return self.get_query_params().get('EndDate')

	def set_EndDate(self, EndDate):  # String
		self.add_query_param('EndDate', EndDate)
	def get_Status(self): # String
		return self.get_query_params().get('Status')

	def set_Status(self, Status):  # String
		self.add_query_param('Status', Status)
	def get_WorkFlowName(self): # String
		return self.get_query_params().get('WorkFlowName')

	def set_WorkFlowName(self, WorkFlowName):  # String
		self.add_query_param('WorkFlowName', WorkFlowName)
	def get_PageSize(self): # String
		return self.get_query_params().get('PageSize')

	def set_PageSize(self, PageSize):  # String
		self.add_query_param('PageSize', PageSize)
	def get_AliUid(self): # String
		return self.get_query_params().get('AliUid')

	def set_AliUid(self, AliUid):  # String
		self.add_query_param('AliUid', AliUid)
