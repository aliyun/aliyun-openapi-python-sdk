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
from aliyunsdkedas.endpoint import endpoint_data

class ListScaleOutEcuRequest(RoaRequest):

	def __init__(self):
		RoaRequest.__init__(self, 'Edas', '2017-08-01', 'ListScaleOutEcu','Edas')
		self.set_uri_pattern('/pop/v5/resource/scale_out_ecu_list')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_Mem(self): # integer
		return self.get_query_params().get('Mem')

	def set_Mem(self, Mem):  # integer
		self.add_query_param('Mem', Mem)
	def get_LogicalRegionId(self): # string
		return self.get_query_params().get('LogicalRegionId')

	def set_LogicalRegionId(self, LogicalRegionId):  # string
		self.add_query_param('LogicalRegionId', LogicalRegionId)
	def get_AppId(self): # string
		return self.get_query_params().get('AppId')

	def set_AppId(self, AppId):  # string
		self.add_query_param('AppId', AppId)
	def get_GroupId(self): # string
		return self.get_query_params().get('GroupId')

	def set_GroupId(self, GroupId):  # string
		self.add_query_param('GroupId', GroupId)
	def get_InstanceNum(self): # integer
		return self.get_query_params().get('InstanceNum')

	def set_InstanceNum(self, InstanceNum):  # integer
		self.add_query_param('InstanceNum', InstanceNum)
	def get_Cpu(self): # integer
		return self.get_query_params().get('Cpu')

	def set_Cpu(self, Cpu):  # integer
		self.add_query_param('Cpu', Cpu)
	def get_ClusterId(self): # string
		return self.get_query_params().get('ClusterId')

	def set_ClusterId(self, ClusterId):  # string
		self.add_query_param('ClusterId', ClusterId)
