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
from aliyunsdkhbr.endpoint import endpoint_data

class DescribeOtsTableSnapshotsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'hbr', '2017-09-08', 'DescribeOtsTableSnapshots')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_CrossAccountType(self): # String
		return self.get_query_params().get('CrossAccountType')

	def set_CrossAccountType(self, CrossAccountType):  # String
		self.add_query_param('CrossAccountType', CrossAccountType)
	def get_SnapshotIds(self): # Array
		return self.get_body_params().get('SnapshotIds')

	def set_SnapshotIds(self, SnapshotIds):  # Array
		for index1, value1 in enumerate(SnapshotIds):
			self.add_body_params('SnapshotIds.' + str(index1 + 1), value1)
	def get_EndTime(self): # Long
		return self.get_body_params().get('EndTime')

	def set_EndTime(self, EndTime):  # Long
		self.add_body_params('EndTime', EndTime)
	def get_CrossAccountRoleName(self): # String
		return self.get_query_params().get('CrossAccountRoleName')

	def set_CrossAccountRoleName(self, CrossAccountRoleName):  # String
		self.add_query_param('CrossAccountRoleName', CrossAccountRoleName)
	def get_StartTime(self): # Long
		return self.get_body_params().get('StartTime')

	def set_StartTime(self, StartTime):  # Long
		self.add_body_params('StartTime', StartTime)
	def get_OtsInstances(self): # Array
		return self.get_body_params().get('OtsInstances')

	def set_OtsInstances(self, OtsInstances):  # Array
		for index1, value1 in enumerate(OtsInstances):
			if value1.get('InstanceName') is not None:
				self.add_body_params('OtsInstances.' + str(index1 + 1) + '.InstanceName', value1.get('InstanceName'))
			if value1.get('TableNames') is not None:
				for index2, value2 in enumerate(value1.get('TableNames')):
					self.add_body_params('OtsInstances.' + str(index1 + 1) + '.TableNames.' + str(index2 + 1), value2)
	def get_NextToken(self): # String
		return self.get_body_params().get('NextToken')

	def set_NextToken(self, NextToken):  # String
		self.add_body_params('NextToken', NextToken)
	def get_Limit(self): # Integer
		return self.get_body_params().get('Limit')

	def set_Limit(self, Limit):  # Integer
		self.add_body_params('Limit', Limit)
	def get_CrossAccountUserId(self): # Long
		return self.get_query_params().get('CrossAccountUserId')

	def set_CrossAccountUserId(self, CrossAccountUserId):  # Long
		self.add_query_param('CrossAccountUserId', CrossAccountUserId)
