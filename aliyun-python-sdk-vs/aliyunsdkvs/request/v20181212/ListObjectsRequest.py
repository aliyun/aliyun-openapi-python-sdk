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
from aliyunsdkvs.endpoint import endpoint_data

class ListObjectsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'vs', '2018-12-12', 'ListObjects','vs')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_MaxKeys(self):
		return self.get_query_params().get('MaxKeys')

	def set_MaxKeys(self,MaxKeys):
		self.add_query_param('MaxKeys',MaxKeys)

	def get_ContinuationToken(self):
		return self.get_query_params().get('ContinuationToken')

	def set_ContinuationToken(self,ContinuationToken):
		self.add_query_param('ContinuationToken',ContinuationToken)

	def get_Prefix(self):
		return self.get_query_params().get('Prefix')

	def set_Prefix(self,Prefix):
		self.add_query_param('Prefix',Prefix)

	def get_Delimiter(self):
		return self.get_query_params().get('Delimiter')

	def set_Delimiter(self,Delimiter):
		self.add_query_param('Delimiter',Delimiter)

	def get_BucketName(self):
		return self.get_query_params().get('BucketName')

	def set_BucketName(self,BucketName):
		self.add_query_param('BucketName',BucketName)

	def get_EncodingType(self):
		return self.get_query_params().get('EncodingType')

	def set_EncodingType(self,EncodingType):
		self.add_query_param('EncodingType',EncodingType)

	def get_StartAfter(self):
		return self.get_query_params().get('StartAfter')

	def set_StartAfter(self,StartAfter):
		self.add_query_param('StartAfter',StartAfter)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_Marker(self):
		return self.get_query_params().get('Marker')

	def set_Marker(self,Marker):
		self.add_query_param('Marker',Marker)