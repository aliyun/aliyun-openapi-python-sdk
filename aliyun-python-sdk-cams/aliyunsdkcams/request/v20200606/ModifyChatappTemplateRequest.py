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
from aliyunsdkcams.endpoint import endpoint_data
import json

class ModifyChatappTemplateRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'cams', '2020-06-06', 'ModifyChatappTemplate')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_Components(self): # Array
		return self.get_body_params().get('Components')

	def set_Components(self, Components):  # Array
		self.add_body_params("Components", json.dumps(Components))
	def get_Language(self): # String
		return self.get_body_params().get('Language')

	def set_Language(self, Language):  # String
		self.add_body_params('Language', Language)
	def get_CustWabaId(self): # String
		return self.get_body_params().get('CustWabaId')

	def set_CustWabaId(self, CustWabaId):  # String
		self.add_body_params('CustWabaId', CustWabaId)
	def get_Example(self): # Map
		return self.get_body_params().get('Example')

	def set_Example(self, Example):  # Map
		self.add_body_params("Example", json.dumps(Example))
	def get_TemplateType(self): # String
		return self.get_body_params().get('TemplateType')

	def set_TemplateType(self, TemplateType):  # String
		self.add_body_params('TemplateType', TemplateType)
	def get_IsvCode(self): # String
		return self.get_body_params().get('IsvCode')

	def set_IsvCode(self, IsvCode):  # String
		self.add_body_params('IsvCode', IsvCode)
	def get_CustSpaceId(self): # String
		return self.get_body_params().get('CustSpaceId')

	def set_CustSpaceId(self, CustSpaceId):  # String
		self.add_body_params('CustSpaceId', CustSpaceId)
	def get_Category(self): # String
		return self.get_body_params().get('Category')

	def set_Category(self, Category):  # String
		self.add_body_params('Category', Category)
	def get_TemplateCode(self): # String
		return self.get_body_params().get('TemplateCode')

	def set_TemplateCode(self, TemplateCode):  # String
		self.add_body_params('TemplateCode', TemplateCode)
