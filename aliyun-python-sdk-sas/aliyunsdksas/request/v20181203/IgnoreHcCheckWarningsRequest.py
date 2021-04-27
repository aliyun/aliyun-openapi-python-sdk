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
from aliyunsdksas.endpoint import endpoint_data

class IgnoreHcCheckWarningsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Sas', '2018-12-03', 'IgnoreHcCheckWarnings','sas')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_Reason(self):
		return self.get_query_params().get('Reason')

	def set_Reason(self,Reason):
		self.add_query_param('Reason',Reason)

	def get_CheckIds(self):
		return self.get_query_params().get('CheckIds')

	def set_CheckIds(self,CheckIds):
		self.add_query_param('CheckIds',CheckIds)

	def get_RiskId(self):
		return self.get_query_params().get('RiskId')

	def set_RiskId(self,RiskId):
		self.add_query_param('RiskId',RiskId)

	def get_Type(self):
		return self.get_query_params().get('Type')

	def set_Type(self,Type):
		self.add_query_param('Type',Type)

	def get_SourceIp(self):
		return self.get_query_params().get('SourceIp')

	def set_SourceIp(self,SourceIp):
		self.add_query_param('SourceIp',SourceIp)

	def get_CheckWarningIds(self):
		return self.get_query_params().get('CheckWarningIds')

	def set_CheckWarningIds(self,CheckWarningIds):
		self.add_query_param('CheckWarningIds',CheckWarningIds)