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
from aliyunsdkdomain.endpoint import endpoint_data

class UpdatePartnerReservePriceRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Domain', '2018-02-08', 'UpdatePartnerReservePrice','domain')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_PartnerType(self): # String
		return self.get_body_params().get('PartnerType')

	def set_PartnerType(self, PartnerType):  # String
		self.add_body_params('PartnerType', PartnerType)
	def get_DomainName(self): # String
		return self.get_body_params().get('DomainName')

	def set_DomainName(self, DomainName):  # String
		self.add_body_params('DomainName', DomainName)
	def get_BiddingId(self): # Integer
		return self.get_body_params().get('BiddingId')

	def set_BiddingId(self, BiddingId):  # Integer
		self.add_body_params('BiddingId', BiddingId)
	def get_ReservePrice(self): # Double
		return self.get_body_params().get('ReservePrice')

	def set_ReservePrice(self, ReservePrice):  # Double
		self.add_body_params('ReservePrice', ReservePrice)
