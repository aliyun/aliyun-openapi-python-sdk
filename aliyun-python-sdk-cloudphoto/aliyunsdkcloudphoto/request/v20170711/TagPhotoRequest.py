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
class TagPhotoRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'CloudPhoto', '2017-07-11', 'TagPhoto','cloudphoto')
		self.set_protocol_type('https');

	def get_LibraryId(self):
		return self.get_query_params().get('LibraryId')

	def set_LibraryId(self,LibraryId):
		self.add_query_param('LibraryId',LibraryId)

	def get_Confidences(self):
		return self.get_query_params().get('Confidences')

	def set_Confidences(self,Confidences):
		for i in range(len(Confidences)):	
			if Confidences[i] is not None:
				self.add_query_param('Confidence.' + str(i + 1) , Confidences[i]);

	def get_StoreName(self):
		return self.get_query_params().get('StoreName')

	def set_StoreName(self,StoreName):
		self.add_query_param('StoreName',StoreName)

	def get_PhotoId(self):
		return self.get_query_params().get('PhotoId')

	def set_PhotoId(self,PhotoId):
		self.add_query_param('PhotoId',PhotoId)

	def get_TagKeys(self):
		return self.get_query_params().get('TagKeys')

	def set_TagKeys(self,TagKeys):
		for i in range(len(TagKeys)):	
			if TagKeys[i] is not None:
				self.add_query_param('TagKey.' + str(i + 1) , TagKeys[i]);