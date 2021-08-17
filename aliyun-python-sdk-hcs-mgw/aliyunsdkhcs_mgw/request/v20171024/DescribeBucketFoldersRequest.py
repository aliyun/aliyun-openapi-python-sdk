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

class DescribeBucketFoldersRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'hcs-mgw', '2017-10-24', 'DescribeBucketFolders')
		self.set_method('POST')

	def get_Prefix(self):
		return self.get_query_params().get('Prefix')

	def set_Prefix(self,Prefix):
		self.add_query_param('Prefix',Prefix)

	def get_AccessKeySecret(self):
		return self.get_query_params().get('AccessKeySecret')

	def set_AccessKeySecret(self,AccessKeySecret):
		self.add_query_param('AccessKeySecret',AccessKeySecret)

	def get_Bucket(self):
		return self.get_query_params().get('Bucket')

	def set_Bucket(self,Bucket):
		self.add_query_param('Bucket',Bucket)

	def get_AccessKey(self):
		return self.get_query_params().get('AccessKey')

	def set_AccessKey(self,AccessKey):
		self.add_query_param('AccessKey',AccessKey)

	def get_Domain(self):
		return self.get_query_params().get('Domain')

	def set_Domain(self,Domain):
		self.add_query_param('Domain',Domain)