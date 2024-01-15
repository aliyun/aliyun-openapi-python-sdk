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
from aliyunsdkiot.endpoint import endpoint_data

class CreateProductRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Iot', '2018-01-20', 'CreateProduct','iot')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_NodeType(self):
		return self.get_query_params().get('NodeType')

	def set_NodeType(self,NodeType):
		self.add_query_param('NodeType',NodeType)

	def get_Description(self):
		return self.get_query_params().get('Description')

	def set_Description(self,Description):
		self.add_query_param('Description',Description)

	def get_CategoryKey(self):
		return self.get_query_params().get('CategoryKey')

	def set_CategoryKey(self,CategoryKey):
		self.add_query_param('CategoryKey',CategoryKey)

	def get_JoinPermissionId(self):
		return self.get_query_params().get('JoinPermissionId')

	def set_JoinPermissionId(self,JoinPermissionId):
		self.add_query_param('JoinPermissionId',JoinPermissionId)

	def get_AuthType(self):
		return self.get_query_params().get('AuthType')

	def set_AuthType(self,AuthType):
		self.add_query_param('AuthType',AuthType)

	def get_ResourceGroupId(self):
		return self.get_query_params().get('ResourceGroupId')

	def set_ResourceGroupId(self,ResourceGroupId):
		self.add_query_param('ResourceGroupId',ResourceGroupId)

	def get_ValidateType(self):
		return self.get_query_params().get('ValidateType')

	def set_ValidateType(self,ValidateType):
		self.add_query_param('ValidateType',ValidateType)

	def get_IotInstanceId(self):
		return self.get_query_params().get('IotInstanceId')

	def set_IotInstanceId(self,IotInstanceId):
		self.add_query_param('IotInstanceId',IotInstanceId)

	def get_ProductName(self):
		return self.get_query_params().get('ProductName')

	def set_ProductName(self,ProductName):
		self.add_query_param('ProductName',ProductName)

	def get_AliyunCommodityCode(self):
		return self.get_query_params().get('AliyunCommodityCode')

	def set_AliyunCommodityCode(self,AliyunCommodityCode):
		self.add_query_param('AliyunCommodityCode',AliyunCommodityCode)

	def get_PublishAuto(self):
		return self.get_query_params().get('PublishAuto')

	def set_PublishAuto(self,PublishAuto):
		self.add_query_param('PublishAuto',PublishAuto)

	def get_DataFormat(self):
		return self.get_query_params().get('DataFormat')

	def set_DataFormat(self,DataFormat):
		self.add_query_param('DataFormat',DataFormat)

	def get_Id2(self):
		return self.get_query_params().get('Id2')

	def set_Id2(self,Id2):
		self.add_query_param('Id2',Id2)

	def get_NetType(self):
		return self.get_query_params().get('NetType')

	def set_NetType(self,NetType):
		self.add_query_param('NetType',NetType)

	def get_ProtocolType(self):
		return self.get_query_params().get('ProtocolType')

	def set_ProtocolType(self,ProtocolType):
		self.add_query_param('ProtocolType',ProtocolType)