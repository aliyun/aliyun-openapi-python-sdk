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
import json

class CreateClusterRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'eflo-controller', '2022-12-15', 'CreateCluster','eflo')
		self.set_method('POST')

	def get_Components(self): # Array
		return self.get_body_params().get('Components')

	def set_Components(self, Components):  # Array
		self.add_body_params("Components", json.dumps(Components))
	def get_ClusterName(self): # String
		return self.get_body_params().get('ClusterName')

	def set_ClusterName(self, ClusterName):  # String
		self.add_body_params('ClusterName', ClusterName)
	def get_Networks(self): # Struct
		return self.get_body_params().get('Networks')

	def set_Networks(self, Networks):  # Struct
		self.add_body_params("Networks", json.dumps(Networks))
	def get_ResourceGroupId(self): # String
		return self.get_body_params().get('ResourceGroupId')

	def set_ResourceGroupId(self, ResourceGroupId):  # String
		self.add_body_params('ResourceGroupId', ResourceGroupId)
	def get_ClusterDescription(self): # String
		return self.get_body_params().get('ClusterDescription')

	def set_ClusterDescription(self, ClusterDescription):  # String
		self.add_body_params('ClusterDescription', ClusterDescription)
	def get_NodeGroups(self): # Array
		return self.get_body_params().get('NodeGroups')

	def set_NodeGroups(self, NodeGroups):  # Array
		self.add_body_params("NodeGroups", json.dumps(NodeGroups))
	def get_Tags(self): # RepeatList
		return self.get_query_params().get('Tag')

	def set_Tags(self, Tag):  # RepeatList
		for depth1 in range(len(Tag)):
			if Tag[depth1].get('Value') is not None:
				self.add_query_param('Tag.' + str(depth1 + 1) + '.Value', Tag[depth1].get('Value'))
			if Tag[depth1].get('Key') is not None:
				self.add_query_param('Tag.' + str(depth1 + 1) + '.Key', Tag[depth1].get('Key'))
	def get_IgnoreFailedNodeTasks(self): # Boolean
		return self.get_body_params().get('IgnoreFailedNodeTasks')

	def set_IgnoreFailedNodeTasks(self, IgnoreFailedNodeTasks):  # Boolean
		self.add_body_params('IgnoreFailedNodeTasks', IgnoreFailedNodeTasks)
	def get_ClusterType(self): # String
		return self.get_body_params().get('ClusterType')

	def set_ClusterType(self, ClusterType):  # String
		self.add_body_params('ClusterType', ClusterType)
