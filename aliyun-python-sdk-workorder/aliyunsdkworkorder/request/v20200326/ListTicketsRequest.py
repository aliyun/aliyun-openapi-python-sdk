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
from aliyunsdkworkorder.endpoint import endpoint_data

class ListTicketsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Workorder', '2020-03-26', 'ListTickets','workorder')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ProductCode(self):
		return self.get_query_params().get('ProductCode')

	def set_ProductCode(self,ProductCode):
		self.add_query_param('ProductCode',ProductCode)

	def get_Language(self):
		return self.get_query_params().get('Language')

	def set_Language(self,Language):
		self.add_query_param('Language',Language)

	def get_SubUserId(self):
		return self.get_query_params().get('SubUserId')

	def set_SubUserId(self,SubUserId):
		self.add_query_param('SubUserId',SubUserId)

	def get_CreatedBeforeTime(self):
		return self.get_query_params().get('CreatedBeforeTime')

	def set_CreatedBeforeTime(self,CreatedBeforeTime):
		self.add_query_param('CreatedBeforeTime',CreatedBeforeTime)

	def get_PageSize(self):
		return self.get_query_params().get('PageSize')

	def set_PageSize(self,PageSize):
		self.add_query_param('PageSize',PageSize)

	def get_Ids(self):
		return self.get_query_params().get('Ids')

	def set_Ids(self,Ids):
		self.add_query_param('Ids',Ids)

	def get_TicketStatus(self):
		return self.get_query_params().get('TicketStatus')

	def set_TicketStatus(self,TicketStatus):
		self.add_query_param('TicketStatus',TicketStatus)

	def get_PageStart(self):
		return self.get_query_params().get('PageStart')

	def set_PageStart(self,PageStart):
		self.add_query_param('PageStart',PageStart)

	def get_CreatedAfterTime(self):
		return self.get_query_params().get('CreatedAfterTime')

	def set_CreatedAfterTime(self,CreatedAfterTime):
		self.add_query_param('CreatedAfterTime',CreatedAfterTime)