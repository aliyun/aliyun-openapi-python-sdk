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

class DescribeAlertsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'cloud-siem', '2022-06-16', 'DescribeAlerts','cloud-siem')
		self.set_method('POST')

	def get_RoleFor(self): # Long
		return self.get_body_params().get('RoleFor')

	def set_RoleFor(self, RoleFor):  # Long
		self.add_body_params('RoleFor', RoleFor)
	def get_AlertName(self): # String
		return self.get_body_params().get('AlertName')

	def set_AlertName(self, AlertName):  # String
		self.add_body_params('AlertName', AlertName)
	def get_EntityName(self): # String
		return self.get_body_params().get('EntityName')

	def set_EntityName(self, EntityName):  # String
		self.add_body_params('EntityName', EntityName)
	def get_AssetName(self): # String
		return self.get_body_params().get('AssetName')

	def set_AssetName(self, AssetName):  # String
		self.add_body_params('AssetName', AssetName)
	def get_EntityId(self): # String
		return self.get_body_params().get('EntityId')

	def set_EntityId(self, EntityId):  # String
		self.add_body_params('EntityId', EntityId)
	def get_Source(self): # String
		return self.get_body_params().get('Source')

	def set_Source(self, Source):  # String
		self.add_body_params('Source', Source)
	def get_IsDefend(self): # String
		return self.get_body_params().get('IsDefend')

	def set_IsDefend(self, IsDefend):  # String
		self.add_body_params('IsDefend', IsDefend)
	def get_StartTime(self): # Long
		return self.get_body_params().get('StartTime')

	def set_StartTime(self, StartTime):  # Long
		self.add_body_params('StartTime', StartTime)
	def get_SubUserId(self): # String
		return self.get_body_params().get('SubUserId')

	def set_SubUserId(self, SubUserId):  # String
		self.add_body_params('SubUserId', SubUserId)
	def get_PageSize(self): # Integer
		return self.get_body_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Integer
		self.add_body_params('PageSize', PageSize)
	def get_RoleType(self): # Integer
		return self.get_body_params().get('RoleType')

	def set_RoleType(self, RoleType):  # Integer
		self.add_body_params('RoleType', RoleType)
	def get_Levels(self): # RepeatList
		return self.get_body_params().get('Level')

	def set_Levels(self, Level):  # RepeatList
		for depth1 in range(len(Level)):
			self.add_body_params('Level.' + str(depth1 + 1), Level[depth1])
	def get_EndTime(self): # Long
		return self.get_body_params().get('EndTime')

	def set_EndTime(self, EndTime):  # Long
		self.add_body_params('EndTime', EndTime)
	def get_AlertTitle(self): # String
		return self.get_body_params().get('AlertTitle')

	def set_AlertTitle(self, AlertTitle):  # String
		self.add_body_params('AlertTitle', AlertTitle)
	def get_CurrentPage(self): # Integer
		return self.get_body_params().get('CurrentPage')

	def set_CurrentPage(self, CurrentPage):  # Integer
		self.add_body_params('CurrentPage', CurrentPage)
	def get_AlertType(self): # String
		return self.get_body_params().get('AlertType')

	def set_AlertType(self, AlertType):  # String
		self.add_body_params('AlertType', AlertType)
	def get_AlertUuid(self): # String
		return self.get_body_params().get('AlertUuid')

	def set_AlertUuid(self, AlertUuid):  # String
		self.add_body_params('AlertUuid', AlertUuid)
	def get_AssetId(self): # String
		return self.get_body_params().get('AssetId')

	def set_AssetId(self, AssetId):  # String
		self.add_body_params('AssetId', AssetId)
	def get_LabelType(self): # String
		return self.get_body_params().get('LabelType')

	def set_LabelType(self, LabelType):  # String
		self.add_body_params('LabelType', LabelType)
