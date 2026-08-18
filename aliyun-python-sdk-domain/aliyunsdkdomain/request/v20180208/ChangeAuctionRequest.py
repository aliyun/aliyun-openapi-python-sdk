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
		RpcRequest.__init__(self, 'Domain', '2018-02-08', 'ChangeAuction','domain')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_AuctionLists(self): # RepeatList
		return self.get_body_params().get('AuctionList')

	def set_AuctionLists(self, AuctionList):  # RepeatList
		for depth1 in range(len(AuctionList)):
			if AuctionList[depth1].get('Winner') is not None:
				self.add_body_params('AuctionList.' + str(depth1 + 1) + '.Winner', AuctionList[depth1].get('Winner'))
			if AuctionList[depth1].get('ReserveRange') is not None:
				self.add_body_params('AuctionList.' + str(depth1 + 1) + '.ReserveRange', AuctionList[depth1].get('ReserveRange'))
			if AuctionList[depth1].get('DomainName') is not None:
				self.add_body_params('AuctionList.' + str(depth1 + 1) + '.DomainName', AuctionList[depth1].get('DomainName'))
			if AuctionList[depth1].get('EndTime') is not None:
				self.add_body_params('AuctionList.' + str(depth1 + 1) + '.EndTime', AuctionList[depth1].get('EndTime'))
			if AuctionList[depth1].get('TimeLeft') is not None:
				self.add_body_params('AuctionList.' + str(depth1 + 1) + '.TimeLeft', AuctionList[depth1].get('TimeLeft'))
			if AuctionList[depth1].get('BidRecords') is not None:
				for depth2 in range(len(AuctionList[depth1].get('BidRecords'))):
					if AuctionList[depth1].get('BidRecords')[depth2].get('CreateTime') is not None:
						self.add_body_params('AuctionList.' + str(depth1 + 1) + '.BidRecords.'  + str(depth2 + 1) + '.CreateTime', AuctionList[depth1].get('BidRecords')[depth2].get('CreateTime'))
					if AuctionList[depth1].get('BidRecords')[depth2].get('Price') is not None:
						self.add_body_params('AuctionList.' + str(depth1 + 1) + '.BidRecords.'  + str(depth2 + 1) + '.Price', AuctionList[depth1].get('BidRecords')[depth2].get('Price'))
					if AuctionList[depth1].get('BidRecords')[depth2].get('UserId') is not None:
						self.add_body_params('AuctionList.' + str(depth1 + 1) + '.BidRecords.'  + str(depth2 + 1) + '.UserId', AuctionList[depth1].get('BidRecords')[depth2].get('UserId'))
			if AuctionList[depth1].get('IsReserve') is not None:
				self.add_body_params('AuctionList.' + str(depth1 + 1) + '.IsReserve', AuctionList[depth1].get('IsReserve'))
			if AuctionList[depth1].get('Status') is not None:
				self.add_body_params('AuctionList.' + str(depth1 + 1) + '.Status', AuctionList[depth1].get('Status'))
			if AuctionList[depth1].get('WinnerPrice') is not None:
				self.add_body_params('AuctionList.' + str(depth1 + 1) + '.WinnerPrice', AuctionList[depth1].get('WinnerPrice'))
			if AuctionList[depth1].get('ReservePrice') is not None:
				self.add_body_params('AuctionList.' + str(depth1 + 1) + '.ReservePrice', AuctionList[depth1].get('ReservePrice'))
