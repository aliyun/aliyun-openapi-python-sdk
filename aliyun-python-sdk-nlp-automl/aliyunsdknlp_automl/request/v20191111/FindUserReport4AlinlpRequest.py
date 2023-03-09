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
from aliyunsdknlp_automl.endpoint import endpoint_data

class FindUserReport4AlinlpRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'nlp-automl', '2019-11-11', 'FindUserReport4Alinlp')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_CustomerUserParentId(self): # Long
		return self.get_body_params().get('CustomerUserParentId')

	def set_CustomerUserParentId(self, CustomerUserParentId):  # Long
		self.add_body_params('CustomerUserParentId', CustomerUserParentId)
	def get_EndTime(self): # String
		return self.get_body_params().get('EndTime')

	def set_EndTime(self, EndTime):  # String
		self.add_body_params('EndTime', EndTime)
	def get_BeginTime(self): # String
		return self.get_body_params().get('BeginTime')

	def set_BeginTime(self, BeginTime):  # String
		self.add_body_params('BeginTime', BeginTime)
	def get_Type(self): # String
		return self.get_body_params().get('Type')

	def set_Type(self, Type):  # String
		self.add_body_params('Type', Type)
	def get_ModelType(self): # String
		return self.get_body_params().get('ModelType')

	def set_ModelType(self, ModelType):  # String
		self.add_body_params('ModelType', ModelType)
