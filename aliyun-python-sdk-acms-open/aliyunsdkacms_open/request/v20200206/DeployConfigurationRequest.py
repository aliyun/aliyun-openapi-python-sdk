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

from aliyunsdkcore.request import RoaRequest
from aliyunsdkacms_open.endpoint import endpoint_data

class DeployConfigurationRequest(RoaRequest):

	def __init__(self):
		RoaRequest.__init__(self, 'acms-open', '2020-02-06', 'DeployConfiguration','acms')
		self.set_uri_pattern('/diamond-ops/pop/configuration')
		self.set_method('PUT')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_DataId(self):
		return self.get_body_params().get('DataId')

	def set_DataId(self,DataId):
		self.add_body_params('DataId', DataId)

	def get_AppName(self):
		return self.get_body_params().get('AppName')

	def set_AppName(self,AppName):
		self.add_body_params('AppName', AppName)

	def get_NamespaceId(self):
		return self.get_body_params().get('NamespaceId')

	def set_NamespaceId(self,NamespaceId):
		self.add_body_params('NamespaceId', NamespaceId)

	def get_Type(self):
		return self.get_body_params().get('Type')

	def set_Type(self,Type):
		self.add_body_params('Type', Type)

	def get_Content(self):
		return self.get_body_params().get('Content')

	def set_Content(self,Content):
		self.add_body_params('Content', Content)

	def get_Group(self):
		return self.get_body_params().get('Group')

	def set_Group(self,Group):
		self.add_body_params('Group', Group)

	def get_Desc(self):
		return self.get_body_params().get('Desc')

	def set_Desc(self,Desc):
		self.add_body_params('Desc', Desc)

	def get_Tags(self):
		return self.get_body_params().get('Tags')

	def set_Tags(self,Tags):
		self.add_body_params('Tags', Tags)