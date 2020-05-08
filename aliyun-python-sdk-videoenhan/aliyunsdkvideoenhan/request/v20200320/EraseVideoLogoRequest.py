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
from aliyunsdkvideoenhan.endpoint import endpoint_data

class EraseVideoLogoRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'videoenhan', '2020-03-20', 'EraseVideoLogo','videoenhan')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_Boxess(self):
		return self.get_body_params().get('Boxess')

	def set_Boxess(self,Boxess):
		for i in range(len(Boxess)):	
			if Boxess[i].get('W') is not None:
				self.add_body_params('Boxes.' + str(i + 1) + '.W' , Boxess[i].get('W'))
			if Boxess[i].get('H') is not None:
				self.add_body_params('Boxes.' + str(i + 1) + '.H' , Boxess[i].get('H'))
			if Boxess[i].get('X') is not None:
				self.add_body_params('Boxes.' + str(i + 1) + '.X' , Boxess[i].get('X'))
			if Boxess[i].get('Y') is not None:
				self.add_body_params('Boxes.' + str(i + 1) + '.Y' , Boxess[i].get('Y'))


	def get_VideoUrl(self):
		return self.get_body_params().get('VideoUrl')

	def set_VideoUrl(self,VideoUrl):
		self.add_body_params('VideoUrl', VideoUrl)