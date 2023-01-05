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

class ShrinkClusterRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'eflo-controller', '2022-12-15', 'ShrinkCluster','eflo')
		self.set_method('POST')

	def get_IgnoreFailedNodeTasks(self): # Boolean
		return self.get_body_params().get('IgnoreFailedNodeTasks')

	def set_IgnoreFailedNodeTasks(self, IgnoreFailedNodeTasks):  # Boolean
		self.add_body_params('IgnoreFailedNodeTasks', IgnoreFailedNodeTasks)
	def get_ClusterId(self): # String
		return self.get_body_params().get('ClusterId')

	def set_ClusterId(self, ClusterId):  # String
		self.add_body_params('ClusterId', ClusterId)
	def get_NodeGroups(self): # Array
		return self.get_body_params().get('NodeGroups')

	def set_NodeGroups(self, NodeGroups):  # Array
		self.add_body_params("NodeGroups", json.dumps(NodeGroups))
