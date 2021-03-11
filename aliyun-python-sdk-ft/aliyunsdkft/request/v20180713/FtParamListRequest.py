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
from aliyunsdkft.endpoint import endpoint_data

class FtParamListRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ft', '2018-07-13', 'FtParamList')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_Disks(self):
		return self.get_query_params().get('Disk')

	def set_Disks(self, Disks):
		for depth1 in range(len(Disks)):
			if Disks[depth1].get('Size') is not None:
				for depth2 in range(len(Disks[depth1].get('Size'))):
					if Disks[depth1].get('Size')[depth2] is not None:
						self.add_query_param('Disk.' + str(depth1 + 1) + '.Size.' + str(depth2 + 1) , Disks[depth1].get('Size')[depth2])
			if Disks[depth1].get('Type') is not None:
				for depth2 in range(len(Disks[depth1].get('Type'))):
					if Disks[depth1].get('Type')[depth2] is not None:
						self.add_query_param('Disk.' + str(depth1 + 1) + '.Type.' + str(depth2 + 1) , Disks[depth1].get('Type')[depth2])

	def get_Name(self):
		return self.get_query_params().get('Name')

	def set_Name(self,Name):
		self.add_query_param('Name',Name)