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
from aliyunsdkwebplus.endpoint import endpoint_data

class CreateApplicationRequest(RoaRequest):

	def __init__(self):
		RoaRequest.__init__(self, 'WebPlus', '2019-03-20', 'CreateApplication','webx')
		self.set_uri_pattern('/pop/v1/wam/application')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_AppDescription(self):
		return self.get_body_params().get('AppDescription')

	def set_AppDescription(self,AppDescription):
		self.add_body_params('AppDescription', AppDescription)

	def get_AppName(self):
		return self.get_body_params().get('AppName')

	def set_AppName(self,AppName):
		self.add_body_params('AppName', AppName)

	def get_CategoryName(self):
		return self.get_body_params().get('CategoryName')

	def set_CategoryName(self,CategoryName):
		self.add_body_params('CategoryName', CategoryName)