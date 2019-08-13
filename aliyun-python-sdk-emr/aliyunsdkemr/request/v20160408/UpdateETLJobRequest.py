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

class UpdateETLJobRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Emr', '2016-04-08', 'UpdateETLJob','emr')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_ClusterConfig(self):
		return self.get_query_params().get('ClusterConfig')

	def set_ClusterConfig(self,ClusterConfig):
		self.add_query_param('ClusterConfig',ClusterConfig)

	def get_TriggerRules(self):
		return self.get_query_params().get('TriggerRules')

	def set_TriggerRules(self,TriggerRules):
		for i in range(len(TriggerRules)):	
			if TriggerRules[i].get('CronExpr') is not None:
				self.add_query_param('TriggerRule.' + str(i + 1) + '.CronExpr' , TriggerRules[i].get('CronExpr'))
			if TriggerRules[i].get('EndTime') is not None:
				self.add_query_param('TriggerRule.' + str(i + 1) + '.EndTime' , TriggerRules[i].get('EndTime'))
			if TriggerRules[i].get('StartTime') is not None:
				self.add_query_param('TriggerRule.' + str(i + 1) + '.StartTime' , TriggerRules[i].get('StartTime'))
			if TriggerRules[i].get('Enabled') is not None:
				self.add_query_param('TriggerRule.' + str(i + 1) + '.Enabled' , TriggerRules[i].get('Enabled'))


	def get_AlertConfig(self):
		return self.get_query_params().get('AlertConfig')

	def set_AlertConfig(self,AlertConfig):
		self.add_query_param('AlertConfig',AlertConfig)

	def get_Description(self):
		return self.get_query_params().get('Description')

	def set_Description(self,Description):
		self.add_query_param('Description',Description)

	def get_Check(self):
		return self.get_query_params().get('Check')

	def set_Check(self,Check):
		self.add_query_param('Check',Check)

	def get_StageConnections(self):
		return self.get_query_params().get('StageConnections')

	def set_StageConnections(self,StageConnections):
		for i in range(len(StageConnections)):	
			if StageConnections[i].get('Port') is not None:
				self.add_query_param('StageConnection.' + str(i + 1) + '.Port' , StageConnections[i].get('Port'))
			if StageConnections[i].get('From') is not None:
				self.add_query_param('StageConnection.' + str(i + 1) + '.From' , StageConnections[i].get('From'))
			if StageConnections[i].get('To') is not None:
				self.add_query_param('StageConnection.' + str(i + 1) + '.To' , StageConnections[i].get('To'))


	def get_Stages(self):
		return self.get_query_params().get('Stages')

	def set_Stages(self,Stages):
		for i in range(len(Stages)):	
			if Stages[i].get('StageName') is not None:
				self.add_query_param('Stage.' + str(i + 1) + '.StageName' , Stages[i].get('StageName'))
			if Stages[i].get('StageConf') is not None:
				self.add_query_param('Stage.' + str(i + 1) + '.StageConf' , Stages[i].get('StageConf'))
			if Stages[i].get('StageType') is not None:
				self.add_query_param('Stage.' + str(i + 1) + '.StageType' , Stages[i].get('StageType'))
			if Stages[i].get('StagePlugin') is not None:
				self.add_query_param('Stage.' + str(i + 1) + '.StagePlugin' , Stages[i].get('StagePlugin'))


	def get_Name(self):
		return self.get_query_params().get('Name')

	def set_Name(self,Name):
		self.add_query_param('Name',Name)

	def get_Id(self):
		return self.get_query_params().get('Id')

	def set_Id(self,Id):
		self.add_query_param('Id',Id)