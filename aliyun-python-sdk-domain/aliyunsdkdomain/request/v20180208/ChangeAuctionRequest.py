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

class ChangeAuctionRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Domain', '2018-02-08', 'ChangeAuction')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_AuctionLists(self):
		return self.get_body_params().get('AuctionList')

	def set_AuctionLists(self, AuctionLists):
		for depth1 in range(len(AuctionLists)):
			if AuctionLists[depth1].get('Winner') is not None:
				self.add_body_params('AuctionList.' + str(depth1 + 1) + '.Winner', AuctionLists[depth1].get('Winner'))
			if AuctionLists[depth1].get('ReserveRange') is not None:
				self.add_body_params('AuctionList.' + str(depth1 + 1) + '.ReserveRange', AuctionLists[depth1].get('ReserveRange'))
			if AuctionLists[depth1].get('DomainName') is not None:
				self.add_body_params('AuctionList.' + str(depth1 + 1) + '.DomainName', AuctionLists[depth1].get('DomainName'))
			if AuctionLists[depth1].get('EndTime') is not None:
				self.add_body_params('AuctionList.' + str(depth1 + 1) + '.EndTime', AuctionLists[depth1].get('EndTime'))
			if AuctionLists[depth1].get('TimeLeft') is not None:
				self.add_body_params('AuctionList.' + str(depth1 + 1) + '.TimeLeft', AuctionLists[depth1].get('TimeLeft'))
			if AuctionLists[depth1].get('IsReserve') is not None:
				self.add_body_params('AuctionList.' + str(depth1 + 1) + '.IsReserve', AuctionLists[depth1].get('IsReserve'))
			if AuctionLists[depth1].get('BidRecords') is not None:
				for depth2 in range(len(AuctionLists[depth1].get('BidRecords'))):
					if AuctionLists[depth1].get('BidRecords')[depth2].get('CreateTime') is not None:
						self.add_body_params('AuctionList.' + str(depth1 + 1) + '.BidRecords.' + str(depth2 + 1) + '.CreateTime', AuctionLists[depth1].get('BidRecords')[depth2].get('CreateTime'))
					if AuctionLists[depth1].get('BidRecords')[depth2].get('Price') is not None:
						self.add_body_params('AuctionList.' + str(depth1 + 1) + '.BidRecords.' + str(depth2 + 1) + '.Price', AuctionLists[depth1].get('BidRecords')[depth2].get('Price'))
					if AuctionLists[depth1].get('BidRecords')[depth2].get('UserId') is not None:
						self.add_body_params('AuctionList.' + str(depth1 + 1) + '.BidRecords.' + str(depth2 + 1) + '.UserId', AuctionLists[depth1].get('BidRecords')[depth2].get('UserId'))
			if AuctionLists[depth1].get('WinnerPrice') is not None:
				self.add_body_params('AuctionList.' + str(depth1 + 1) + '.WinnerPrice', AuctionLists[depth1].get('WinnerPrice'))
			if AuctionLists[depth1].get('Status') is not None:
				self.add_body_params('AuctionList.' + str(depth1 + 1) + '.Status', AuctionLists[depth1].get('Status'))
			if AuctionLists[depth1].get('ReservePrice') is not None:
				self.add_body_params('AuctionList.' + str(depth1 + 1) + '.ReservePrice', AuctionLists[depth1].get('ReservePrice'))