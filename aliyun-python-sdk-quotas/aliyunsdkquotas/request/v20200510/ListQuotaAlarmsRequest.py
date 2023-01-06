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
from aliyunsdkquotas.endpoint import endpoint_data

class ListQuotaAlarmsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'quotas', '2020-05-10', 'ListQuotaAlarms','quotas')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ProductCode(self): # String
		return self.get_body_params().get('ProductCode')

	def set_ProductCode(self, ProductCode):  # String
		self.add_body_params('ProductCode', ProductCode)
	def get_QuotaActionCode(self): # String
		return self.get_body_params().get('QuotaActionCode')

	def set_QuotaActionCode(self, QuotaActionCode):  # String
		self.add_body_params('QuotaActionCode', QuotaActionCode)
	def get_NextToken(self): # String
		return self.get_body_params().get('NextToken')

	def set_NextToken(self, NextToken):  # String
		self.add_body_params('NextToken', NextToken)
	def get_QuotaDimensionss(self): # RepeatList
		return self.get_body_params().get('QuotaDimensions')

	def set_QuotaDimensionss(self, QuotaDimensions):  # RepeatList
		for depth1 in range(len(QuotaDimensions)):
			if QuotaDimensions[depth1].get('Key') is not None:
				self.add_body_params('QuotaDimensions.' + str(depth1 + 1) + '.Key', QuotaDimensions[depth1].get('Key'))
			if QuotaDimensions[depth1].get('Value') is not None:
				self.add_body_params('QuotaDimensions.' + str(depth1 + 1) + '.Value', QuotaDimensions[depth1].get('Value'))
	def get_MaxResults(self): # Integer
		return self.get_body_params().get('MaxResults')

	def set_MaxResults(self, MaxResults):  # Integer
		self.add_body_params('MaxResults', MaxResults)
	def get_AlarmName(self): # String
		return self.get_body_params().get('AlarmName')

	def set_AlarmName(self, AlarmName):  # String
		self.add_body_params('AlarmName', AlarmName)
