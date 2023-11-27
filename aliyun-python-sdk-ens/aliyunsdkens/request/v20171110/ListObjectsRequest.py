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

class ListObjectsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ens', '2017-11-10', 'ListObjects','ens')
		self.set_method('POST')

	def get_MaxKeys(self): # Long
		return self.get_query_params().get('MaxKeys')

	def set_MaxKeys(self, MaxKeys):  # Long
		self.add_query_param('MaxKeys', MaxKeys)
	def get_ContinuationToken(self): # String
		return self.get_query_params().get('ContinuationToken')

	def set_ContinuationToken(self, ContinuationToken):  # String
		self.add_query_param('ContinuationToken', ContinuationToken)
	def get_Prefix(self): # String
		return self.get_query_params().get('Prefix')

	def set_Prefix(self, Prefix):  # String
		self.add_query_param('Prefix', Prefix)
	def get_Marker(self): # String
		return self.get_query_params().get('Marker')

	def set_Marker(self, Marker):  # String
		self.add_query_param('Marker', Marker)
	def get_BucketName(self): # String
		return self.get_query_params().get('BucketName')

	def set_BucketName(self, BucketName):  # String
		self.add_query_param('BucketName', BucketName)
	def get_EncodingType(self): # String
		return self.get_query_params().get('EncodingType')

	def set_EncodingType(self, EncodingType):  # String
		self.add_query_param('EncodingType', EncodingType)
	def get_StartAfter(self): # String
		return self.get_query_params().get('StartAfter')

	def set_StartAfter(self, StartAfter):  # String
		self.add_query_param('StartAfter', StartAfter)
