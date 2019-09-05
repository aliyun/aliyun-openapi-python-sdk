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
from aliyunsdkfoas.endpoint import endpoint_data

class CreateClusterRequest(RoaRequest):

	def __init__(self):
		RoaRequest.__init__(self, 'foas', '2018-11-11', 'CreateCluster','foas')
		self.set_protocol_type('https')
		self.set_uri_pattern('/api/v2/clusters')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_orderId(self):
		return self.get_body_params().get('orderId')

	def set_orderId(self,orderId):
		self.add_body_params('orderId', orderId)

	def get_userOssBucket(self):
		return self.get_body_params().get('userOssBucket')

	def set_userOssBucket(self,userOssBucket):
		self.add_body_params('userOssBucket', userOssBucket)

	def get_displayName(self):
		return self.get_body_params().get('displayName')

	def set_displayName(self,displayName):
		self.add_body_params('displayName', displayName)

	def get_userVpcId(self):
		return self.get_body_params().get('userVpcId')

	def set_userVpcId(self,userVpcId):
		self.add_body_params('userVpcId', userVpcId)

	def get_zoneId(self):
		return self.get_body_params().get('zoneId')

	def set_zoneId(self,zoneId):
		self.add_body_params('zoneId', zoneId)

	def get_description(self):
		return self.get_body_params().get('description')

	def set_description(self,description):
		self.add_body_params('description', description)

	def get_userVSwitch(self):
		return self.get_body_params().get('userVSwitch')

	def set_userVSwitch(self,userVSwitch):
		self.add_body_params('userVSwitch', userVSwitch)