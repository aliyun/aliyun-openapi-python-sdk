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

class SwitchHbaseHaSlbRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'HBase', '2019-01-01', 'SwitchHbaseHaSlb')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_HaTypes(self):
		return self.get_query_params().get('HaTypes')

	def set_HaTypes(self,HaTypes):
		self.add_query_param('HaTypes',HaTypes)

	def get_HbaseType(self):
		return self.get_query_params().get('HbaseType')

	def set_HbaseType(self,HbaseType):
		self.add_query_param('HbaseType',HbaseType)

	def get_BdsId(self):
		return self.get_query_params().get('BdsId')

	def set_BdsId(self,BdsId):
		self.add_query_param('BdsId',BdsId)

	def get_HaId(self):
		return self.get_query_params().get('HaId')

	def set_HaId(self,HaId):
		self.add_query_param('HaId',HaId)