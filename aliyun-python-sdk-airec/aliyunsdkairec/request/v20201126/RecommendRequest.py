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
from aliyunsdkairec.endpoint import endpoint_data

class RecommendRequest(RoaRequest):

	def __init__(self):
		RoaRequest.__init__(self, 'Airec', '2020-11-26', 'Recommend','airec')
		self.set_uri_pattern('/v2/openapi/instances/[instanceId]/actions/recommend')
		self.set_method('GET')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_returnCount(self):
		return self.get_query_params().get('returnCount')

	def set_returnCount(self,returnCount):
		self.add_query_param('returnCount',returnCount)

	def get_serviceType(self):
		return self.get_query_params().get('serviceType')

	def set_serviceType(self,serviceType):
		self.add_query_param('serviceType',serviceType)

	def get_instanceId(self):
		return self.get_path_params().get('instanceId')

	def set_instanceId(self,instanceId):
		self.add_path_param('instanceId',instanceId)

	def get_ip(self):
		return self.get_query_params().get('ip')

	def set_ip(self,ip):
		self.add_query_param('ip',ip)

	def get_sceneId(self):
		return self.get_query_params().get('sceneId')

	def set_sceneId(self,sceneId):
		self.add_query_param('sceneId',sceneId)

	def get_imei(self):
		return self.get_query_params().get('imei')

	def set_imei(self,imei):
		self.add_query_param('imei',imei)

	def get_userId(self):
		return self.get_query_params().get('userId')

	def set_userId(self,userId):
		self.add_query_param('userId',userId)

	def get_items(self):
		return self.get_query_params().get('items')

	def set_items(self,items):
		self.add_query_param('items',items)

	def get_userInfo(self):
		return self.get_query_params().get('userInfo')

	def set_userInfo(self,userInfo):
		self.add_query_param('userInfo',userInfo)