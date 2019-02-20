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
class InvokeServiceRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'industry-brain', '2018-07-12', 'InvokeService')
		self.set_method('POST')

	def get_RequestParams(self):
		return self.get_query_params().get('RequestParams')

	def set_RequestParams(self,RequestParams):
		self.add_query_param('RequestParams',RequestParams)

	def get_ServiceId(self):
		return self.get_query_params().get('ServiceId')

	def set_ServiceId(self,ServiceId):
		self.add_query_param('ServiceId',ServiceId)

	def get_RequestData(self):
		return self.get_query_params().get('RequestData')

	def set_RequestData(self,RequestData):
		self.add_query_param('RequestData',RequestData)

	def get_ShowParams(self):
		return self.get_query_params().get('ShowParams')

	def set_ShowParams(self,ShowParams):
		self.add_query_param('ShowParams',ShowParams)