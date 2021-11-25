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
from aliyunsdkimm.endpoint import endpoint_data

class GetWebofficeURLRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'imm', '2017-09-06', 'GetWebofficeURL','imm')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_SrcType(self): # String
		return self.get_query_params().get('SrcType')

	def set_SrcType(self, SrcType):  # String
		self.add_query_param('SrcType', SrcType)
	def get_Project(self): # String
		return self.get_query_params().get('Project')

	def set_Project(self, Project):  # String
		self.add_query_param('Project', Project)
	def get_File(self): # String
		return self.get_query_params().get('File')

	def set_File(self, File):  # String
		self.add_query_param('File', File)
	def get_Hidecmb(self): # Boolean
		return self.get_query_params().get('Hidecmb')

	def set_Hidecmb(self, Hidecmb):  # Boolean
		self.add_query_param('Hidecmb', Hidecmb)
	def get_NotifyEndpoint(self): # String
		return self.get_query_params().get('NotifyEndpoint')

	def set_NotifyEndpoint(self, NotifyEndpoint):  # String
		self.add_query_param('NotifyEndpoint', NotifyEndpoint)
	def get_FileID(self): # String
		return self.get_query_params().get('FileID')

	def set_FileID(self, FileID):  # String
		self.add_query_param('FileID', FileID)
	def get_Watermark(self): # String
		return self.get_query_params().get('Watermark')

	def set_Watermark(self, Watermark):  # String
		self.add_query_param('Watermark', Watermark)
	def get_NotifyTopicName(self): # String
		return self.get_query_params().get('NotifyTopicName')

	def set_NotifyTopicName(self, NotifyTopicName):  # String
		self.add_query_param('NotifyTopicName', NotifyTopicName)
	def get_Permission(self): # String
		return self.get_query_params().get('Permission')

	def set_Permission(self, Permission):  # String
		self.add_query_param('Permission', Permission)
	def get_User(self): # String
		return self.get_query_params().get('User')

	def set_User(self, User):  # String
		self.add_query_param('User', User)
