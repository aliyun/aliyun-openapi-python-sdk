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
from aliyunsdkecs.endpoint import endpoint_data
import json

class DescribePlanMaintenanceWindowsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ecs', '2014-05-26', 'DescribePlanMaintenanceWindows','ecs')
		self.set_protocol_type('https')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_TargetResourceTags(self): # Struct
		return self.get_query_params().get('TargetResourceTags')

	def set_TargetResourceTags(self, TargetResourceTags):  # Struct
		self.add_query_param("TargetResourceTags", json.dumps(TargetResourceTags))
	def get_PlanWindowId(self): # String
		return self.get_query_params().get('PlanWindowId')

	def set_PlanWindowId(self, PlanWindowId):  # String
		self.add_query_param('PlanWindowId', PlanWindowId)
	def get_NextToken(self): # String
		return self.get_query_params().get('NextToken')

	def set_NextToken(self, NextToken):  # String
		self.add_query_param('NextToken', NextToken)
	def get_Enable(self): # Boolean
		return self.get_query_params().get('Enable')

	def set_Enable(self, Enable):  # Boolean
		self.add_query_param('Enable', Enable)
	def get_PlanWindowName(self): # String
		return self.get_query_params().get('PlanWindowName')

	def set_PlanWindowName(self, PlanWindowName):  # String
		self.add_query_param('PlanWindowName', PlanWindowName)
	def get_TargetResourceGroupId(self): # String
		return self.get_query_params().get('TargetResourceGroupId')

	def set_TargetResourceGroupId(self, TargetResourceGroupId):  # String
		self.add_query_param('TargetResourceGroupId', TargetResourceGroupId)
	def get_MaxResults(self): # Integer
		return self.get_query_params().get('MaxResults')

	def set_MaxResults(self, MaxResults):  # Integer
		self.add_query_param('MaxResults', MaxResults)
