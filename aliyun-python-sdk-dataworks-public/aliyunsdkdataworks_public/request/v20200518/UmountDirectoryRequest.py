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

class UmountDirectoryRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'dataworks-public', '2020-05-18', 'UmountDirectory')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_TargetType(self): # String
		return self.get_body_params().get('TargetType')

	def set_TargetType(self, TargetType):  # String
		self.add_body_params('TargetType', TargetType)
	def get_TargetId(self): # String
		return self.get_body_params().get('TargetId')

	def set_TargetId(self, TargetId):  # String
		self.add_body_params('TargetId', TargetId)
	def get_TargetUserId(self): # String
		return self.get_body_params().get('TargetUserId')

	def set_TargetUserId(self, TargetUserId):  # String
		self.add_body_params('TargetUserId', TargetUserId)
