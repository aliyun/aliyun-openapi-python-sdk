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
class DeleteTagsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ots', '2016-06-20', 'DeleteTags','ots')
		self.set_method('POST')

	def get_access_key_id(self):
		return self.get_query_params().get('access_key_id')

	def set_access_key_id(self,access_key_id):
		self.add_query_param('access_key_id',access_key_id)

	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_InstanceName(self):
		return self.get_query_params().get('InstanceName')

	def set_InstanceName(self,InstanceName):
		self.add_query_param('InstanceName',InstanceName)

	def get_TagInfos(self):
		return self.get_query_params().get('TagInfos')

	def set_TagInfos(self,TagInfos):
		for i in range(len(TagInfos)):	
			if TagInfos[i].get('TagKey') is not None:
				self.add_query_param('TagInfo.' + str(i + 1) + '.TagKey' , TagInfos[i].get('TagKey'))
			if TagInfos[i].get('TagValue') is not None:
				self.add_query_param('TagInfo.' + str(i + 1) + '.TagValue' , TagInfos[i].get('TagValue'))
