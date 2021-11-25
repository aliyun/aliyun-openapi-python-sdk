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

class IndexVideoRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'imm', '2017-09-06', 'IndexVideo','imm')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_Project(self): # String
		return self.get_query_params().get('Project')

	def set_Project(self, Project):  # String
		self.add_query_param('Project', Project)
	def get_ExternalId(self): # String
		return self.get_query_params().get('ExternalId')

	def set_ExternalId(self, ExternalId):  # String
		self.add_query_param('ExternalId', ExternalId)
	def get_NotifyEndpoint(self): # String
		return self.get_query_params().get('NotifyEndpoint')

	def set_NotifyEndpoint(self, NotifyEndpoint):  # String
		self.add_query_param('NotifyEndpoint', NotifyEndpoint)
	def get_NotifyTopicName(self): # String
		return self.get_query_params().get('NotifyTopicName')

	def set_NotifyTopicName(self, NotifyTopicName):  # String
		self.add_query_param('NotifyTopicName', NotifyTopicName)
	def get_RemarksB(self): # String
		return self.get_query_params().get('RemarksB')

	def set_RemarksB(self, RemarksB):  # String
		self.add_query_param('RemarksB', RemarksB)
	def get_RemarksA(self): # String
		return self.get_query_params().get('RemarksA')

	def set_RemarksA(self, RemarksA):  # String
		self.add_query_param('RemarksA', RemarksA)
	def get_VideoUri(self): # String
		return self.get_query_params().get('VideoUri')

	def set_VideoUri(self, VideoUri):  # String
		self.add_query_param('VideoUri', VideoUri)
	def get_RemarksD(self): # String
		return self.get_query_params().get('RemarksD')

	def set_RemarksD(self, RemarksD):  # String
		self.add_query_param('RemarksD', RemarksD)
	def get_RemarksC(self): # String
		return self.get_query_params().get('RemarksC')

	def set_RemarksC(self, RemarksC):  # String
		self.add_query_param('RemarksC', RemarksC)
	def get_SetId(self): # String
		return self.get_query_params().get('SetId')

	def set_SetId(self, SetId):  # String
		self.add_query_param('SetId', SetId)
	def get_TgtUri(self): # String
		return self.get_query_params().get('TgtUri')

	def set_TgtUri(self, TgtUri):  # String
		self.add_query_param('TgtUri', TgtUri)
