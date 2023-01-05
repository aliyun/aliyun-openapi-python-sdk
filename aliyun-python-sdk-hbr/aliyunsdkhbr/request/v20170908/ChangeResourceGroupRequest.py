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
from aliyunsdkhbr.endpoint import endpoint_data

class ChangeResourceGroupRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'hbr', '2017-09-08', 'ChangeResourceGroup')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ResourceId(self): # String
		return self.get_body_params().get('ResourceId')

	def set_ResourceId(self, ResourceId):  # String
		self.add_body_params('ResourceId', ResourceId)
	def get_ResourceType(self): # String
		return self.get_body_params().get('ResourceType')

	def set_ResourceType(self, ResourceType):  # String
		self.add_body_params('ResourceType', ResourceType)
	def get_NewResourceGroupId(self): # String
		return self.get_body_params().get('NewResourceGroupId')

	def set_NewResourceGroupId(self, NewResourceGroupId):  # String
		self.add_body_params('NewResourceGroupId', NewResourceGroupId)
