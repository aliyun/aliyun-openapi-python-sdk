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

class PutBucketRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ens', '2017-11-10', 'PutBucket','ens')
		self.set_method('POST')

	def get_EnsRegionId(self): # String
		return self.get_body_params().get('EnsRegionId')

	def set_EnsRegionId(self, EnsRegionId):  # String
		self.add_body_params('EnsRegionId', EnsRegionId)
	def get_LogicalBucketType(self): # String
		return self.get_body_params().get('LogicalBucketType')

	def set_LogicalBucketType(self, LogicalBucketType):  # String
		self.add_body_params('LogicalBucketType', LogicalBucketType)
	def get_BucketName(self): # String
		return self.get_body_params().get('BucketName')

	def set_BucketName(self, BucketName):  # String
		self.add_body_params('BucketName', BucketName)
	def get_BucketAcl(self): # String
		return self.get_body_params().get('BucketAcl')

	def set_BucketAcl(self, BucketAcl):  # String
		self.add_body_params('BucketAcl', BucketAcl)
	def get_DispatchScope(self): # String
		return self.get_body_params().get('DispatchScope')

	def set_DispatchScope(self, DispatchScope):  # String
		self.add_body_params('DispatchScope', DispatchScope)
	def get_Comment(self): # String
		return self.get_body_params().get('Comment')

	def set_Comment(self, Comment):  # String
		self.add_body_params('Comment', Comment)
