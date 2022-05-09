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

class ModifyResourceQueueRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Emr', '2016-04-08', 'ModifyResourceQueue','emr')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_QualifiedName(self):
		return self.get_query_params().get('QualifiedName')

	def set_QualifiedName(self,QualifiedName):
		self.add_query_param('QualifiedName',QualifiedName)

	def get_ResourcePoolId(self):
		return self.get_query_params().get('ResourcePoolId')

	def set_ResourcePoolId(self,ResourcePoolId):
		self.add_query_param('ResourcePoolId',ResourcePoolId)

	def get_ClusterId(self):
		return self.get_query_params().get('ClusterId')

	def set_ClusterId(self,ClusterId):
		self.add_query_param('ClusterId',ClusterId)

	def get_Leaf(self):
		return self.get_query_params().get('Leaf')

	def set_Leaf(self,Leaf):
		self.add_query_param('Leaf',Leaf)

	def get_ParentQueueId(self):
		return self.get_query_params().get('ParentQueueId')

	def set_ParentQueueId(self,ParentQueueId):
		self.add_query_param('ParentQueueId',ParentQueueId)

	def get_Name(self):
		return self.get_query_params().get('Name')

	def set_Name(self,Name):
		self.add_query_param('Name',Name)

	def get_Id(self):
		return self.get_query_params().get('Id')

	def set_Id(self,Id):
		self.add_query_param('Id',Id)

	def get_Configs(self):
		return self.get_query_params().get('Config')

	def set_Configs(self, Configs):
		for depth1 in range(len(Configs)):
			if Configs[depth1].get('ConfigKey') is not None:
				self.add_query_param('Config.' + str(depth1 + 1) + '.ConfigKey', Configs[depth1].get('ConfigKey'))
			if Configs[depth1].get('Note') is not None:
				self.add_query_param('Config.' + str(depth1 + 1) + '.Note', Configs[depth1].get('Note'))
			if Configs[depth1].get('ConfigValue') is not None:
				self.add_query_param('Config.' + str(depth1 + 1) + '.ConfigValue', Configs[depth1].get('ConfigValue'))
			if Configs[depth1].get('Id') is not None:
				self.add_query_param('Config.' + str(depth1 + 1) + '.Id', Configs[depth1].get('Id'))
			if Configs[depth1].get('Category') is not None:
				self.add_query_param('Config.' + str(depth1 + 1) + '.Category', Configs[depth1].get('Category'))