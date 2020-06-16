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

class DescribeInstancesRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ens', '2017-11-10', 'DescribeInstances','ens')
		self.set_method('POST')

	def get_ImageId(self):
		return self.get_query_params().get('ImageId')

	def set_ImageId(self,ImageId):
		self.add_query_param('ImageId',ImageId)

	def get_SearchKey(self):
		return self.get_query_params().get('SearchKey')

	def set_SearchKey(self,SearchKey):
		self.add_query_param('SearchKey',SearchKey)

	def get_PageNumber(self):
		return self.get_query_params().get('PageNumber')

	def set_PageNumber(self,PageNumber):
		self.add_query_param('PageNumber',PageNumber)

	def get_OrderByParams(self):
		return self.get_query_params().get('OrderByParams')

	def set_OrderByParams(self,OrderByParams):
		self.add_query_param('OrderByParams',OrderByParams)

	def get_EnsRegionId(self):
		return self.get_query_params().get('EnsRegionId')

	def set_EnsRegionId(self,EnsRegionId):
		self.add_query_param('EnsRegionId',EnsRegionId)

	def get_PageSize(self):
		return self.get_query_params().get('PageSize')

	def set_PageSize(self,PageSize):
		self.add_query_param('PageSize',PageSize)

	def get_EnsRegionIds(self):
		return self.get_query_params().get('EnsRegionIds')

	def set_EnsRegionIds(self,EnsRegionIds):
		self.add_query_param('EnsRegionIds',EnsRegionIds)

	def get_InstanceResourceType(self):
		return self.get_query_params().get('InstanceResourceType')

	def set_InstanceResourceType(self,InstanceResourceType):
		self.add_query_param('InstanceResourceType',InstanceResourceType)

	def get_EnsServiceId(self):
		return self.get_query_params().get('EnsServiceId')

	def set_EnsServiceId(self,EnsServiceId):
		self.add_query_param('EnsServiceId',EnsServiceId)

	def get_Version(self):
		return self.get_query_params().get('Version')

	def set_Version(self,Version):
		self.add_query_param('Version',Version)

	def get_InstanceId(self):
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self,InstanceId):
		self.add_query_param('InstanceId',InstanceId)

	def get_InstanceName(self):
		return self.get_query_params().get('InstanceName')

	def set_InstanceName(self,InstanceName):
		self.add_query_param('InstanceName',InstanceName)

	def get_InstanceIds(self):
		return self.get_query_params().get('InstanceIds')

	def set_InstanceIds(self,InstanceIds):
		self.add_query_param('InstanceIds',InstanceIds)

	def get_Status(self):
		return self.get_query_params().get('Status')

	def set_Status(self,Status):
		self.add_query_param('Status',Status)