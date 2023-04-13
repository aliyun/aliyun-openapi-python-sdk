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

class ListErRouteMapsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'eflo', '2022-05-30', 'ListErRouteMaps','eflo')
		self.set_method('POST')

	def get_ReceptionInstanceType(self): # String
		return self.get_body_params().get('ReceptionInstanceType')

	def set_ReceptionInstanceType(self, ReceptionInstanceType):  # String
		self.add_body_params('ReceptionInstanceType', ReceptionInstanceType)
	def get_ReceptionInstanceId(self): # String
		return self.get_body_params().get('ReceptionInstanceId')

	def set_ReceptionInstanceId(self, ReceptionInstanceId):  # String
		self.add_body_params('ReceptionInstanceId', ReceptionInstanceId)
	def get_ErRouteMapNum(self): # Integer
		return self.get_body_params().get('ErRouteMapNum')

	def set_ErRouteMapNum(self, ErRouteMapNum):  # Integer
		self.add_body_params('ErRouteMapNum', ErRouteMapNum)
	def get_PageNumber(self): # Integer
		return self.get_body_params().get('PageNumber')

	def set_PageNumber(self, PageNumber):  # Integer
		self.add_body_params('PageNumber', PageNumber)
	def get_RouteMapAction(self): # String
		return self.get_body_params().get('RouteMapAction')

	def set_RouteMapAction(self, RouteMapAction):  # String
		self.add_body_params('RouteMapAction', RouteMapAction)
	def get_TransmissionInstanceType(self): # String
		return self.get_body_params().get('TransmissionInstanceType')

	def set_TransmissionInstanceType(self, TransmissionInstanceType):  # String
		self.add_body_params('TransmissionInstanceType', TransmissionInstanceType)
	def get_PageSize(self): # Integer
		return self.get_body_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Integer
		self.add_body_params('PageSize', PageSize)
	def get_TransmissionInstanceName(self): # String
		return self.get_body_params().get('TransmissionInstanceName')

	def set_TransmissionInstanceName(self, TransmissionInstanceName):  # String
		self.add_body_params('TransmissionInstanceName', TransmissionInstanceName)
	def get_DestinationCidrBlock(self): # String
		return self.get_body_params().get('DestinationCidrBlock')

	def set_DestinationCidrBlock(self, DestinationCidrBlock):  # String
		self.add_body_params('DestinationCidrBlock', DestinationCidrBlock)
	def get_ErId(self): # String
		return self.get_body_params().get('ErId')

	def set_ErId(self, ErId):  # String
		self.add_body_params('ErId', ErId)
	def get_ErRouteMapId(self): # String
		return self.get_body_params().get('ErRouteMapId')

	def set_ErRouteMapId(self, ErRouteMapId):  # String
		self.add_body_params('ErRouteMapId', ErRouteMapId)
	def get_ReceptionInstanceName(self): # String
		return self.get_body_params().get('ReceptionInstanceName')

	def set_ReceptionInstanceName(self, ReceptionInstanceName):  # String
		self.add_body_params('ReceptionInstanceName', ReceptionInstanceName)
	def get_EnablePage(self): # Boolean
		return self.get_body_params().get('EnablePage')

	def set_EnablePage(self, EnablePage):  # Boolean
		self.add_body_params('EnablePage', EnablePage)
	def get_TransmissionInstanceId(self): # String
		return self.get_body_params().get('TransmissionInstanceId')

	def set_TransmissionInstanceId(self, TransmissionInstanceId):  # String
		self.add_body_params('TransmissionInstanceId', TransmissionInstanceId)
