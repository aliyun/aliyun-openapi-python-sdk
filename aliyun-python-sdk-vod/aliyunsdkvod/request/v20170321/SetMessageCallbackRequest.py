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
from aliyunsdkvod.endpoint import endpoint_data

class SetMessageCallbackRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'vod', '2017-03-21', 'SetMessageCallback','vod')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_AuthKey(self):
		return self.get_query_params().get('AuthKey')

	def set_AuthKey(self,AuthKey):
		self.add_query_param('AuthKey',AuthKey)

	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_ResourceRealOwnerId(self):
		return self.get_query_params().get('ResourceRealOwnerId')

	def set_ResourceRealOwnerId(self,ResourceRealOwnerId):
		self.add_query_param('ResourceRealOwnerId',ResourceRealOwnerId)

	def get_CallbackType(self):
		return self.get_query_params().get('CallbackType')

	def set_CallbackType(self,CallbackType):
		self.add_query_param('CallbackType',CallbackType)

	def get_ResourceOwnerAccount(self):
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self,ResourceOwnerAccount):
		self.add_query_param('ResourceOwnerAccount',ResourceOwnerAccount)

	def get_OwnerAccount(self):
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self,OwnerAccount):
		self.add_query_param('OwnerAccount',OwnerAccount)

	def get_EventTypeList(self):
		return self.get_query_params().get('EventTypeList')

	def set_EventTypeList(self,EventTypeList):
		self.add_query_param('EventTypeList',EventTypeList)

	def get_MnsQueueName(self):
		return self.get_query_params().get('MnsQueueName')

	def set_MnsQueueName(self,MnsQueueName):
		self.add_query_param('MnsQueueName',MnsQueueName)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_MnsEndpoint(self):
		return self.get_query_params().get('MnsEndpoint')

	def set_MnsEndpoint(self,MnsEndpoint):
		self.add_query_param('MnsEndpoint',MnsEndpoint)

	def get_AppId(self):
		return self.get_query_params().get('AppId')

	def set_AppId(self,AppId):
		self.add_query_param('AppId',AppId)

	def get_AuthSwitch(self):
		return self.get_query_params().get('AuthSwitch')

	def set_AuthSwitch(self,AuthSwitch):
		self.add_query_param('AuthSwitch',AuthSwitch)

	def get_CallbackURL(self):
		return self.get_query_params().get('CallbackURL')

	def set_CallbackURL(self,CallbackURL):
		self.add_query_param('CallbackURL',CallbackURL)