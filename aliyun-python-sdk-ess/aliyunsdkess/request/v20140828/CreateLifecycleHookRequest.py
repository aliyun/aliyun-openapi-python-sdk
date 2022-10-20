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
from aliyunsdkess.endpoint import endpoint_data

class CreateLifecycleHookRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ess', '2014-08-28', 'CreateLifecycleHook','ess')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_DefaultResult(self): # String
		return self.get_query_params().get('DefaultResult')

	def set_DefaultResult(self, DefaultResult):  # String
		self.add_query_param('DefaultResult', DefaultResult)
	def get_HeartbeatTimeout(self): # Integer
		return self.get_query_params().get('HeartbeatTimeout')

	def set_HeartbeatTimeout(self, HeartbeatTimeout):  # Integer
		self.add_query_param('HeartbeatTimeout', HeartbeatTimeout)
	def get_ScalingGroupId(self): # String
		return self.get_query_params().get('ScalingGroupId')

	def set_ScalingGroupId(self, ScalingGroupId):  # String
		self.add_query_param('ScalingGroupId', ScalingGroupId)
	def get_LifecycleTransition(self): # String
		return self.get_query_params().get('LifecycleTransition')

	def set_LifecycleTransition(self, LifecycleTransition):  # String
		self.add_query_param('LifecycleTransition', LifecycleTransition)
	def get_LifecycleHookName(self): # String
		return self.get_query_params().get('LifecycleHookName')

	def set_LifecycleHookName(self, LifecycleHookName):  # String
		self.add_query_param('LifecycleHookName', LifecycleHookName)
	def get_NotificationArn(self): # String
		return self.get_query_params().get('NotificationArn')

	def set_NotificationArn(self, NotificationArn):  # String
		self.add_query_param('NotificationArn', NotificationArn)
	def get_ResourceOwnerAccount(self): # String
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self, ResourceOwnerAccount):  # String
		self.add_query_param('ResourceOwnerAccount', ResourceOwnerAccount)
	def get_OwnerAccount(self): # String
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self, OwnerAccount):  # String
		self.add_query_param('OwnerAccount', OwnerAccount)
	def get_NotificationMetadata(self): # String
		return self.get_query_params().get('NotificationMetadata')

	def set_NotificationMetadata(self, NotificationMetadata):  # String
		self.add_query_param('NotificationMetadata', NotificationMetadata)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
