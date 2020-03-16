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

class PutExporterOutputRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Cms', '2019-01-01', 'PutExporterOutput','cms')
		self.set_method('POST')

	def get_DestName(self):
		return self.get_query_params().get('DestName')

	def set_DestName(self,DestName):
		self.add_query_param('DestName',DestName)

	def get_ConfigJson(self):
		return self.get_query_params().get('ConfigJson')

	def set_ConfigJson(self,ConfigJson):
		self.add_query_param('ConfigJson',ConfigJson)

	def get_DestType(self):
		return self.get_query_params().get('DestType')

	def set_DestType(self,DestType):
		self.add_query_param('DestType',DestType)

	def get_Desc(self):
		return self.get_query_params().get('Desc')

	def set_Desc(self,Desc):
		self.add_query_param('Desc',Desc)