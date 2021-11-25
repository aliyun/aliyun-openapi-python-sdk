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

class GetOfficeEditURLRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'imm', '2017-09-06', 'GetOfficeEditURL','imm')
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
	def get_UserID(self): # String
		return self.get_query_params().get('UserID')

	def set_UserID(self, UserID):  # String
		self.add_query_param('UserID', UserID)
	def get_NotifyEndpoint(self): # String
		return self.get_query_params().get('NotifyEndpoint')

	def set_NotifyEndpoint(self, NotifyEndpoint):  # String
		self.add_query_param('NotifyEndpoint', NotifyEndpoint)
	def get_FileID(self): # String
		return self.get_query_params().get('FileID')

	def set_FileID(self, FileID):  # String
		self.add_query_param('FileID', FileID)
	def get_NotifyTopicName(self): # String
		return self.get_query_params().get('NotifyTopicName')

	def set_NotifyTopicName(self, NotifyTopicName):  # String
		self.add_query_param('NotifyTopicName', NotifyTopicName)
	def get_FileName(self): # String
		return self.get_query_params().get('FileName')

	def set_FileName(self, FileName):  # String
		self.add_query_param('FileName', FileName)
	def get_SrcUri(self): # String
		return self.get_query_params().get('SrcUri')

	def set_SrcUri(self, SrcUri):  # String
		self.add_query_param('SrcUri', SrcUri)
	def get_TgtUri(self): # String
		return self.get_query_params().get('TgtUri')

	def set_TgtUri(self, TgtUri):  # String
		self.add_query_param('TgtUri', TgtUri)
	def get_UserName(self): # String
		return self.get_query_params().get('UserName')

	def set_UserName(self, UserName):  # String
		self.add_query_param('UserName', UserName)
