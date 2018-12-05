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
class CreateLifecycleHookRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ess', '2014-08-28', 'CreateLifecycleHook','ess')

	def get_DefaultResult(self):
		return self.get_query_params().get('DefaultResult')

	def set_DefaultResult(self,DefaultResult):
		self.add_query_param('DefaultResult',DefaultResult)

	def get_ResourceOwnerAccount(self):
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self,ResourceOwnerAccount):
		self.add_query_param('ResourceOwnerAccount',ResourceOwnerAccount)

	def get_HeartbeatTimeout(self):
		return self.get_query_params().get('HeartbeatTimeout')

	def set_HeartbeatTimeout(self,HeartbeatTimeout):
		self.add_query_param('HeartbeatTimeout',HeartbeatTimeout)

	def get_ScalingGroupId(self):
		return self.get_query_params().get('ScalingGroupId')

	def set_ScalingGroupId(self,ScalingGroupId):
		self.add_query_param('ScalingGroupId',ScalingGroupId)

	def get_OwnerAccount(self):
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self,OwnerAccount):
		self.add_query_param('OwnerAccount',OwnerAccount)

	def get_NotificationMetadata(self):
		return self.get_query_params().get('NotificationMetadata')

	def set_NotificationMetadata(self,NotificationMetadata):
		self.add_query_param('NotificationMetadata',NotificationMetadata)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_LifecycleTransition(self):
		return self.get_query_params().get('LifecycleTransition')

	def set_LifecycleTransition(self,LifecycleTransition):
		self.add_query_param('LifecycleTransition',LifecycleTransition)

	def get_LifecycleHookName(self):
		return self.get_query_params().get('LifecycleHookName')

	def set_LifecycleHookName(self,LifecycleHookName):
		self.add_query_param('LifecycleHookName',LifecycleHookName)

	def get_NotificationArn(self):
		return self.get_query_params().get('NotificationArn')

	def set_NotificationArn(self,NotificationArn):
		self.add_query_param('NotificationArn',NotificationArn)

	def get_LifecycleHooks(self):
		return self.get_query_params().get('LifecycleHooks')

	def set_LifecycleHooks(self,LifecycleHooks):
		for i in range(len(LifecycleHooks)):	
			if LifecycleHooks[i].get('DefaultResult') is not None:
				self.add_query_param('LifecycleHook.' + str(i + 1) + '.DefaultResult' , LifecycleHooks[i].get('DefaultResult'))
			if LifecycleHooks[i].get('LifecycleHookName') is not None:
				self.add_query_param('LifecycleHook.' + str(i + 1) + '.LifecycleHookName' , LifecycleHooks[i].get('LifecycleHookName'))
			if LifecycleHooks[i].get('HeartbeatTimeout') is not None:
				self.add_query_param('LifecycleHook.' + str(i + 1) + '.HeartbeatTimeout' , LifecycleHooks[i].get('HeartbeatTimeout'))
			if LifecycleHooks[i].get('NotificationArn') is not None:
				self.add_query_param('LifecycleHook.' + str(i + 1) + '.NotificationArn' , LifecycleHooks[i].get('NotificationArn'))
			if LifecycleHooks[i].get('NotificationMetadata') is not None:
				self.add_query_param('LifecycleHook.' + str(i + 1) + '.NotificationMetadata' , LifecycleHooks[i].get('NotificationMetadata'))
			if LifecycleHooks[i].get('LifecycleTransition') is not None:
				self.add_query_param('LifecycleHook.' + str(i + 1) + '.LifecycleTransition' , LifecycleHooks[i].get('LifecycleTransition'))
