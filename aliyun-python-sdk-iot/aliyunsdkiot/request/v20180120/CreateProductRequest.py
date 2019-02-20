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
class CreateProductRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Iot', '2018-01-20', 'CreateProduct','iot')

	def get_DataFormat(self):
		return self.get_query_params().get('DataFormat')

	def set_DataFormat(self,DataFormat):
		self.add_query_param('DataFormat',DataFormat)

	def get_NodeType(self):
		return self.get_query_params().get('NodeType')

	def set_NodeType(self,NodeType):
		self.add_query_param('NodeType',NodeType)

	def get_Id2(self):
		return self.get_query_params().get('Id2')

	def set_Id2(self,Id2):
		self.add_query_param('Id2',Id2)

	def get_IotInstanceId(self):
		return self.get_query_params().get('IotInstanceId')

	def set_IotInstanceId(self,IotInstanceId):
		self.add_query_param('IotInstanceId',IotInstanceId)

	def get_NetType(self):
		return self.get_query_params().get('NetType')

	def set_NetType(self,NetType):
		self.add_query_param('NetType',NetType)

	def get_ProductName(self):
		return self.get_query_params().get('ProductName')

	def set_ProductName(self,ProductName):
		self.add_query_param('ProductName',ProductName)

	def get_Description(self):
		return self.get_query_params().get('Description')

	def set_Description(self,Description):
		self.add_query_param('Description',Description)

	def get_ProtocolType(self):
		return self.get_query_params().get('ProtocolType')

	def set_ProtocolType(self,ProtocolType):
		self.add_query_param('ProtocolType',ProtocolType)

	def get_AliyunCommodityCode(self):
		return self.get_query_params().get('AliyunCommodityCode')

	def set_AliyunCommodityCode(self,AliyunCommodityCode):
		self.add_query_param('AliyunCommodityCode',AliyunCommodityCode)

	def get_CategoryId(self):
		return self.get_query_params().get('CategoryId')

	def set_CategoryId(self,CategoryId):
		self.add_query_param('CategoryId',CategoryId)