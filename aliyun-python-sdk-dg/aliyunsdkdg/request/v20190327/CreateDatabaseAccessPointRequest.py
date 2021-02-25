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
from aliyunsdkdg.endpoint import endpoint_data

class CreateDatabaseAccessPointRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'dg', '2019-03-27', 'CreateDatabaseAccessPoint','dg')
		self.set_protocol_type('https')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_VpcAZone(self):
		return self.get_body_params().get('VpcAZone')

	def set_VpcAZone(self,VpcAZone):
		self.add_body_params('VpcAZone', VpcAZone)

	def get_ClientToken(self):
		return self.get_body_params().get('ClientToken')

	def set_ClientToken(self,ClientToken):
		self.add_body_params('ClientToken', ClientToken)

	def get_DbInstanceId(self):
		return self.get_body_params().get('DbInstanceId')

	def set_DbInstanceId(self,DbInstanceId):
		self.add_body_params('DbInstanceId', DbInstanceId)

	def get_VpcRegionId(self):
		return self.get_body_params().get('VpcRegionId')

	def set_VpcRegionId(self,VpcRegionId):
		self.add_body_params('VpcRegionId', VpcRegionId)

	def get_VSwitchId(self):
		return self.get_body_params().get('VSwitchId')

	def set_VSwitchId(self,VSwitchId):
		self.add_body_params('VSwitchId', VSwitchId)

	def get_VpcId(self):
		return self.get_body_params().get('VpcId')

	def set_VpcId(self,VpcId):
		self.add_body_params('VpcId', VpcId)