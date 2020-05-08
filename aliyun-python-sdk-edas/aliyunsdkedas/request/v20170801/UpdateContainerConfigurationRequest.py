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
from aliyunsdkedas.endpoint import endpoint_data

class UpdateContainerConfigurationRequest(RoaRequest):

	def __init__(self):
		RoaRequest.__init__(self, 'Edas', '2017-08-01', 'UpdateContainerConfiguration','edas')
		self.set_uri_pattern('/pop/v5/app/container_config')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_UseBodyEncoding(self):
		return self.get_query_params().get('UseBodyEncoding')

	def set_UseBodyEncoding(self,UseBodyEncoding):
		self.add_query_param('UseBodyEncoding',UseBodyEncoding)

	def get_MaxThreads(self):
		return self.get_query_params().get('MaxThreads')

	def set_MaxThreads(self,MaxThreads):
		self.add_query_param('MaxThreads',MaxThreads)

	def get_URIEncoding(self):
		return self.get_query_params().get('URIEncoding')

	def set_URIEncoding(self,URIEncoding):
		self.add_query_param('URIEncoding',URIEncoding)

	def get_AppId(self):
		return self.get_query_params().get('AppId')

	def set_AppId(self,AppId):
		self.add_query_param('AppId',AppId)

	def get_GroupId(self):
		return self.get_query_params().get('GroupId')

	def set_GroupId(self,GroupId):
		self.add_query_param('GroupId',GroupId)

	def get_HttpPort(self):
		return self.get_query_params().get('HttpPort')

	def set_HttpPort(self,HttpPort):
		self.add_query_param('HttpPort',HttpPort)

	def get_ContextPath(self):
		return self.get_query_params().get('ContextPath')

	def set_ContextPath(self,ContextPath):
		self.add_query_param('ContextPath',ContextPath)