# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
class CreateTicketRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ccs', '2017-10-01', 'CreateTicket','ccs')
		self.set_method('POST')

	def get_CreatorId(self):
		return self.get_query_params().get('CreatorId')

	def set_CreatorId(self,CreatorId):
		self.add_query_param('CreatorId',CreatorId)

	def get_Description(self):
		return self.get_query_params().get('Description')

	def set_Description(self,Description):
		self.add_query_param('Description',Description)

	def get_Type(self):
		return self.get_query_params().get('Type')

	def set_Type(self,Type):
		self.add_query_param('Type',Type)

	def get_CcsInstanceId(self):
		return self.get_query_params().get('CcsInstanceId')

	def set_CcsInstanceId(self,CcsInstanceId):
		self.add_query_param('CcsInstanceId',CcsInstanceId)

	def get_CustomFields(self):
		return self.get_query_params().get('CustomFields')

	def set_CustomFields(self,CustomFields):
		self.add_query_param('CustomFields',CustomFields)