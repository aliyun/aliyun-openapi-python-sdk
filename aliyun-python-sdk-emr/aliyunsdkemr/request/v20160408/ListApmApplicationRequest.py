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

class ListApmApplicationRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Emr', '2016-04-08', 'ListApmApplication','emr')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_PageNumber(self):
		return self.get_query_params().get('PageNumber')

	def set_PageNumber(self,PageNumber):
		self.add_query_param('PageNumber',PageNumber)

	def get_FinalStatus(self):
		return self.get_query_params().get('FinalStatus')

	def set_FinalStatus(self,FinalStatus):
		self.add_query_param('FinalStatus',FinalStatus)

	def get_PageSize(self):
		return self.get_query_params().get('PageSize')

	def set_PageSize(self,PageSize):
		self.add_query_param('PageSize',PageSize)

	def get_State(self):
		return self.get_query_params().get('State')

	def set_State(self,State):
		self.add_query_param('State',State)

	def get_StartTimeTo(self):
		return self.get_query_params().get('StartTimeTo')

	def set_StartTimeTo(self,StartTimeTo):
		self.add_query_param('StartTimeTo',StartTimeTo)

	def get_DiagnoseResult(self):
		return self.get_query_params().get('DiagnoseResult')

	def set_DiagnoseResult(self,DiagnoseResult):
		self.add_query_param('DiagnoseResult',DiagnoseResult)

	def get_EndTimeFrom(self):
		return self.get_query_params().get('EndTimeFrom')

	def set_EndTimeFrom(self,EndTimeFrom):
		self.add_query_param('EndTimeFrom',EndTimeFrom)

	def get_OrderBy(self):
		return self.get_query_params().get('OrderBy')

	def set_OrderBy(self,OrderBy):
		self.add_query_param('OrderBy',OrderBy)

	def get_ClusterId(self):
		return self.get_query_params().get('ClusterId')

	def set_ClusterId(self,ClusterId):
		self.add_query_param('ClusterId',ClusterId)

	def get_JobType(self):
		return self.get_query_params().get('JobType')

	def set_JobType(self,JobType):
		self.add_query_param('JobType',JobType)

	def get_StartTimeFrom(self):
		return self.get_query_params().get('StartTimeFrom')

	def set_StartTimeFrom(self,StartTimeFrom):
		self.add_query_param('StartTimeFrom',StartTimeFrom)

	def get_AppId(self):
		return self.get_query_params().get('AppId')

	def set_AppId(self,AppId):
		self.add_query_param('AppId',AppId)

	def get_Name(self):
		return self.get_query_params().get('Name')

	def set_Name(self,Name):
		self.add_query_param('Name',Name)

	def get_User(self):
		return self.get_query_params().get('User')

	def set_User(self,User):
		self.add_query_param('User',User)

	def get_EndTimeTo(self):
		return self.get_query_params().get('EndTimeTo')

	def set_EndTimeTo(self,EndTimeTo):
		self.add_query_param('EndTimeTo',EndTimeTo)

	def get_Queue(self):
		return self.get_query_params().get('Queue')

	def set_Queue(self,Queue):
		self.add_query_param('Queue',Queue)