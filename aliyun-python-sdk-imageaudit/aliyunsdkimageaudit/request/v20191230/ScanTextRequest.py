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
from aliyunsdkimageaudit.endpoint import endpoint_data

class ScanTextRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'imageaudit', '2019-12-30', 'ScanText','imageaudit')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_Labelss(self):
		return self.get_body_params().get('Labels')

	def set_Labelss(self, Labelss):
		for depth1 in range(len(Labelss)):
			if Labelss[depth1].get('Label') is not None:
				self.add_body_params('Labels.' + str(depth1 + 1) + '.Label', Labelss[depth1].get('Label'))

	def get_Taskss(self):
		return self.get_body_params().get('Tasks')

	def set_Taskss(self, Taskss):
		for depth1 in range(len(Taskss)):
			if Taskss[depth1].get('Content') is not None:
				self.add_body_params('Tasks.' + str(depth1 + 1) + '.Content', Taskss[depth1].get('Content'))