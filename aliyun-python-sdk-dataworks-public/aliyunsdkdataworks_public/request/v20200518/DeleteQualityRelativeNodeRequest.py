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
from aliyunsdkdataworks_public.endpoint import endpoint_data

class DeleteQualityRelativeNodeRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'dataworks-public', '2020-05-18', 'DeleteQualityRelativeNode')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ProjectName(self): # String
		return self.get_body_params().get('ProjectName')

	def set_ProjectName(self, ProjectName):  # String
		self.add_body_params('ProjectName', ProjectName)
	def get_TargetNodeProjectId(self): # Long
		return self.get_body_params().get('TargetNodeProjectId')

	def set_TargetNodeProjectId(self, TargetNodeProjectId):  # Long
		self.add_body_params('TargetNodeProjectId', TargetNodeProjectId)
	def get_MatchExpression(self): # String
		return self.get_body_params().get('MatchExpression')

	def set_MatchExpression(self, MatchExpression):  # String
		self.add_body_params('MatchExpression', MatchExpression)
	def get_EnvType(self): # String
		return self.get_body_params().get('EnvType')

	def set_EnvType(self, EnvType):  # String
		self.add_body_params('EnvType', EnvType)
	def get_TargetNodeProjectName(self): # String
		return self.get_body_params().get('TargetNodeProjectName')

	def set_TargetNodeProjectName(self, TargetNodeProjectName):  # String
		self.add_body_params('TargetNodeProjectName', TargetNodeProjectName)
	def get_TableName(self): # String
		return self.get_body_params().get('TableName')

	def set_TableName(self, TableName):  # String
		self.add_body_params('TableName', TableName)
	def get_NodeId(self): # Long
		return self.get_body_params().get('NodeId')

	def set_NodeId(self, NodeId):  # Long
		self.add_body_params('NodeId', NodeId)
	def get_ProjectId(self): # Long
		return self.get_body_params().get('ProjectId')

	def set_ProjectId(self, ProjectId):  # Long
		self.add_body_params('ProjectId', ProjectId)
