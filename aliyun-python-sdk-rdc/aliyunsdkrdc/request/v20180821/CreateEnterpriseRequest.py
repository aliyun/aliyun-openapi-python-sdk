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
from aliyunsdkrdc.endpoint import endpoint_data

class CreateEnterpriseRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Rdc', '2018-08-21', 'CreateEnterprise','rdc')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_Emails(self):
		return self.get_query_params().get('Emails')

	def set_Emails(self,Emails):
		self.add_query_param('Emails',Emails)

	def get_CreatorStaffId(self):
		return self.get_query_params().get('CreatorStaffId')

	def set_CreatorStaffId(self,CreatorStaffId):
		self.add_query_param('CreatorStaffId',CreatorStaffId)

	def get_Domain(self):
		return self.get_query_params().get('Domain')

	def set_Domain(self,Domain):
		self.add_query_param('Domain',Domain)

	def get_Name(self):
		return self.get_query_params().get('Name')

	def set_Name(self,Name):
		self.add_query_param('Name',Name)

	def get_Description(self):
		return self.get_query_params().get('Description')

	def set_Description(self,Description):
		self.add_query_param('Description',Description)