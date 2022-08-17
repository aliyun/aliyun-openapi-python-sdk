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

class DescribeDedicatedBlockStorageClustersRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'ebs', '2021-07-30', 'DescribeDedicatedBlockStorageClusters','ebs')
		self.set_method('POST')

	def get_DedicatedBlockStorageClusterIds(self): # RepeatList
		return self.get_body_params().get('DedicatedBlockStorageClusterId')

	def set_DedicatedBlockStorageClusterIds(self, DedicatedBlockStorageClusterId):  # RepeatList
		for depth1 in range(len(DedicatedBlockStorageClusterId)):
			self.add_body_params('DedicatedBlockStorageClusterId.' + str(depth1 + 1), DedicatedBlockStorageClusterId[depth1])
	def get_ClientToken(self): # String
		return self.get_body_params().get('ClientToken')

	def set_ClientToken(self, ClientToken):  # String
		self.add_body_params('ClientToken', ClientToken)
	def get_AzoneId(self): # String
		return self.get_body_params().get('AzoneId')

	def set_AzoneId(self, AzoneId):  # String
		self.add_body_params('AzoneId', AzoneId)
	def get_NextToken(self): # String
		return self.get_body_params().get('NextToken')

	def set_NextToken(self, NextToken):  # String
		self.add_body_params('NextToken', NextToken)
	def get_MaxResults(self): # Integer
		return self.get_body_params().get('MaxResults')

	def set_MaxResults(self, MaxResults):  # Integer
		self.add_body_params('MaxResults', MaxResults)
	def get_Category(self): # String
		return self.get_body_params().get('Category')

	def set_Category(self, Category):  # String
		self.add_body_params('Category', Category)
	def get_Statuss(self): # RepeatList
		return self.get_body_params().get('Status')

	def set_Statuss(self, Status):  # RepeatList
		for depth1 in range(len(Status)):
			self.add_body_params('Status.' + str(depth1 + 1), Status[depth1])
