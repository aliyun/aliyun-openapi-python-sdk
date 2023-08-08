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

class DescribeLiveCdnDiagnoseInfoRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'live', '2016-11-01', 'DescribeLiveCdnDiagnoseInfo','live')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_intervalType(self): # String
		return self.get_query_params().get('intervalType')

	def set_intervalType(self, intervalType):  # String
		self.add_query_param('intervalType', intervalType)
	def get_streamSuffix(self): # String
		return self.get_query_params().get('streamSuffix')

	def set_streamSuffix(self, streamSuffix):  # String
		self.add_query_param('streamSuffix', streamSuffix)
	def get_startTime(self): # Long
		return self.get_query_params().get('startTime')

	def set_startTime(self, startTime):  # Long
		self.add_query_param('startTime', startTime)
	def get_requestType(self): # String
		return self.get_query_params().get('requestType')

	def set_requestType(self, requestType):  # String
		self.add_query_param('requestType', requestType)
	def get_streamName(self): # String
		return self.get_query_params().get('streamName')

	def set_streamName(self, streamName):  # String
		self.add_query_param('streamName', streamName)
	def get_app(self): # String
		return self.get_query_params().get('app')

	def set_app(self, app):  # String
		self.add_query_param('app', app)
	def get_phase(self): # Integer
		return self.get_query_params().get('phase')

	def set_phase(self, phase):  # Integer
		self.add_query_param('phase', phase)
	def get_endTime(self): # Long
		return self.get_query_params().get('endTime')

	def set_endTime(self, endTime):  # Long
		self.add_query_param('endTime', endTime)
	def get_domain(self): # String
		return self.get_query_params().get('domain')

	def set_domain(self, domain):  # String
		self.add_query_param('domain', domain)
