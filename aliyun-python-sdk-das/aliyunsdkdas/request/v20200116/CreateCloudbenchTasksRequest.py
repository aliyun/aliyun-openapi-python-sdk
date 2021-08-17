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

class CreateCloudbenchTasksRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'DAS', '2020-01-16', 'CreateCloudbenchTasks','das')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ClientType(self):
		return self.get_query_params().get('ClientType')

	def set_ClientType(self,ClientType):
		self.add_query_param('ClientType',ClientType)

	def get_DstPort(self):
		return self.get_query_params().get('DstPort')

	def set_DstPort(self,DstPort):
		self.add_query_param('DstPort',DstPort)

	def get_Description(self):
		return self.get_query_params().get('Description')

	def set_Description(self,Description):
		self.add_query_param('Description',Description)

	def get_RequestStartTime(self):
		return self.get_query_params().get('RequestStartTime')

	def set_RequestStartTime(self,RequestStartTime):
		self.add_query_param('RequestStartTime',RequestStartTime)

	def get_DstConnectionString(self):
		return self.get_query_params().get('DstConnectionString')

	def set_DstConnectionString(self,DstConnectionString):
		self.add_query_param('DstConnectionString',DstConnectionString)

	def get_DstSuperPassword(self):
		return self.get_query_params().get('DstSuperPassword')

	def set_DstSuperPassword(self,DstSuperPassword):
		self.add_query_param('DstSuperPassword',DstSuperPassword)

	def get_DstSuperAccount(self):
		return self.get_query_params().get('DstSuperAccount')

	def set_DstSuperAccount(self,DstSuperAccount):
		self.add_query_param('DstSuperAccount',DstSuperAccount)

	def get_DstInstanceId(self):
		return self.get_query_params().get('DstInstanceId')

	def set_DstInstanceId(self,DstInstanceId):
		self.add_query_param('DstInstanceId',DstInstanceId)

	def get_Rate(self):
		return self.get_query_params().get('Rate')

	def set_Rate(self,Rate):
		self.add_query_param('Rate',Rate)

	def get_RequestDuration(self):
		return self.get_query_params().get('RequestDuration')

	def set_RequestDuration(self,RequestDuration):
		self.add_query_param('RequestDuration',RequestDuration)

	def get_DtsJobId(self):
		return self.get_query_params().get('DtsJobId')

	def set_DtsJobId(self,DtsJobId):
		self.add_query_param('DtsJobId',DtsJobId)

	def get_RequestEndTime(self):
		return self.get_query_params().get('RequestEndTime')

	def set_RequestEndTime(self,RequestEndTime):
		self.add_query_param('RequestEndTime',RequestEndTime)

	def get_Amount(self):
		return self.get_query_params().get('Amount')

	def set_Amount(self,Amount):
		self.add_query_param('Amount',Amount)

	def get_TaskType(self):
		return self.get_query_params().get('TaskType')

	def set_TaskType(self,TaskType):
		self.add_query_param('TaskType',TaskType)

	def get_EndState(self):
		return self.get_query_params().get('EndState')

	def set_EndState(self,EndState):
		self.add_query_param('EndState',EndState)

	def get_BackupId(self):
		return self.get_query_params().get('BackupId')

	def set_BackupId(self,BackupId):
		self.add_query_param('BackupId',BackupId)

	def get_SrcSuperPassword(self):
		return self.get_query_params().get('SrcSuperPassword')

	def set_SrcSuperPassword(self,SrcSuperPassword):
		self.add_query_param('SrcSuperPassword',SrcSuperPassword)

	def get_BackupTime(self):
		return self.get_query_params().get('BackupTime')

	def set_BackupTime(self,BackupTime):
		self.add_query_param('BackupTime',BackupTime)

	def get_GatewayVpcIp(self):
		return self.get_query_params().get('GatewayVpcIp')

	def set_GatewayVpcIp(self,GatewayVpcIp):
		self.add_query_param('GatewayVpcIp',GatewayVpcIp)

	def get_WorkDir(self):
		return self.get_query_params().get('WorkDir')

	def set_WorkDir(self,WorkDir):
		self.add_query_param('WorkDir',WorkDir)

	def get_DtsJobClass(self):
		return self.get_query_params().get('DtsJobClass')

	def set_DtsJobClass(self,DtsJobClass):
		self.add_query_param('DtsJobClass',DtsJobClass)

	def get_SrcPublicIp(self):
		return self.get_query_params().get('SrcPublicIp')

	def set_SrcPublicIp(self,SrcPublicIp):
		self.add_query_param('SrcPublicIp',SrcPublicIp)

	def get_SrcInstanceId(self):
		return self.get_query_params().get('SrcInstanceId')

	def set_SrcInstanceId(self,SrcInstanceId):
		self.add_query_param('SrcInstanceId',SrcInstanceId)

	def get_DstType(self):
		return self.get_query_params().get('DstType')

	def set_DstType(self,DstType):
		self.add_query_param('DstType',DstType)

	def get_SrcSuperAccount(self):
		return self.get_query_params().get('SrcSuperAccount')

	def set_SrcSuperAccount(self,SrcSuperAccount):
		self.add_query_param('SrcSuperAccount',SrcSuperAccount)

	def get_GatewayVpcId(self):
		return self.get_query_params().get('GatewayVpcId')

	def set_GatewayVpcId(self,GatewayVpcId):
		self.add_query_param('GatewayVpcId',GatewayVpcId)

	def get_SmartPressureTime(self):
		return self.get_query_params().get('SmartPressureTime')

	def set_SmartPressureTime(self,SmartPressureTime):
		self.add_query_param('SmartPressureTime',SmartPressureTime)