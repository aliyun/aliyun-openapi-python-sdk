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
from aliyunsdkcams.endpoint import endpoint_data
import json

class ModifyPhoneBusinessProfileRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'cams', '2020-06-06', 'ModifyPhoneBusinessProfile')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_PhoneNumber(self): # String
		return self.get_query_params().get('PhoneNumber')

	def set_PhoneNumber(self, PhoneNumber):  # String
		self.add_query_param('PhoneNumber', PhoneNumber)
	def get_Description(self): # String
		return self.get_query_params().get('Description')

	def set_Description(self, Description):  # String
		self.add_query_param('Description', Description)
	def get_Vertical(self): # String
		return self.get_query_params().get('Vertical')

	def set_Vertical(self, Vertical):  # String
		self.add_query_param('Vertical', Vertical)
	def get_Email(self): # String
		return self.get_query_params().get('Email')

	def set_Email(self, Email):  # String
		self.add_query_param('Email', Email)
	def get_Address(self): # String
		return self.get_query_params().get('Address')

	def set_Address(self, Address):  # String
		self.add_query_param('Address', Address)
	def get_ProfilePictureUrl(self): # String
		return self.get_query_params().get('ProfilePictureUrl')

	def set_ProfilePictureUrl(self, ProfilePictureUrl):  # String
		self.add_query_param('ProfilePictureUrl', ProfilePictureUrl)
	def get_CustSpaceId(self): # String
		return self.get_query_params().get('CustSpaceId')

	def set_CustSpaceId(self, CustSpaceId):  # String
		self.add_query_param('CustSpaceId', CustSpaceId)
	def get_Websites(self): # Array
		return self.get_query_params().get('Websites')

	def set_Websites(self, Websites):  # Array
		self.add_query_param("Websites", json.dumps(Websites))
