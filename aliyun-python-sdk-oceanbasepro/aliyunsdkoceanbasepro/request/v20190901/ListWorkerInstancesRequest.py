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
import json

class ListWorkerInstancesRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'OceanBasePro', '2019-09-01', 'ListWorkerInstances','oceanbase')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_OnlyBindable(self): # Boolean
		return self.get_body_params().get('OnlyBindable')

	def set_OnlyBindable(self, OnlyBindable):  # Boolean
		self.add_body_params('OnlyBindable', OnlyBindable)
	def get_PageNumber(self): # Integer
		return self.get_body_params().get('PageNumber')

	def set_PageNumber(self, PageNumber):  # Integer
		self.add_body_params('PageNumber', PageNumber)
	def get_Specs(self): # Array
		return self.get_body_params().get('Specs')

	def set_Specs(self, Specs):  # Array
		self.add_body_params("Specs", json.dumps(Specs))
	def get_InstanceName(self): # String
		return self.get_body_params().get('InstanceName')

	def set_InstanceName(self, InstanceName):  # String
		self.add_body_params('InstanceName', InstanceName)
	def get_PageSize(self): # Integer
		return self.get_body_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Integer
		self.add_body_params('PageSize', PageSize)
	def get_SourceType(self): # String
		return self.get_body_params().get('SourceType')

	def set_SourceType(self, SourceType):  # String
		self.add_body_params('SourceType', SourceType)
	def get_DestType(self): # String
		return self.get_body_params().get('DestType')

	def set_DestType(self, DestType):  # String
		self.add_body_params('DestType', DestType)
