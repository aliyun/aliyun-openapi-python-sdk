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
import json

class CreatePolicyV2Request(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'hbr', '2017-09-08', 'CreatePolicyV2')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_Rules(self): # Array
		return self.get_body_params().get('Rules')

	def set_Rules(self, Rules):  # Array
		self.add_body_params("Rules", json.dumps(Rules))
	def get_PolicyName(self): # String
		return self.get_body_params().get('PolicyName')

	def set_PolicyName(self, PolicyName):  # String
		self.add_body_params('PolicyName', PolicyName)
	def get_PolicyDescription(self): # String
		return self.get_body_params().get('PolicyDescription')

	def set_PolicyDescription(self, PolicyDescription):  # String
		self.add_body_params('PolicyDescription', PolicyDescription)
