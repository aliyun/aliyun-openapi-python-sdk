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
from aliyunsdkoos.endpoint import endpoint_data
import json

class UpdatePatchBaselineRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'oos', '2019-06-01', 'UpdatePatchBaseline','oos')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_Sources(self): # Array
		return self.get_query_params().get('Sources')

	def set_Sources(self, Sources):  # Array
		self.add_query_param("Sources", json.dumps(Sources))
	def get_ClientToken(self): # String
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self, ClientToken):  # String
		self.add_query_param('ClientToken', ClientToken)
	def get_ApprovalRules(self): # String
		return self.get_query_params().get('ApprovalRules')

	def set_ApprovalRules(self, ApprovalRules):  # String
		self.add_query_param('ApprovalRules', ApprovalRules)
	def get_Description(self): # String
		return self.get_query_params().get('Description')

	def set_Description(self, Description):  # String
		self.add_query_param('Description', Description)
	def get_RejectedPatchesAction(self): # String
		return self.get_query_params().get('RejectedPatchesAction')

	def set_RejectedPatchesAction(self, RejectedPatchesAction):  # String
		self.add_query_param('RejectedPatchesAction', RejectedPatchesAction)
	def get_ApprovedPatchesEnableNonSecurity(self): # Boolean
		return self.get_query_params().get('ApprovedPatchesEnableNonSecurity')

	def set_ApprovedPatchesEnableNonSecurity(self, ApprovedPatchesEnableNonSecurity):  # Boolean
		self.add_query_param('ApprovedPatchesEnableNonSecurity', ApprovedPatchesEnableNonSecurity)
	def get_Tags(self): # Array
		return self.get_query_params().get('Tags')

	def set_Tags(self, Tags):  # Array
		self.add_query_param("Tags", json.dumps(Tags))
	def get_RejectedPatches(self): # Array
		return self.get_query_params().get('RejectedPatches')

	def set_RejectedPatches(self, RejectedPatches):  # Array
		self.add_query_param("RejectedPatches", json.dumps(RejectedPatches))
	def get_Name(self): # String
		return self.get_query_params().get('Name')

	def set_Name(self, Name):  # String
		self.add_query_param('Name', Name)
	def get_ApprovedPatches(self): # Array
		return self.get_query_params().get('ApprovedPatches')

	def set_ApprovedPatches(self, ApprovedPatches):  # Array
		self.add_query_param("ApprovedPatches", json.dumps(ApprovedPatches))
