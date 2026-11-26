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
from aliyunsdkgpdb.endpoint import endpoint_data

class DeleteAINodeRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'gpdb', '2016-05-03', 'DeleteAINode','GPDB')
		self.set_protocol_type('https')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_NodeNamess(self): # RepeatList
		return self.get_query_params().get('NodeNames')

	def set_NodeNamess(self, NodeNames):  # RepeatList
		for depth1 in range(len(NodeNames)):
			self.add_query_param('NodeNames.' + str(depth1 + 1), NodeNames[depth1])
	def get_AINodeNum(self): # Integer
		return self.get_query_params().get('AINodeNum')

	def set_AINodeNum(self, AINodeNum):  # Integer
		self.add_query_param('AINodeNum', AINodeNum)
	def get_DBInstanceId(self): # String
		return self.get_query_params().get('DBInstanceId')

	def set_DBInstanceId(self, DBInstanceId):  # String
		self.add_query_param('DBInstanceId', DBInstanceId)
	def get_AINodePoolId(self): # String
		return self.get_query_params().get('AINodePoolId')

	def set_AINodePoolId(self, AINodePoolId):  # String
		self.add_query_param('AINodePoolId', AINodePoolId)
