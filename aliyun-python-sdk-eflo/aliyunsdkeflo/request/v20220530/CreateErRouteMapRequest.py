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

class CreateErRouteMapRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'eflo', '2022-05-30', 'CreateErRouteMap','eflo')
		self.set_method('POST')

	def get_ReceptionInstanceType(self): # String
		return self.get_body_params().get('ReceptionInstanceType')

	def set_ReceptionInstanceType(self, ReceptionInstanceType):  # String
		self.add_body_params('ReceptionInstanceType', ReceptionInstanceType)
	def get_Description(self): # String
		return self.get_body_params().get('Description')

	def set_Description(self, Description):  # String
		self.add_body_params('Description', Description)
	def get_ReceptionInstanceId(self): # String
		return self.get_body_params().get('ReceptionInstanceId')

	def set_ReceptionInstanceId(self, ReceptionInstanceId):  # String
		self.add_body_params('ReceptionInstanceId', ReceptionInstanceId)
	def get_RouteMapAction(self): # String
		return self.get_body_params().get('RouteMapAction')

	def set_RouteMapAction(self, RouteMapAction):  # String
		self.add_body_params('RouteMapAction', RouteMapAction)
	def get_TransmissionInstanceType(self): # String
		return self.get_body_params().get('TransmissionInstanceType')

	def set_TransmissionInstanceType(self, TransmissionInstanceType):  # String
		self.add_body_params('TransmissionInstanceType', TransmissionInstanceType)
	def get_DestinationCidrBlock(self): # String
		return self.get_body_params().get('DestinationCidrBlock')

	def set_DestinationCidrBlock(self, DestinationCidrBlock):  # String
		self.add_body_params('DestinationCidrBlock', DestinationCidrBlock)
	def get_ErId(self): # String
		return self.get_body_params().get('ErId')

	def set_ErId(self, ErId):  # String
		self.add_body_params('ErId', ErId)
	def get_RouteMapNum(self): # Integer
		return self.get_body_params().get('RouteMapNum')

	def set_RouteMapNum(self, RouteMapNum):  # Integer
		self.add_body_params('RouteMapNum', RouteMapNum)
	def get_ReceptionInstanceOwner(self): # String
		return self.get_body_params().get('ReceptionInstanceOwner')

	def set_ReceptionInstanceOwner(self, ReceptionInstanceOwner):  # String
		self.add_body_params('ReceptionInstanceOwner', ReceptionInstanceOwner)
	def get_TransmissionInstanceOwner(self): # String
		return self.get_body_params().get('TransmissionInstanceOwner')

	def set_TransmissionInstanceOwner(self, TransmissionInstanceOwner):  # String
		self.add_body_params('TransmissionInstanceOwner', TransmissionInstanceOwner)
	def get_TransmissionInstanceId(self): # String
		return self.get_body_params().get('TransmissionInstanceId')

	def set_TransmissionInstanceId(self, TransmissionInstanceId):  # String
		self.add_body_params('TransmissionInstanceId', TransmissionInstanceId)
