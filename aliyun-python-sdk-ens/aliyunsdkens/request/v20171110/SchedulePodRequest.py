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

class SchedulePodRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ens', '2017-11-10', 'SchedulePod','ens')
		self.set_method('POST')

	def get_AreaCodes(self): # String
		return self.get_query_params().get('AreaCodes')

	def set_AreaCodes(self, AreaCodes):  # String
		self.add_query_param('AreaCodes', AreaCodes)
	def get_GroupUuid(self): # String
		return self.get_query_params().get('GroupUuid')

	def set_GroupUuid(self, GroupUuid):  # String
		self.add_query_param('GroupUuid', GroupUuid)
	def get_Isps(self): # String
		return self.get_query_params().get('Isps')

	def set_Isps(self, Isps):  # String
		self.add_query_param('Isps', Isps)
	def get_Tenant(self): # String
		return self.get_query_params().get('Tenant')

	def set_Tenant(self, Tenant):  # String
		self.add_query_param('Tenant', Tenant)
	def get_WorkloadUuid(self): # String
		return self.get_query_params().get('WorkloadUuid')

	def set_WorkloadUuid(self, WorkloadUuid):  # String
		self.add_query_param('WorkloadUuid', WorkloadUuid)
	def get_Labels(self): # String
		return self.get_query_params().get('Labels')

	def set_Labels(self, Labels):  # String
		self.add_query_param('Labels', Labels)
	def get_Regions(self): # String
		return self.get_query_params().get('Regions')

	def set_Regions(self, Regions):  # String
		self.add_query_param('Regions', Regions)
	def get_ResourceAttribute(self): # String
		return self.get_body_params().get('ResourceAttribute')

	def set_ResourceAttribute(self, ResourceAttribute):  # String
		self.add_body_params('ResourceAttribute', ResourceAttribute)
	def get_AliUid(self): # Long
		return self.get_query_params().get('AliUid')

	def set_AliUid(self, AliUid):  # Long
		self.add_query_param('AliUid', AliUid)
	def get_Requirements(self): # String
		return self.get_body_params().get('Requirements')

	def set_Requirements(self, Requirements):  # String
		self.add_body_params('Requirements', Requirements)
