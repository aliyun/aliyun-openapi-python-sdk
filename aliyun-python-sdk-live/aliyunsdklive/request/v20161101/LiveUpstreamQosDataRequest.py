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
import json

class LiveUpstreamQosDataRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'live', '2016-11-01', 'LiveUpstreamQosData','live')
		self.set_protocol_type('https')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_CdnDomains(self): # String
		return self.get_query_params().get('CdnDomains')

	def set_CdnDomains(self, CdnDomains):  # String
		self.add_query_param('CdnDomains', CdnDomains)
	def get_StartTime(self): # String
		return self.get_query_params().get('StartTime')

	def set_StartTime(self, StartTime):  # String
		self.add_query_param('StartTime', StartTime)
	def get_CdnProvinces(self): # String
		return self.get_query_params().get('CdnProvinces')

	def set_CdnProvinces(self, CdnProvinces):  # String
		self.add_query_param('CdnProvinces', CdnProvinces)
	def get_KwaiSidcs(self): # String
		return self.get_query_params().get('KwaiSidcs')

	def set_KwaiSidcs(self, KwaiSidcs):  # String
		self.add_query_param('KwaiSidcs', KwaiSidcs)
	def get_KwaiTsc(self): # Array
		return self.get_query_params().get('KwaiTsc')

	def set_KwaiTsc(self, KwaiTsc):  # Array
		self.add_query_param("KwaiTsc", json.dumps(KwaiTsc))
	def get_UpstreamDomains(self): # String
		return self.get_query_params().get('UpstreamDomains')

	def set_UpstreamDomains(self, UpstreamDomains):  # String
		self.add_query_param('UpstreamDomains', UpstreamDomains)
	def get_EndTime(self): # String
		return self.get_query_params().get('EndTime')

	def set_EndTime(self, EndTime):  # String
		self.add_query_param('EndTime', EndTime)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_CdnIsps(self): # String
		return self.get_query_params().get('CdnIsps')

	def set_CdnIsps(self, CdnIsps):  # String
		self.add_query_param('CdnIsps', CdnIsps)
	def get_Region(self): # String
		return self.get_query_params().get('Region')

	def set_Region(self, Region):  # String
		self.add_query_param('Region', Region)
