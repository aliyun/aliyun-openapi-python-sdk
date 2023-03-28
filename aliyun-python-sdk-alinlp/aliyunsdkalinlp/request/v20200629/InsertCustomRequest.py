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
from aliyunsdkalinlp.endpoint import endpoint_data

class InsertCustomRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'alinlp', '2020-06-29', 'InsertCustom','alinlp')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_CustomUrl(self): # String
		return self.get_body_params().get('CustomUrl')

	def set_CustomUrl(self, CustomUrl):  # String
		self.add_body_params('CustomUrl', CustomUrl)
	def get_RegUrl(self): # String
		return self.get_body_params().get('RegUrl')

	def set_RegUrl(self, RegUrl):  # String
		self.add_body_params('RegUrl', RegUrl)
	def get_ServiceCode(self): # String
		return self.get_body_params().get('ServiceCode')

	def set_ServiceCode(self, ServiceCode):  # String
		self.add_body_params('ServiceCode', ServiceCode)
	def get_RegFileName(self): # String
		return self.get_body_params().get('RegFileName')

	def set_RegFileName(self, RegFileName):  # String
		self.add_body_params('RegFileName', RegFileName)
	def get_CustomFileName(self): # String
		return self.get_body_params().get('CustomFileName')

	def set_CustomFileName(self, CustomFileName):  # String
		self.add_body_params('CustomFileName', CustomFileName)
	def get_ApiId(self): # Integer
		return self.get_body_params().get('ApiId')

	def set_ApiId(self, ApiId):  # Integer
		self.add_body_params('ApiId', ApiId)
