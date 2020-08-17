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
from aliyunsdkdrds.endpoint import endpoint_data

class SubmitTableShardingKeyModifyRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Drds', '2019-01-23', 'SubmitTableShardingKeyModify','Drds')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_TbPartitions(self):
		return self.get_query_params().get('TbPartitions')

	def set_TbPartitions(self,TbPartitions):
		self.add_query_param('TbPartitions',TbPartitions)

	def get_IsShard(self):
		return self.get_query_params().get('IsShard')

	def set_IsShard(self,IsShard):
		self.add_query_param('IsShard',IsShard)

	def get_TbShardingFunction(self):
		return self.get_query_params().get('TbShardingFunction')

	def set_TbShardingFunction(self,TbShardingFunction):
		self.add_query_param('TbShardingFunction',TbShardingFunction)

	def get_DbShardingColumnList(self):
		return self.get_query_params().get('DbShardingColumnList')

	def set_DbShardingColumnList(self,DbShardingColumnList):
		self.add_query_param('DbShardingColumnList',DbShardingColumnList)

	def get_TbComputeLength(self):
		return self.get_query_params().get('TbComputeLength')

	def set_TbComputeLength(self,TbComputeLength):
		self.add_query_param('TbComputeLength',TbComputeLength)

	def get_TbRightShiftOffset(self):
		return self.get_query_params().get('TbRightShiftOffset')

	def set_TbRightShiftOffset(self,TbRightShiftOffset):
		self.add_query_param('TbRightShiftOffset',TbRightShiftOffset)

	def get_DbComputeLength(self):
		return self.get_query_params().get('DbComputeLength')

	def set_DbComputeLength(self,DbComputeLength):
		self.add_query_param('DbComputeLength',DbComputeLength)

	def get_SrcTableName(self):
		return self.get_query_params().get('SrcTableName')

	def set_SrcTableName(self,SrcTableName):
		self.add_query_param('SrcTableName',SrcTableName)

	def get_DbRightShiftOffset(self):
		return self.get_query_params().get('DbRightShiftOffset')

	def set_DbRightShiftOffset(self,DbRightShiftOffset):
		self.add_query_param('DbRightShiftOffset',DbRightShiftOffset)

	def get_TargetTableName(self):
		return self.get_query_params().get('TargetTableName')

	def set_TargetTableName(self,TargetTableName):
		self.add_query_param('TargetTableName',TargetTableName)

	def get_DrdsInstanceId(self):
		return self.get_query_params().get('DrdsInstanceId')

	def set_DrdsInstanceId(self,DrdsInstanceId):
		self.add_query_param('DrdsInstanceId',DrdsInstanceId)

	def get_DbShardingFunction(self):
		return self.get_query_params().get('DbShardingFunction')

	def set_DbShardingFunction(self,DbShardingFunction):
		self.add_query_param('DbShardingFunction',DbShardingFunction)

	def get_DbName(self):
		return self.get_query_params().get('DbName')

	def set_DbName(self,DbName):
		self.add_query_param('DbName',DbName)

	def get_TbShardingColumnList(self):
		return self.get_query_params().get('TbShardingColumnList')

	def set_TbShardingColumnList(self,TbShardingColumnList):
		self.add_query_param('TbShardingColumnList',TbShardingColumnList)