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
from aliyunsdkimm.endpoint import endpoint_data

class ListFaceGroupsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'imm', '2017-09-06', 'ListFaceGroups','imm')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_Project(self):
		return self.get_query_params().get('Project')

	def set_Project(self,Project):
		self.add_query_param('Project',Project)

	def get_RemarksBQuery(self):
		return self.get_query_params().get('RemarksBQuery')

	def set_RemarksBQuery(self,RemarksBQuery):
		self.add_query_param('RemarksBQuery',RemarksBQuery)

	def get_ExternalId(self):
		return self.get_query_params().get('ExternalId')

	def set_ExternalId(self,ExternalId):
		self.add_query_param('ExternalId',ExternalId)

	def get_Limit(self):
		return self.get_query_params().get('Limit')

	def set_Limit(self,Limit):
		self.add_query_param('Limit',Limit)

	def get_RemarksArrayBQuery(self):
		return self.get_query_params().get('RemarksArrayBQuery')

	def set_RemarksArrayBQuery(self,RemarksArrayBQuery):
		self.add_query_param('RemarksArrayBQuery',RemarksArrayBQuery)

	def get_Order(self):
		return self.get_query_params().get('Order')

	def set_Order(self,Order):
		self.add_query_param('Order',Order)

	def get_RemarksAQuery(self):
		return self.get_query_params().get('RemarksAQuery')

	def set_RemarksAQuery(self,RemarksAQuery):
		self.add_query_param('RemarksAQuery',RemarksAQuery)

	def get_OrderBy(self):
		return self.get_query_params().get('OrderBy')

	def set_OrderBy(self,OrderBy):
		self.add_query_param('OrderBy',OrderBy)

	def get_RemarksDQuery(self):
		return self.get_query_params().get('RemarksDQuery')

	def set_RemarksDQuery(self,RemarksDQuery):
		self.add_query_param('RemarksDQuery',RemarksDQuery)

	def get_RemarksArrayAQuery(self):
		return self.get_query_params().get('RemarksArrayAQuery')

	def set_RemarksArrayAQuery(self,RemarksArrayAQuery):
		self.add_query_param('RemarksArrayAQuery',RemarksArrayAQuery)

	def get_Marker(self):
		return self.get_query_params().get('Marker')

	def set_Marker(self,Marker):
		self.add_query_param('Marker',Marker)

	def get_SetId(self):
		return self.get_query_params().get('SetId')

	def set_SetId(self,SetId):
		self.add_query_param('SetId',SetId)

	def get_RemarksCQuery(self):
		return self.get_query_params().get('RemarksCQuery')

	def set_RemarksCQuery(self,RemarksCQuery):
		self.add_query_param('RemarksCQuery',RemarksCQuery)