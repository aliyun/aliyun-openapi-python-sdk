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
from aliyunsdkbrain_industrial.endpoint import endpoint_data

class ActivateLicenseRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'brain-industrial', '2020-09-20', 'ActivateLicense','aistudio')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_Fingerprint(self): # String
		return self.get_body_params().get('Fingerprint')

	def set_Fingerprint(self, Fingerprint):  # String
		self.add_body_params('Fingerprint', Fingerprint)
	def get_Id(self): # String
		return self.get_body_params().get('Id')

	def set_Id(self, Id):  # String
		self.add_body_params('Id', Id)
	def get_OrderId(self): # String
		return self.get_body_params().get('OrderId')

	def set_OrderId(self, OrderId):  # String
		self.add_body_params('OrderId', OrderId)
	def get_InstanceId(self): # String
		return self.get_body_params().get('InstanceId')

	def set_InstanceId(self, InstanceId):  # String
		self.add_body_params('InstanceId', InstanceId)
