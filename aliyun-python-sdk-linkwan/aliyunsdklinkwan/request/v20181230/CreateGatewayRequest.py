# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
class CreateGatewayRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'LinkWAN', '2018-12-30', 'CreateGateway','linkwan')
		self.set_protocol_type('https');

	def get_City(self):
		return self.get_body_params().get('City')

	def set_City(self,City):
		self.add_body_params('City', City)

	def get_Latitude(self):
		return self.get_body_params().get('Latitude')

	def set_Latitude(self,Latitude):
		self.add_body_params('Latitude', Latitude)

	def get_Description(self):
		return self.get_body_params().get('Description')

	def set_Description(self,Description):
		self.add_body_params('Description', Description)

	def get_AddressCode(self):
		return self.get_body_params().get('AddressCode')

	def set_AddressCode(self,AddressCode):
		self.add_body_params('AddressCode', AddressCode)

	def get_GisCoordinateSystem(self):
		return self.get_body_params().get('GisCoordinateSystem')

	def set_GisCoordinateSystem(self,GisCoordinateSystem):
		self.add_body_params('GisCoordinateSystem', GisCoordinateSystem)

	def get_Longitude(self):
		return self.get_body_params().get('Longitude')

	def set_Longitude(self,Longitude):
		self.add_body_params('Longitude', Longitude)

	def get_PinCode(self):
		return self.get_body_params().get('PinCode')

	def set_PinCode(self,PinCode):
		self.add_body_params('PinCode', PinCode)

	def get_Address(self):
		return self.get_body_params().get('Address')

	def set_Address(self,Address):
		self.add_body_params('Address', Address)

	def get_GwEui(self):
		return self.get_body_params().get('GwEui')

	def set_GwEui(self,GwEui):
		self.add_body_params('GwEui', GwEui)

	def get_FreqBandPlanGroupId(self):
		return self.get_body_params().get('FreqBandPlanGroupId')

	def set_FreqBandPlanGroupId(self,FreqBandPlanGroupId):
		self.add_body_params('FreqBandPlanGroupId', FreqBandPlanGroupId)

	def get_District(self):
		return self.get_body_params().get('District')

	def set_District(self,District):
		self.add_body_params('District', District)

	def get_Name(self):
		return self.get_body_params().get('Name')

	def set_Name(self,Name):
		self.add_body_params('Name', Name)

	def get_CommunicationMode(self):
		return self.get_body_params().get('CommunicationMode')

	def set_CommunicationMode(self,CommunicationMode):
		self.add_body_params('CommunicationMode', CommunicationMode)