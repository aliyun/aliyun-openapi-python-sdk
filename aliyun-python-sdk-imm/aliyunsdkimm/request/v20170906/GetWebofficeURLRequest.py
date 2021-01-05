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


	def get_SrcType(self):
		return self.get_query_params().get('SrcType')

	def set_SrcType(self,SrcType):
		self.add_query_param('SrcType',SrcType)

	def get_Project(self):
		return self.get_query_params().get('Project')

	def set_Project(self,Project):
		self.add_query_param('Project',Project)

	def get_File(self):
		return self.get_query_params().get('File')

	def set_File(self,File):
		self.add_query_param('File',File)

	def get_NotifyEndpoint(self):
		return self.get_query_params().get('NotifyEndpoint')

	def set_NotifyEndpoint(self,NotifyEndpoint):
		self.add_query_param('NotifyEndpoint',NotifyEndpoint)

	def get_FileID(self):
		return self.get_query_params().get('FileID')

	def set_FileID(self,FileID):
		self.add_query_param('FileID',FileID)

	def get_NotifyTopicName(self):
		return self.get_query_params().get('NotifyTopicName')

	def set_NotifyTopicName(self,NotifyTopicName):
		self.add_query_param('NotifyTopicName',NotifyTopicName)

	def get_Permission(self):
		return self.get_query_params().get('Permission')

	def set_Permission(self,Permission):
		self.add_query_param('Permission',Permission)

	def get_User(self):
		return self.get_query_params().get('User')

	def set_User(self,User):
		self.add_query_param('User',User)