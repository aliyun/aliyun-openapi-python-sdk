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
class CreateTransactionRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'CloudPhoto', '2017-07-11', 'CreateTransaction','cloudphoto')
		self.set_protocol_type('https');

	def get_Ext(self):
		return self.get_query_params().get('Ext')

	def set_Ext(self,Ext):
		self.add_query_param('Ext',Ext)

	def get_Size(self):
		return self.get_query_params().get('Size')

	def set_Size(self,Size):
		self.add_query_param('Size',Size)

	def get_LibraryId(self):
		return self.get_query_params().get('LibraryId')

	def set_LibraryId(self,LibraryId):
		self.add_query_param('LibraryId',LibraryId)

	def get_StoreName(self):
		return self.get_query_params().get('StoreName')

	def set_StoreName(self,StoreName):
		self.add_query_param('StoreName',StoreName)

	def get_Force(self):
		return self.get_query_params().get('Force')

	def set_Force(self,Force):
		self.add_query_param('Force',Force)

	def get_Md5(self):
		return self.get_query_params().get('Md5')

	def set_Md5(self,Md5):
		self.add_query_param('Md5',Md5)