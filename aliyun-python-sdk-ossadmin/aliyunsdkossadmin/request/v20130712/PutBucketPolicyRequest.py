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
class PutBucketPolicyRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'OssAdmin', '2013-07-12', 'PutBucketPolicy','ossadmin')

	def get_LogPrefix(self):
		return self.get_query_params().get('LogPrefix')

	def set_LogPrefix(self,LogPrefix):
		self.add_query_param('LogPrefix',LogPrefix)

	def get_OwnerAccount(self):
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self,OwnerAccount):
		self.add_query_param('OwnerAccount',OwnerAccount)

	def get_ErrorFile(self):
		return self.get_query_params().get('ErrorFile')

	def set_ErrorFile(self,ErrorFile):
		self.add_query_param('ErrorFile',ErrorFile)

	def get_IndexFile(self):
		return self.get_query_params().get('IndexFile')

	def set_IndexFile(self,IndexFile):
		self.add_query_param('IndexFile',IndexFile)

	def get_DisallowEmptyRefer(self):
		return self.get_query_params().get('DisallowEmptyRefer')

	def set_DisallowEmptyRefer(self,DisallowEmptyRefer):
		self.add_query_param('DisallowEmptyRefer',DisallowEmptyRefer)

	def get_uid(self):
		return self.get_query_params().get('uid')

	def set_uid(self,uid):
		self.add_query_param('uid',uid)

	def get_LogBucket(self):
		return self.get_query_params().get('LogBucket')

	def set_LogBucket(self,LogBucket):
		self.add_query_param('LogBucket',LogBucket)

	def get_BucketName(self):
		return self.get_query_params().get('BucketName')

	def set_BucketName(self,BucketName):
		self.add_query_param('BucketName',BucketName)

	def get_Location(self):
		return self.get_query_params().get('Location')

	def set_Location(self,Location):
		self.add_query_param('Location',Location)

	def get_bid(self):
		return self.get_query_params().get('bid')

	def set_bid(self,bid):
		self.add_query_param('bid',bid)

	def get_EnableDualCluster(self):
		return self.get_query_params().get('EnableDualCluster')

	def set_EnableDualCluster(self,EnableDualCluster):
		self.add_query_param('EnableDualCluster',EnableDualCluster)

	def get_WhiteReferList(self):
		return self.get_query_params().get('WhiteReferList')

	def set_WhiteReferList(self,WhiteReferList):
		self.add_query_param('WhiteReferList',WhiteReferList)

	def get_IamPolicy(self):
		return self.get_query_params().get('IamPolicy')

	def set_IamPolicy(self,IamPolicy):
		self.add_query_param('IamPolicy',IamPolicy)