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

class QueryGroupedSecurityEventMarkMissListRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Sas', '2018-12-03', 'QueryGroupedSecurityEventMarkMissList')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_Remark(self): # String
		return self.get_body_params().get('Remark')

	def set_Remark(self, Remark):  # String
		self.add_body_params('Remark', Remark)
	def get_EventName(self): # String
		return self.get_body_params().get('EventName')

	def set_EventName(self, EventName):  # String
		self.add_body_params('EventName', EventName)
	def get_DisposalWay(self): # String
		return self.get_query_params().get('DisposalWay')

	def set_DisposalWay(self, DisposalWay):  # String
		self.add_query_param('DisposalWay', DisposalWay)
	def get_SourceIp(self): # String
		return self.get_query_params().get('SourceIp')

	def set_SourceIp(self, SourceIp):  # String
		self.add_query_param('SourceIp', SourceIp)
	def get_PageSize(self): # Integer
		return self.get_body_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Integer
		self.add_body_params('PageSize', PageSize)
	def get_From(self): # String
		return self.get_body_params().get('From')

	def set_From(self, _From):  # String
		self.add_body_params('From', _From)
	def get_Lang(self): # String
		return self.get_body_params().get('Lang')

	def set_Lang(self, Lang):  # String
		self.add_body_params('Lang', Lang)
	def get_CurrentPage(self): # Integer
		return self.get_body_params().get('CurrentPage')

	def set_CurrentPage(self, CurrentPage):  # Integer
		self.add_body_params('CurrentPage', CurrentPage)
