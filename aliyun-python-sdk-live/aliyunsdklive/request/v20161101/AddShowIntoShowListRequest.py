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
from aliyunsdklive.endpoint import endpoint_data

class AddShowIntoShowListRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'live', '2016-11-01', 'AddShowIntoShowList','live')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_LiveInputType(self):
		return self.get_query_params().get('LiveInputType')

	def set_LiveInputType(self,LiveInputType):
		self.add_query_param('LiveInputType',LiveInputType)

	def get_Duration(self):
		return self.get_query_params().get('Duration')

	def set_Duration(self,Duration):
		self.add_query_param('Duration',Duration)

	def get_RepeatTimes(self):
		return self.get_query_params().get('RepeatTimes')

	def set_RepeatTimes(self,RepeatTimes):
		self.add_query_param('RepeatTimes',RepeatTimes)

	def get_ShowName(self):
		return self.get_query_params().get('ShowName')

	def set_ShowName(self,ShowName):
		self.add_query_param('ShowName',ShowName)

	def get_ResourceId(self):
		return self.get_query_params().get('ResourceId')

	def set_ResourceId(self,ResourceId):
		self.add_query_param('ResourceId',ResourceId)

	def get_CasterId(self):
		return self.get_query_params().get('CasterId')

	def set_CasterId(self,CasterId):
		self.add_query_param('CasterId',CasterId)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_ResourceType(self):
		return self.get_query_params().get('ResourceType')

	def set_ResourceType(self,ResourceType):
		self.add_query_param('ResourceType',ResourceType)

	def get_ResourceUrl(self):
		return self.get_query_params().get('ResourceUrl')

	def set_ResourceUrl(self,ResourceUrl):
		self.add_query_param('ResourceUrl',ResourceUrl)

	def get_Spot(self):
		return self.get_query_params().get('Spot')

	def set_Spot(self,Spot):
		self.add_query_param('Spot',Spot)