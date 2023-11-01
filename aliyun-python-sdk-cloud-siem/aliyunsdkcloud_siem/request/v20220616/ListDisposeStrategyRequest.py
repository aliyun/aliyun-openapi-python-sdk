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

class ListDisposeStrategyRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'cloud-siem', '2022-06-16', 'ListDisposeStrategy','cloud-siem')
		self.set_method('POST')

	def get_EntityIdentity(self): # String
		return self.get_body_params().get('EntityIdentity')

	def set_EntityIdentity(self, EntityIdentity):  # String
		self.add_body_params('EntityIdentity', EntityIdentity)
	def get_PlaybookName(self): # String
		return self.get_body_params().get('PlaybookName')

	def set_PlaybookName(self, PlaybookName):  # String
		self.add_body_params('PlaybookName', PlaybookName)
	def get_PlaybookTypes(self): # String
		return self.get_body_params().get('PlaybookTypes')

	def set_PlaybookTypes(self, PlaybookTypes):  # String
		self.add_body_params('PlaybookTypes', PlaybookTypes)
	def get_StartTime(self): # Long
		return self.get_body_params().get('StartTime')

	def set_StartTime(self, StartTime):  # Long
		self.add_body_params('StartTime', StartTime)
	def get_PageSize(self): # Integer
		return self.get_body_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Integer
		self.add_body_params('PageSize', PageSize)
	def get_OrderField(self): # String
		return self.get_body_params().get('OrderField')

	def set_OrderField(self, OrderField):  # String
		self.add_body_params('OrderField', OrderField)
	def get_Order(self): # String
		return self.get_body_params().get('Order')

	def set_Order(self, Order):  # String
		self.add_body_params('Order', Order)
	def get_SophonTaskId(self): # String
		return self.get_body_params().get('SophonTaskId')

	def set_SophonTaskId(self, SophonTaskId):  # String
		self.add_body_params('SophonTaskId', SophonTaskId)
	def get_EffectiveStatus(self): # Integer
		return self.get_body_params().get('EffectiveStatus')

	def set_EffectiveStatus(self, EffectiveStatus):  # Integer
		self.add_body_params('EffectiveStatus', EffectiveStatus)
	def get_EndTime(self): # Long
		return self.get_body_params().get('EndTime')

	def set_EndTime(self, EndTime):  # Long
		self.add_body_params('EndTime', EndTime)
	def get_CurrentPage(self): # Integer
		return self.get_body_params().get('CurrentPage')

	def set_CurrentPage(self, CurrentPage):  # Integer
		self.add_body_params('CurrentPage', CurrentPage)
	def get_PlaybookUuid(self): # String
		return self.get_body_params().get('PlaybookUuid')

	def set_PlaybookUuid(self, PlaybookUuid):  # String
		self.add_body_params('PlaybookUuid', PlaybookUuid)
	def get_EntityType(self): # String
		return self.get_body_params().get('EntityType')

	def set_EntityType(self, EntityType):  # String
		self.add_body_params('EntityType', EntityType)
