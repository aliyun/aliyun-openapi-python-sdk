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
class CreateConfigurationRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'afs', '2018-01-12', 'CreateConfiguration')

	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_SourceIp(self):
		return self.get_query_params().get('SourceIp')

	def set_SourceIp(self,SourceIp):
		self.add_query_param('SourceIp',SourceIp)

	def get_ConfigurationName(self):
		return self.get_query_params().get('ConfigurationName')

	def set_ConfigurationName(self,ConfigurationName):
		self.add_query_param('ConfigurationName',ConfigurationName)

	def get_MaxPV(self):
		return self.get_query_params().get('MaxPV')

	def set_MaxPV(self,MaxPV):
		self.add_query_param('MaxPV',MaxPV)

	def get_ConfigurationMethod(self):
		return self.get_query_params().get('ConfigurationMethod')

	def set_ConfigurationMethod(self,ConfigurationMethod):
		self.add_query_param('ConfigurationMethod',ConfigurationMethod)

	def get_ApplyType(self):
		return self.get_query_params().get('ApplyType')

	def set_ApplyType(self,ApplyType):
		self.add_query_param('ApplyType',ApplyType)

	def get_Scene(self):
		return self.get_query_params().get('Scene')

	def set_Scene(self,Scene):
		self.add_query_param('Scene',Scene)