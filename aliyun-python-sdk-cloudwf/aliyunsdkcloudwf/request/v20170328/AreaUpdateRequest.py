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
class AreaUpdateRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'cloudwf', '2017-03-28', 'AreaUpdate','cloudwf')

	def get_Name(self):
		return self.get_query_params().get('Name')

	def set_Name(self,Name):
		self.add_query_param('Name',Name)

	def get_Dids(self):
		return self.get_query_params().get('Dids')

	def set_Dids(self,Dids):
		self.add_query_param('Dids',Dids)

	def get_Aid(self):
		return self.get_query_params().get('Aid')

	def set_Aid(self,Aid):
		self.add_query_param('Aid',Aid)

	def get_Sid(self):
		return self.get_query_params().get('Sid')

	def set_Sid(self,Sid):
		self.add_query_param('Sid',Sid)