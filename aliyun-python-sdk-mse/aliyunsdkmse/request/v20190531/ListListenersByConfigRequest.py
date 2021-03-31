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

class ListListenersByConfigRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'mse', '2019-05-31', 'ListListenersByConfig','mse')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_InstanceId(self):
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self,InstanceId):
		self.add_query_param('InstanceId',InstanceId)

	def get_DataId(self):
		return self.get_query_params().get('DataId')

	def set_DataId(self,DataId):
		self.add_query_param('DataId',DataId)

	def get_NamespaceId(self):
		return self.get_query_params().get('NamespaceId')

	def set_NamespaceId(self,NamespaceId):
		self.add_query_param('NamespaceId',NamespaceId)

	def get_RequestPars(self):
		return self.get_query_params().get('RequestPars')

	def set_RequestPars(self,RequestPars):
		self.add_query_param('RequestPars',RequestPars)

	def get_Group(self):
		return self.get_query_params().get('Group')

	def set_Group(self,Group):
		self.add_query_param('Group',Group)