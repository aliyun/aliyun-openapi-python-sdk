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

from aliyunsdkcore.request import RoaRequest
from aliyunsdkfoas.endpoint import endpoint_data

class CreateCellClusterOrderRequest(RoaRequest):

	def __init__(self):
		RoaRequest.__init__(self, 'foas', '2018-11-11', 'CreateCellClusterOrder','foas')
		self.set_protocol_type('https')
		self.set_uri_pattern('/api/v2/realtime-compute/cell/buy')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_period(self):
		return self.get_body_params().get('period')

	def set_period(self,period):
		self.add_body_params('period', period)

	def get_slaveNum(self):
		return self.get_body_params().get('slaveNum')

	def set_slaveNum(self,slaveNum):
		self.add_body_params('slaveNum', slaveNum)

	def get_slaveSpec(self):
		return self.get_body_params().get('slaveSpec')

	def set_slaveSpec(self,slaveSpec):
		self.add_body_params('slaveSpec', slaveSpec)

	def get_region(self):
		return self.get_body_params().get('region')

	def set_region(self,region):
		self.add_body_params('region', region)

	def get_masterNum(self):
		return self.get_body_params().get('masterNum')

	def set_masterNum(self,masterNum):
		self.add_body_params('masterNum', masterNum)

	def get_masterSpec(self):
		return self.get_body_params().get('masterSpec')

	def set_masterSpec(self,masterSpec):
		self.add_body_params('masterSpec', masterSpec)

	def get_payModel(self):
		return self.get_body_params().get('payModel')

	def set_payModel(self,payModel):
		self.add_body_params('payModel', payModel)