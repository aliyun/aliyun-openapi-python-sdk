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
class MetastoreCreateTableRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Emr', '2016-04-08', 'MetastoreCreateTable')

	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_DbName(self):
		return self.get_query_params().get('DbName')

	def set_DbName(self,DbName):
		self.add_query_param('DbName',DbName)

	def get_TableName(self):
		return self.get_query_params().get('TableName')

	def set_TableName(self,TableName):
		self.add_query_param('TableName',TableName)

	def get_LocationUri(self):
		return self.get_query_params().get('LocationUri')

	def set_LocationUri(self,LocationUri):
		self.add_query_param('LocationUri',LocationUri)

	def get_FieldDelimiter(self):
		return self.get_query_params().get('FieldDelimiter')

	def set_FieldDelimiter(self,FieldDelimiter):
		self.add_query_param('FieldDelimiter',FieldDelimiter)

	def get_Columns(self):
		return self.get_query_params().get('Columns')

	def set_Columns(self,Columns):
		for i in range(len(Columns)):	
			self.add_query_param('Column.' + bytes(i + 1) + '.Name' , Columns[i].get('Name'))
			self.add_query_param('Column.' + bytes(i + 1) + '.Type' , Columns[i].get('Type'))
			self.add_query_param('Column.' + bytes(i + 1) + '.Comment' , Columns[i].get('Comment'))
