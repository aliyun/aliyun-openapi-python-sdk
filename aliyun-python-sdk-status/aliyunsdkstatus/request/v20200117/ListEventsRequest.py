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

class ListEventsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Status', '2020-01-17', 'ListEvents','StatusAPI')

	def get_EndDate(self):
		return self.get_query_params().get('EndDate')

	def set_EndDate(self,EndDate):
		self.add_query_param('EndDate',EndDate)

	def get_ProductId(self):
		return self.get_query_params().get('ProductId')

	def set_ProductId(self,ProductId):
		self.add_query_param('ProductId',ProductId)

	def get_NumOfDay(self):
		return self.get_query_params().get('NumOfDay')

	def set_NumOfDay(self,NumOfDay):
		self.add_query_param('NumOfDay',NumOfDay)