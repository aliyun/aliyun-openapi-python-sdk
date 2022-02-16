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

class CreateAutoScalingPolicyRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Emr', '2021-03-20', 'CreateAutoScalingPolicy','emr')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ClusterId(self):
		return self.get_query_params().get('ClusterId')

	def set_ClusterId(self,ClusterId):
		self.add_query_param('ClusterId',ClusterId)

	def get_ScalingRuleSpecs(self):
		return self.get_query_params().get('ScalingRuleSpecs')

	def set_ScalingRuleSpecs(self,ScalingRuleSpecs):
		self.add_query_param('ScalingRuleSpecs',ScalingRuleSpecs)

	def get_NodeGroupId(self):
		return self.get_query_params().get('NodeGroupId')

	def set_NodeGroupId(self,NodeGroupId):
		self.add_query_param('NodeGroupId',NodeGroupId)

	def get_EnableWhenCreate(self):
		return self.get_query_params().get('EnableWhenCreate')

	def set_EnableWhenCreate(self,EnableWhenCreate):
		self.add_query_param('EnableWhenCreate',EnableWhenCreate)