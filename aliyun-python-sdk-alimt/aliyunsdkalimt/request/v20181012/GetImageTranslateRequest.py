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
from aliyunsdkalimt.endpoint import endpoint_data

class GetImageTranslateRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'alimt', '2018-10-12', 'GetImageTranslate')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_SourceLanguage(self): # String
		return self.get_body_params().get('SourceLanguage')

	def set_SourceLanguage(self, SourceLanguage):  # String
		self.add_body_params('SourceLanguage', SourceLanguage)
	def get_Url(self): # String
		return self.get_body_params().get('Url')

	def set_Url(self, Url):  # String
		self.add_body_params('Url', Url)
	def get_Extra(self): # String
		return self.get_body_params().get('Extra')

	def set_Extra(self, Extra):  # String
		self.add_body_params('Extra', Extra)
	def get_TargetLanguage(self): # String
		return self.get_body_params().get('TargetLanguage')

	def set_TargetLanguage(self, TargetLanguage):  # String
		self.add_body_params('TargetLanguage', TargetLanguage)
