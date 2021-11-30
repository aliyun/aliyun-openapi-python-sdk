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
from aliyunsdkalb.endpoint import endpoint_data

class UpdateListenerLogConfigRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Alb', '2020-06-16', 'UpdateListenerLogConfig','alb')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ClientToken(self): # String
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self, ClientToken):  # String
		self.add_query_param('ClientToken', ClientToken)
	def get_ListenerId(self): # String
		return self.get_query_params().get('ListenerId')

	def set_ListenerId(self, ListenerId):  # String
		self.add_query_param('ListenerId', ListenerId)
	def get_AccessLogRecordCustomizedHeadersEnabled(self): # Boolean
		return self.get_query_params().get('AccessLogRecordCustomizedHeadersEnabled')

	def set_AccessLogRecordCustomizedHeadersEnabled(self, AccessLogRecordCustomizedHeadersEnabled):  # Boolean
		self.add_query_param('AccessLogRecordCustomizedHeadersEnabled', AccessLogRecordCustomizedHeadersEnabled)
	def get_DryRun(self): # Boolean
		return self.get_query_params().get('DryRun')

	def set_DryRun(self, DryRun):  # Boolean
		self.add_query_param('DryRun', DryRun)
	def get_AccessLogTracingConfig(self): # Struct
		return self.get_query_params().get('AccessLogTracingConfig')

	def set_AccessLogTracingConfig(self, AccessLogTracingConfig):  # Struct
		if AccessLogTracingConfig.get('TracingType') is not None:
			self.add_query_param('AccessLogTracingConfig.TracingType', AccessLogTracingConfig.get('TracingType'))
		if AccessLogTracingConfig.get('TracingEnabled') is not None:
			self.add_query_param('AccessLogTracingConfig.TracingEnabled', AccessLogTracingConfig.get('TracingEnabled'))
		if AccessLogTracingConfig.get('TracingSample') is not None:
			self.add_query_param('AccessLogTracingConfig.TracingSample', AccessLogTracingConfig.get('TracingSample'))
