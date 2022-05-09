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

class CreateFlowForWebRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Emr', '2016-04-08', 'CreateFlowForWeb','emr')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_CronExpr(self):
		return self.get_query_params().get('CronExpr')

	def set_CronExpr(self,CronExpr):
		self.add_query_param('CronExpr',CronExpr)

	def get_Description(self):
		return self.get_query_params().get('Description')

	def set_Description(self,Description):
		self.add_query_param('Description',Description)

	def get_AlertUserGroupBizId(self):
		return self.get_query_params().get('AlertUserGroupBizId')

	def set_AlertUserGroupBizId(self,AlertUserGroupBizId):
		self.add_query_param('AlertUserGroupBizId',AlertUserGroupBizId)

	def get_Lifecycle(self):
		return self.get_query_params().get('Lifecycle')

	def set_Lifecycle(self,Lifecycle):
		self.add_query_param('Lifecycle',Lifecycle)

	def get_HostName(self):
		return self.get_query_params().get('HostName')

	def set_HostName(self,HostName):
		self.add_query_param('HostName',HostName)

	def get_CreateCluster(self):
		return self.get_query_params().get('CreateCluster')

	def set_CreateCluster(self,CreateCluster):
		self.add_query_param('CreateCluster',CreateCluster)

	def get_EndSchedule(self):
		return self.get_query_params().get('EndSchedule')

	def set_EndSchedule(self,EndSchedule):
		self.add_query_param('EndSchedule',EndSchedule)

	def get_AlertConf(self):
		return self.get_query_params().get('AlertConf')

	def set_AlertConf(self,AlertConf):
		self.add_query_param('AlertConf',AlertConf)

	def get_ProjectId(self):
		return self.get_query_params().get('ProjectId')

	def set_ProjectId(self,ProjectId):
		self.add_query_param('ProjectId',ProjectId)

	def get_ParentFlowList(self):
		return self.get_query_params().get('ParentFlowList')

	def set_ParentFlowList(self,ParentFlowList):
		self.add_query_param('ParentFlowList',ParentFlowList)

	def get_LogArchiveLocation(self):
		return self.get_query_params().get('LogArchiveLocation')

	def set_LogArchiveLocation(self,LogArchiveLocation):
		self.add_query_param('LogArchiveLocation',LogArchiveLocation)

	def get_AlertDingDingGroupBizId(self):
		return self.get_query_params().get('AlertDingDingGroupBizId')

	def set_AlertDingDingGroupBizId(self,AlertDingDingGroupBizId):
		self.add_query_param('AlertDingDingGroupBizId',AlertDingDingGroupBizId)

	def get_StartSchedule(self):
		return self.get_query_params().get('StartSchedule')

	def set_StartSchedule(self,StartSchedule):
		self.add_query_param('StartSchedule',StartSchedule)

	def get_ClusterId(self):
		return self.get_query_params().get('ClusterId')

	def set_ClusterId(self,ClusterId):
		self.add_query_param('ClusterId',ClusterId)

	def get_Graph(self):
		return self.get_query_params().get('Graph')

	def set_Graph(self,Graph):
		self.add_query_param('Graph',Graph)

	def get_Name(self):
		return self.get_query_params().get('Name')

	def set_Name(self,Name):
		self.add_query_param('Name',Name)

	def get_Namespace(self):
		return self.get_query_params().get('Namespace')

	def set_Namespace(self,Namespace):
		self.add_query_param('Namespace',Namespace)

	def get_ParentCategory(self):
		return self.get_query_params().get('ParentCategory')

	def set_ParentCategory(self,ParentCategory):
		self.add_query_param('ParentCategory',ParentCategory)