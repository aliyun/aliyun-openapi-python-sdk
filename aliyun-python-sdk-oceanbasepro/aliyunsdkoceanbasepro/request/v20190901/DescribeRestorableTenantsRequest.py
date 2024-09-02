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
from aliyunsdkoceanbasepro.endpoint import endpoint_data

class DescribeRestorableTenantsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'OceanBasePro', '2019-09-01', 'DescribeRestorableTenants','oceanbase')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_RestoreMode(self): # String
		return self.get_body_params().get('RestoreMode')

	def set_RestoreMode(self, RestoreMode):  # String
		self.add_body_params('RestoreMode', RestoreMode)
	def get_RestoreObjectType(self): # String
		return self.get_body_params().get('RestoreObjectType')

	def set_RestoreObjectType(self, RestoreObjectType):  # String
		self.add_body_params('RestoreObjectType', RestoreObjectType)
	def get_IsOnline(self): # Boolean
		return self.get_body_params().get('IsOnline')

	def set_IsOnline(self, IsOnline):  # Boolean
		self.add_body_params('IsOnline', IsOnline)
	def get_IsRemote(self): # Boolean
		return self.get_body_params().get('IsRemote')

	def set_IsRemote(self, IsRemote):  # Boolean
		self.add_body_params('IsRemote', IsRemote)
	def get_Method(self): # String
		return self.get_body_params().get('Method')

	def set_Method(self, Method):  # String
		self.add_body_params('Method', Method)
	def get_InstanceId(self): # String
		return self.get_body_params().get('InstanceId')

	def set_InstanceId(self, InstanceId):  # String
		self.add_body_params('InstanceId', InstanceId)
	def get_SetId(self): # String
		return self.get_body_params().get('SetId')

	def set_SetId(self, SetId):  # String
		self.add_body_params('SetId', SetId)
