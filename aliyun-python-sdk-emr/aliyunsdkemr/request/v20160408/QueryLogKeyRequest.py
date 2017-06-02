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
class QueryLogKeyRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Emr', '2016-04-08', 'QueryLogKey')

	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_ClusterId(self):
		return self.get_query_params().get('ClusterId')

	def set_ClusterId(self,ClusterId):
		self.add_query_param('ClusterId',ClusterId)

	def get_JobId(self):
		return self.get_query_params().get('JobId')

	def set_JobId(self,JobId):
		self.add_query_param('JobId',JobId)

	def get_KeyBase(self):
		return self.get_query_params().get('KeyBase')

	def set_KeyBase(self,KeyBase):
		self.add_query_param('KeyBase',KeyBase)

	def get_InstanceId(self):
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self,InstanceId):
		self.add_query_param('InstanceId',InstanceId)

	def get_ContainerId(self):
		return self.get_query_params().get('ContainerId')

	def set_ContainerId(self,ContainerId):
		self.add_query_param('ContainerId',ContainerId)

	def get_LogName(self):
		return self.get_query_params().get('LogName')

	def set_LogName(self,LogName):
		self.add_query_param('LogName',LogName)