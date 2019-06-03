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
class SubscribeExportToOSSRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'BssOpenApi', '2017-12-14', 'SubscribeExportToOSS')

	def get_BucketOwnerId(self):
		return self.get_query_params().get('BucketOwnerId')

	def set_BucketOwnerId(self,BucketOwnerId):
		self.add_query_param('BucketOwnerId',BucketOwnerId)

	def get_SubscribeTypes(self):
		return self.get_query_params().get('SubscribeTypes')

	def set_SubscribeTypes(self,SubscribeTypes):
		for i in range(len(SubscribeTypes)):	
			if SubscribeTypes[i] is not None:
				self.add_query_param('SubscribeType.' + str(i + 1) , SubscribeTypes[i]);

	def get_SubscribeBucket(self):
		return self.get_query_params().get('SubscribeBucket')

	def set_SubscribeBucket(self,SubscribeBucket):
		self.add_query_param('SubscribeBucket',SubscribeBucket)