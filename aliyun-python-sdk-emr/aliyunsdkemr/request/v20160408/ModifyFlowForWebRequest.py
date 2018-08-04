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
class ModifyFlowForWebRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Emr', '2016-04-08', 'ModifyFlowForWeb')

	def get_CronExpr(self):
		return self.get_query_params().get('CronExpr')

	def set_CronExpr(self,CronExpr):
		self.add_query_param('CronExpr',CronExpr)

	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_Periodic(self):
		return self.get_query_params().get('Periodic')

	def set_Periodic(self,Periodic):
		self.add_query_param('Periodic',Periodic)

	def get_StartSchedule(self):
		return self.get_query_params().get('StartSchedule')

	def set_StartSchedule(self,StartSchedule):
		self.add_query_param('StartSchedule',StartSchedule)

	def get_Description(self):
		return self.get_query_params().get('Description')

	def set_Description(self,Description):
		self.add_query_param('Description',Description)

	def get_ClusterId(self):
		return self.get_query_params().get('ClusterId')

	def set_ClusterId(self,ClusterId):
		self.add_query_param('ClusterId',ClusterId)

	def get_Graph(self):
		return self.get_query_params().get('Graph')

	def set_Graph(self,Graph):
		self.add_query_param('Graph',Graph)

	def get_CreateCluster(self):
		return self.get_query_params().get('CreateCluster')

	def set_CreateCluster(self,CreateCluster):
		self.add_query_param('CreateCluster',CreateCluster)

	def get_Name(self):
		return self.get_query_params().get('Name')

	def set_Name(self,Name):
		self.add_query_param('Name',Name)

	def get_EndSchedule(self):
		return self.get_query_params().get('EndSchedule')

	def set_EndSchedule(self,EndSchedule):
		self.add_query_param('EndSchedule',EndSchedule)

	def get_Id(self):
		return self.get_query_params().get('Id')

	def set_Id(self,Id):
		self.add_query_param('Id',Id)

	def get_ProjectId(self):
		return self.get_query_params().get('ProjectId')

	def set_ProjectId(self,ProjectId):
		self.add_query_param('ProjectId',ProjectId)

	def get_Status(self):
		return self.get_query_params().get('Status')

	def set_Status(self,Status):
		self.add_query_param('Status',Status)

	def get_ParentCategory(self):
		return self.get_query_params().get('ParentCategory')

	def set_ParentCategory(self,ParentCategory):
		self.add_query_param('ParentCategory',ParentCategory)