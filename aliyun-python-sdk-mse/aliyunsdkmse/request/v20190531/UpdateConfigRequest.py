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
from aliyunsdkmse.endpoint import endpoint_data

class UpdateConfigRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'mse', '2019-05-31', 'UpdateConfig','mse')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_OpenSuperAcl(self):
		return self.get_body_params().get('OpenSuperAcl')

	def set_OpenSuperAcl(self,OpenSuperAcl):
		self.add_body_params('OpenSuperAcl', OpenSuperAcl)

	def get_ConfigAuthEnabled(self):
		return self.get_query_params().get('ConfigAuthEnabled')

	def set_ConfigAuthEnabled(self,ConfigAuthEnabled):
		self.add_query_param('ConfigAuthEnabled',ConfigAuthEnabled)

	def get_PassWord(self):
		return self.get_query_params().get('PassWord')

	def set_PassWord(self,PassWord):
		self.add_query_param('PassWord',PassWord)

	def get_MaxClientCnxns(self):
		return self.get_query_params().get('MaxClientCnxns')

	def set_MaxClientCnxns(self,MaxClientCnxns):
		self.add_query_param('MaxClientCnxns',MaxClientCnxns)

	def get_RequestPars(self):
		return self.get_query_params().get('RequestPars')

	def set_RequestPars(self,RequestPars):
		self.add_query_param('RequestPars',RequestPars)

	def get_JuteMaxbuffer(self):
		return self.get_query_params().get('JuteMaxbuffer')

	def set_JuteMaxbuffer(self,JuteMaxbuffer):
		self.add_query_param('JuteMaxbuffer',JuteMaxbuffer)

	def get_ConfigType(self):
		return self.get_query_params().get('ConfigType')

	def set_ConfigType(self,ConfigType):
		self.add_query_param('ConfigType',ConfigType)

	def get_AutopurgeSnapRetainCount(self):
		return self.get_query_params().get('AutopurgeSnapRetainCount')

	def set_AutopurgeSnapRetainCount(self,AutopurgeSnapRetainCount):
		self.add_query_param('AutopurgeSnapRetainCount',AutopurgeSnapRetainCount)

	def get_MCPEnabled(self):
		return self.get_query_params().get('MCPEnabled')

	def set_MCPEnabled(self,MCPEnabled):
		self.add_query_param('MCPEnabled',MCPEnabled)

	def get_TickTime(self):
		return self.get_query_params().get('TickTime')

	def set_TickTime(self,TickTime):
		self.add_query_param('TickTime',TickTime)

	def get_ClusterId(self):
		return self.get_query_params().get('ClusterId')

	def set_ClusterId(self,ClusterId):
		self.add_query_param('ClusterId',ClusterId)

	def get_SyncLimit(self):
		return self.get_query_params().get('SyncLimit')

	def set_SyncLimit(self,SyncLimit):
		self.add_query_param('SyncLimit',SyncLimit)

	def get_InstanceId(self):
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self,InstanceId):
		self.add_query_param('InstanceId',InstanceId)

	def get_AutopurgePurgeInterval(self):
		return self.get_query_params().get('AutopurgePurgeInterval')

	def set_AutopurgePurgeInterval(self,AutopurgePurgeInterval):
		self.add_query_param('AutopurgePurgeInterval',AutopurgePurgeInterval)

	def get_InitLimit(self):
		return self.get_query_params().get('InitLimit')

	def set_InitLimit(self,InitLimit):
		self.add_query_param('InitLimit',InitLimit)

	def get_UserName(self):
		return self.get_query_params().get('UserName')

	def set_UserName(self,UserName):
		self.add_query_param('UserName',UserName)