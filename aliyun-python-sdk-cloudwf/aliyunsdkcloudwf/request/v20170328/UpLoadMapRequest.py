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
class UpLoadMapRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'cloudwf', '2017-03-28', 'UpLoadMap','cloudwf')

	def get_FileName(self):
		return self.get_query_params().get('FileName')

	def set_FileName(self,FileName):
		self.add_query_param('FileName',FileName)

	def get_UploadId(self):
		return self.get_query_params().get('UploadId')

	def set_UploadId(self,UploadId):
		self.add_query_param('UploadId',UploadId)

	def get_ObjectName(self):
		return self.get_query_params().get('ObjectName')

	def set_ObjectName(self,ObjectName):
		self.add_query_param('ObjectName',ObjectName)

	def get_ChunkIndex(self):
		return self.get_query_params().get('ChunkIndex')

	def set_ChunkIndex(self,ChunkIndex):
		self.add_query_param('ChunkIndex',ChunkIndex)

	def get_ChunkCnt(self):
		return self.get_query_params().get('ChunkCnt')

	def set_ChunkCnt(self,ChunkCnt):
		self.add_query_param('ChunkCnt',ChunkCnt)