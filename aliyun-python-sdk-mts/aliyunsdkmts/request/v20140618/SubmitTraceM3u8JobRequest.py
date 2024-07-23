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
from aliyunsdkmts.endpoint import endpoint_data

class SubmitTraceM3u8JobRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Mts', '2014-06-18', 'SubmitTraceM3u8Job','mts')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_MediaId(self): # String
		return self.get_query_params().get('MediaId')

	def set_MediaId(self, MediaId):  # String
		self.add_query_param('MediaId', MediaId)
	def get_Params(self): # String
		return self.get_query_params().get('Params')

	def set_Params(self, Params):  # String
		self.add_query_param('Params', Params)
	def get_Output(self): # String
		return self.get_query_params().get('Output')

	def set_Output(self, Output):  # String
		self.add_query_param('Output', Output)
	def get_Trace(self): # String
		return self.get_query_params().get('Trace')

	def set_Trace(self, Trace):  # String
		self.add_query_param('Trace', Trace)
	def get_KeyUri(self): # String
		return self.get_query_params().get('KeyUri')

	def set_KeyUri(self, KeyUri):  # String
		self.add_query_param('KeyUri', KeyUri)
