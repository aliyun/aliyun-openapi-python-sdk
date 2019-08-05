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
from aliyunsdkcspro.endpoint import endpoint_data

class GetSecCheckResultDetailRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'cspro', '2018-12-17', 'GetSecCheckResultDetail','cspro')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_RiskType(self):
		return self.get_body_params().get('RiskType')

	def set_RiskType(self,RiskType):
		self.add_body_params('RiskType', RiskType)

	def get_RiskSource(self):
		return self.get_body_params().get('RiskSource')

	def set_RiskSource(self,RiskSource):
		self.add_body_params('RiskSource', RiskSource)

	def get_ResultId(self):
		return self.get_body_params().get('ResultId')

	def set_ResultId(self,ResultId):
		self.add_body_params('ResultId', ResultId)