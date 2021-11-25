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

class UpdateFaceGroupRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'imm', '2017-09-06', 'UpdateFaceGroup','imm')
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
	def get_GroupId(self): # String
		return self.get_query_params().get('GroupId')

	def set_GroupId(self, GroupId):  # String
		self.add_query_param('GroupId', GroupId)
	def get_RemarksB(self): # String
		return self.get_query_params().get('RemarksB')

	def set_RemarksB(self, RemarksB):  # String
		self.add_query_param('RemarksB', RemarksB)
	def get_RemarksA(self): # String
		return self.get_query_params().get('RemarksA')

	def set_RemarksA(self, RemarksA):  # String
		self.add_query_param('RemarksA', RemarksA)
	def get_GroupName(self): # String
		return self.get_query_params().get('GroupName')

	def set_GroupName(self, GroupName):  # String
		self.add_query_param('GroupName', GroupName)
	def get_ResetItems(self): # String
		return self.get_query_params().get('ResetItems')

	def set_ResetItems(self, ResetItems):  # String
		self.add_query_param('ResetItems', ResetItems)
	def get_RemarksArrayA(self): # String
		return self.get_query_params().get('RemarksArrayA')

	def set_RemarksArrayA(self, RemarksArrayA):  # String
		self.add_query_param('RemarksArrayA', RemarksArrayA)
	def get_RemarksArrayB(self): # String
		return self.get_query_params().get('RemarksArrayB')

	def set_RemarksArrayB(self, RemarksArrayB):  # String
		self.add_query_param('RemarksArrayB', RemarksArrayB)
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
	def get_GroupCoverFaceId(self): # String
		return self.get_query_params().get('GroupCoverFaceId')

	def set_GroupCoverFaceId(self, GroupCoverFaceId):  # String
		self.add_query_param('GroupCoverFaceId', GroupCoverFaceId)
