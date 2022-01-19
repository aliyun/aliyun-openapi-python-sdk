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
from aliyunsdkdysmsapi.endpoint import endpoint_data

class AddSmsSignRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Dysmsapi', '2017-05-25', 'AddSmsSign')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_Remark(self):
		return self.get_query_params().get('Remark')

	def set_Remark(self,Remark):
		self.add_query_param('Remark',Remark)

	def get_SignName(self):
		return self.get_query_params().get('SignName')

	def set_SignName(self,SignName):
		self.add_query_param('SignName',SignName)

	def get_SignFileLists(self):
		return self.get_body_params().get('SignFileList')

	def set_SignFileLists(self, SignFileLists):
		for depth1 in range(len(SignFileLists)):
			if SignFileLists[depth1].get('FileContents') is not None:
				self.add_body_params('SignFileList.' + str(depth1 + 1) + '.FileContents', SignFileLists[depth1].get('FileContents'))
			if SignFileLists[depth1].get('FileSuffix') is not None:
				self.add_body_params('SignFileList.' + str(depth1 + 1) + '.FileSuffix', SignFileLists[depth1].get('FileSuffix'))

	def get_ResourceOwnerAccount(self):
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self,ResourceOwnerAccount):
		self.add_query_param('ResourceOwnerAccount',ResourceOwnerAccount)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_SignSource(self):
		return self.get_query_params().get('SignSource')

	def set_SignSource(self,SignSource):
		self.add_query_param('SignSource',SignSource)