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
from aliyunsdkcompanyreg.endpoint import endpoint_data

class SubmitIcpSolutionRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'companyreg', '2019-05-08', 'SubmitIcpSolution')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_Area(self): # String
		return self.get_body_params().get('Area')

	def set_Area(self, Area):  # String
		self.add_body_params('Area', Area)
	def get_ActionType(self): # String
		return self.get_body_params().get('ActionType')

	def set_ActionType(self, ActionType):  # String
		self.add_body_params('ActionType', ActionType)
	def get_IntentionBizId(self): # String
		return self.get_body_params().get('IntentionBizId')

	def set_IntentionBizId(self, IntentionBizId):  # String
		self.add_body_params('IntentionBizId', IntentionBizId)
	def get_Source(self): # String
		return self.get_body_params().get('Source')

	def set_Source(self, Source):  # String
		self.add_body_params('Source', Source)
	def get_UserId(self): # String
		return self.get_body_params().get('UserId')

	def set_UserId(self, UserId):  # String
		self.add_body_params('UserId', UserId)
	def get_IcpType(self): # Integer
		return self.get_body_params().get('IcpType')

	def set_IcpType(self, IcpType):  # Integer
		self.add_body_params('IcpType', IcpType)
	def get_CompanyAddress(self): # String
		return self.get_body_params().get('CompanyAddress')

	def set_CompanyAddress(self, CompanyAddress):  # String
		self.add_body_params('CompanyAddress', CompanyAddress)
	def get_CompanyName(self): # String
		return self.get_body_params().get('CompanyName')

	def set_CompanyName(self, CompanyName):  # String
		self.add_body_params('CompanyName', CompanyName)
	def get_BizId(self): # String
		return self.get_body_params().get('BizId')

	def set_BizId(self, BizId):  # String
		self.add_body_params('BizId', BizId)
