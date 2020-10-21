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
from aliyunsdksgw.endpoint import endpoint_data

class CreateGatewayBlockVolumeRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'sgw', '2018-05-11', 'CreateGatewayBlockVolume','hcs_sgw')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_OssEndpoint(self):
		return self.get_query_params().get('OssEndpoint')

	def set_OssEndpoint(self,OssEndpoint):
		self.add_query_param('OssEndpoint',OssEndpoint)

	def get_Recovery(self):
		return self.get_query_params().get('Recovery')

	def set_Recovery(self,Recovery):
		self.add_query_param('Recovery',Recovery)

	def get_SecurityToken(self):
		return self.get_query_params().get('SecurityToken')

	def set_SecurityToken(self,SecurityToken):
		self.add_query_param('SecurityToken',SecurityToken)

	def get_ChunkSize(self):
		return self.get_query_params().get('ChunkSize')

	def set_ChunkSize(self,ChunkSize):
		self.add_query_param('ChunkSize',ChunkSize)

	def get_GatewayId(self):
		return self.get_query_params().get('GatewayId')

	def set_GatewayId(self,GatewayId):
		self.add_query_param('GatewayId',GatewayId)

	def get_VolumeProtocol(self):
		return self.get_query_params().get('VolumeProtocol')

	def set_VolumeProtocol(self,VolumeProtocol):
		self.add_query_param('VolumeProtocol',VolumeProtocol)

	def get_ChapEnabled(self):
		return self.get_query_params().get('ChapEnabled')

	def set_ChapEnabled(self,ChapEnabled):
		self.add_query_param('ChapEnabled',ChapEnabled)

	def get_CacheMode(self):
		return self.get_query_params().get('CacheMode')

	def set_CacheMode(self,CacheMode):
		self.add_query_param('CacheMode',CacheMode)

	def get_LocalFilePath(self):
		return self.get_query_params().get('LocalFilePath')

	def set_LocalFilePath(self,LocalFilePath):
		self.add_query_param('LocalFilePath',LocalFilePath)

	def get_OssBucketSsl(self):
		return self.get_query_params().get('OssBucketSsl')

	def set_OssBucketSsl(self,OssBucketSsl):
		self.add_query_param('OssBucketSsl',OssBucketSsl)

	def get_Size(self):
		return self.get_query_params().get('Size')

	def set_Size(self,Size):
		self.add_query_param('Size',Size)

	def get_ChapInUser(self):
		return self.get_query_params().get('ChapInUser')

	def set_ChapInUser(self,ChapInUser):
		self.add_query_param('ChapInUser',ChapInUser)

	def get_Name(self):
		return self.get_query_params().get('Name')

	def set_Name(self,Name):
		self.add_query_param('Name',Name)

	def get_OssBucketName(self):
		return self.get_query_params().get('OssBucketName')

	def set_OssBucketName(self,OssBucketName):
		self.add_query_param('OssBucketName',OssBucketName)

	def get_ChapInPassword(self):
		return self.get_query_params().get('ChapInPassword')

	def set_ChapInPassword(self,ChapInPassword):
		self.add_query_param('ChapInPassword',ChapInPassword)