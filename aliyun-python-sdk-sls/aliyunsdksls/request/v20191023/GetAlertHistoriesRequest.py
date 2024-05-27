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
from aliyunsdksls.endpoint import endpoint_data

class GetAlertHistoriesRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Sls', '2019-10-23', 'GetAlertHistories','sls')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_Line(self): # Integer
		return self.get_body_params().get('Line')

	def set_Line(self, Line):  # Integer
		self.add_body_params('Line', Line)
	def get_SlsAccessToken(self): # String
		return self.get_query_params().get('SlsAccessToken')

	def set_SlsAccessToken(self, SlsAccessToken):  # String
		self.add_query_param('SlsAccessToken', SlsAccessToken)
	def get_ToTs(self): # Integer
		return self.get_body_params().get('ToTs')

	def set_ToTs(self, ToTs):  # Integer
		self.add_body_params('ToTs', ToTs)
	def get_Endpoint(self): # String
		return self.get_body_params().get('Endpoint')

	def set_Endpoint(self, Endpoint):  # String
		self.add_body_params('Endpoint', Endpoint)
	def get_App(self): # String
		return self.get_body_params().get('App')

	def set_App(self, App):  # String
		self.add_body_params('App', App)
	def get_FromTs(self): # Integer
		return self.get_body_params().get('FromTs')

	def set_FromTs(self, FromTs):  # Integer
		self.add_body_params('FromTs', FromTs)
	def get_ProjectName(self): # String
		return self.get_body_params().get('ProjectName')

	def set_ProjectName(self, ProjectName):  # String
		self.add_body_params('ProjectName', ProjectName)
	def get_Offset(self): # Integer
		return self.get_body_params().get('Offset')

	def set_Offset(self, Offset):  # Integer
		self.add_body_params('Offset', Offset)
	def get_AlertId(self): # String
		return self.get_body_params().get('AlertId')

	def set_AlertId(self, AlertId):  # String
		self.add_body_params('AlertId', AlertId)
	def get_Region(self): # String
		return self.get_body_params().get('Region')

	def set_Region(self, Region):  # String
		self.add_body_params('Region', Region)
