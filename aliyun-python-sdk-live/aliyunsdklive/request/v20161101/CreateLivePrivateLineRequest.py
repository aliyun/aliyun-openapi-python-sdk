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

class CreateLivePrivateLineRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'live', '2016-11-01', 'CreateLivePrivateLine','live')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_MaxBandwidth(self): # String
		return self.get_query_params().get('MaxBandwidth')

	def set_MaxBandwidth(self, MaxBandwidth):  # String
		self.add_query_param('MaxBandwidth', MaxBandwidth)
	def get_Reuse(self): # String
		return self.get_query_params().get('Reuse')

	def set_Reuse(self, Reuse):  # String
		self.add_query_param('Reuse', Reuse)
	def get_AccelerationArea(self): # String
		return self.get_query_params().get('AccelerationArea')

	def set_AccelerationArea(self, AccelerationArea):  # String
		self.add_query_param('AccelerationArea', AccelerationArea)
	def get_AppName(self): # String
		return self.get_query_params().get('AppName')

	def set_AppName(self, AppName):  # String
		self.add_query_param('AppName', AppName)
	def get_StreamName(self): # String
		return self.get_query_params().get('StreamName')

	def set_StreamName(self, StreamName):  # String
		self.add_query_param('StreamName', StreamName)
	def get_DomainName(self): # String
		return self.get_query_params().get('DomainName')

	def set_DomainName(self, DomainName):  # String
		self.add_query_param('DomainName', DomainName)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_VideoCenter(self): # String
		return self.get_query_params().get('VideoCenter')

	def set_VideoCenter(self, VideoCenter):  # String
		self.add_query_param('VideoCenter', VideoCenter)
	def get_AccelerationType(self): # String
		return self.get_query_params().get('AccelerationType')

	def set_AccelerationType(self, AccelerationType):  # String
		self.add_query_param('AccelerationType', AccelerationType)
	def get_InstanceId(self): # String
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self, InstanceId):  # String
		self.add_query_param('InstanceId', InstanceId)
