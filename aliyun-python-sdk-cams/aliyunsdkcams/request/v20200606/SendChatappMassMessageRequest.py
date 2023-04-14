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

class SendChatappMassMessageRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'cams', '2020-06-06', 'SendChatappMassMessage')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_Language(self): # String
		return self.get_body_params().get('Language')

	def set_Language(self, Language):  # String
		self.add_body_params('Language', Language)
	def get_CustWabaId(self): # String
		return self.get_body_params().get('CustWabaId')

	def set_CustWabaId(self, CustWabaId):  # String
		self.add_body_params('CustWabaId', CustWabaId)
	def get_FallBackContent(self): # String
		return self.get_body_params().get('FallBackContent')

	def set_FallBackContent(self, FallBackContent):  # String
		self.add_body_params('FallBackContent', FallBackContent)
	def get_SenderList(self): # Array
		return self.get_body_params().get('SenderList')

	def set_SenderList(self, SenderList):  # Array
		self.add_body_params("SenderList", json.dumps(SenderList))
	def get_ChannelType(self): # String
		return self.get_body_params().get('ChannelType')

	def set_ChannelType(self, ChannelType):  # String
		self.add_body_params('ChannelType', ChannelType)
	def get_From(self): # String
		return self.get_body_params().get('From')

	def set_From(self, _From):  # String
		self.add_body_params('From', _From)
	def get_Tag(self): # String
		return self.get_body_params().get('Tag')

	def set_Tag(self, Tag):  # String
		self.add_body_params('Tag', Tag)
	def get_TaskId(self): # String
		return self.get_body_params().get('TaskId')

	def set_TaskId(self, TaskId):  # String
		self.add_body_params('TaskId', TaskId)
	def get_IsvCode(self): # String
		return self.get_body_params().get('IsvCode')

	def set_IsvCode(self, IsvCode):  # String
		self.add_body_params('IsvCode', IsvCode)
	def get_Label(self): # String
		return self.get_body_params().get('Label')

	def set_Label(self, Label):  # String
		self.add_body_params('Label', Label)
	def get_FallBackId(self): # String
		return self.get_body_params().get('FallBackId')

	def set_FallBackId(self, FallBackId):  # String
		self.add_body_params('FallBackId', FallBackId)
	def get_Ttl(self): # Long
		return self.get_body_params().get('Ttl')

	def set_Ttl(self, Ttl):  # Long
		self.add_body_params('Ttl', Ttl)
	def get_FallBackDuration(self): # Integer
		return self.get_body_params().get('FallBackDuration')

	def set_FallBackDuration(self, FallBackDuration):  # Integer
		self.add_body_params('FallBackDuration', FallBackDuration)
	def get_CustSpaceId(self): # String
		return self.get_body_params().get('CustSpaceId')

	def set_CustSpaceId(self, CustSpaceId):  # String
		self.add_body_params('CustSpaceId', CustSpaceId)
	def get_TemplateCode(self): # String
		return self.get_body_params().get('TemplateCode')

	def set_TemplateCode(self, TemplateCode):  # String
		self.add_body_params('TemplateCode', TemplateCode)
