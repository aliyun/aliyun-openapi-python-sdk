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
from aliyunsdkhbase.endpoint import endpoint_data

class ModifyInstanceServiceConfigRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'HBase', '2019-01-01', 'ModifyInstanceServiceConfig','hbase')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ConfigureName(self):
		return self.get_query_params().get('ConfigureName')

	def set_ConfigureName(self,ConfigureName):
		self.add_query_param('ConfigureName',ConfigureName)

	def get_Restart(self):
		return self.get_query_params().get('Restart')

	def set_Restart(self,Restart):
		self.add_query_param('Restart',Restart)

	def get_ClusterId(self):
		return self.get_query_params().get('ClusterId')

	def set_ClusterId(self,ClusterId):
		self.add_query_param('ClusterId',ClusterId)

	def get_ConfigureValue(self):
		return self.get_query_params().get('ConfigureValue')

	def set_ConfigureValue(self,ConfigureValue):
		self.add_query_param('ConfigureValue',ConfigureValue)

	def get_Parameters(self):
		return self.get_query_params().get('Parameters')

	def set_Parameters(self,Parameters):
		self.add_query_param('Parameters',Parameters)