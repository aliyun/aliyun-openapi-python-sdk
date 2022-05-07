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
from aliyunsdkvpc.endpoint import endpoint_data

class ListVpnCertificateAssociationsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Vpc', '2016-04-28', 'ListVpnCertificateAssociations','vpc')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_CertificateIds(self): # RepeatList
		return self.get_query_params().get('CertificateId')

	def set_CertificateIds(self, CertificateId):  # RepeatList
		for depth1 in range(len(CertificateId)):
			self.add_query_param('CertificateId.' + str(depth1 + 1), CertificateId[depth1])
	def get_VpnGatewayIds(self): # RepeatList
		return self.get_query_params().get('VpnGatewayId')

	def set_VpnGatewayIds(self, VpnGatewayId):  # RepeatList
		for depth1 in range(len(VpnGatewayId)):
			self.add_query_param('VpnGatewayId.' + str(depth1 + 1), VpnGatewayId[depth1])
	def get_CertificateType(self): # String
		return self.get_query_params().get('CertificateType')

	def set_CertificateType(self, CertificateType):  # String
		self.add_query_param('CertificateType', CertificateType)
	def get_NextToken(self): # String
		return self.get_query_params().get('NextToken')

	def set_NextToken(self, NextToken):  # String
		self.add_query_param('NextToken', NextToken)
	def get_MaxResults(self): # Integer
		return self.get_query_params().get('MaxResults')

	def set_MaxResults(self, MaxResults):  # Integer
		self.add_query_param('MaxResults', MaxResults)
