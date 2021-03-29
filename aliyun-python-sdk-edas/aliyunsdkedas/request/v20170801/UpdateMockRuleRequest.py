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

from aliyunsdkcore.request import RoaRequest
from aliyunsdkedas.endpoint import endpoint_data

class UpdateMockRuleRequest(RoaRequest):

	def __init__(self):
		RoaRequest.__init__(self, 'Edas', '2017-08-01', 'UpdateMockRule','Edas')
		self.set_uri_pattern('/pop/sp/api/mock/updateMockRule')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ScMockItemJson(self):
		return self.get_query_params().get('ScMockItemJson')

	def set_ScMockItemJson(self,ScMockItemJson):
		self.add_query_param('ScMockItemJson',ScMockItemJson)

	def get_DubboMockItemJson(self):
		return self.get_query_params().get('DubboMockItemJson')

	def set_DubboMockItemJson(self,DubboMockItemJson):
		self.add_query_param('DubboMockItemJson',DubboMockItemJson)

	def get_ExtraJson(self):
		return self.get_query_params().get('ExtraJson')

	def set_ExtraJson(self,ExtraJson):
		self.add_query_param('ExtraJson',ExtraJson)

	def get_Name(self):
		return self.get_query_params().get('Name')

	def set_Name(self,Name):
		self.add_query_param('Name',Name)

	def get_Id(self):
		return self.get_query_params().get('Id')

	def set_Id(self,Id):
		self.add_query_param('Id',Id)

	def get_Region(self):
		return self.get_query_params().get('Region')

	def set_Region(self,Region):
		self.add_query_param('Region',Region)