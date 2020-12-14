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

class ListCityMapAoisRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'CDRS', '2020-11-01', 'ListCityMapAois')
		self.set_method('POST')

	def get_Latitude(self):
		return self.get_body_params().get('Latitude')

	def set_Latitude(self,Latitude):
		self.add_body_params('Latitude', Latitude)

	def get_Radius(self):
		return self.get_body_params().get('Radius')

	def set_Radius(self,Radius):
		self.add_body_params('Radius', Radius)

	def get_Longitude(self):
		return self.get_body_params().get('Longitude')

	def set_Longitude(self,Longitude):
		self.add_body_params('Longitude', Longitude)