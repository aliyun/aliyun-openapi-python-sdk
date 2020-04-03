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
from aliyunsdkarms.endpoint import endpoint_data

class QueryDatasetRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'ARMS', '2019-08-08', 'QueryDataset','arms')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_DateStr(self):
		return self.get_query_params().get('DateStr')

	def set_DateStr(self,DateStr):
		self.add_query_param('DateStr',DateStr)

	def get_MinTime(self):
		return self.get_query_params().get('MinTime')

	def set_MinTime(self,MinTime):
		self.add_query_param('MinTime',MinTime)

	def get_ProxyUserId(self):
		return self.get_query_params().get('ProxyUserId')

	def set_ProxyUserId(self,ProxyUserId):
		self.add_query_param('ProxyUserId',ProxyUserId)

	def get_ReduceTail(self):
		return self.get_query_params().get('ReduceTail')

	def set_ReduceTail(self,ReduceTail):
		self.add_query_param('ReduceTail',ReduceTail)

	def get_MaxTime(self):
		return self.get_query_params().get('MaxTime')

	def set_MaxTime(self,MaxTime):
		self.add_query_param('MaxTime',MaxTime)

	def get_OptionalDimss(self):
		return self.get_query_params().get('OptionalDimss')

	def set_OptionalDimss(self,OptionalDimss):
		for i in range(len(OptionalDimss)):	
			if OptionalDimss[i].get('Type') is not None:
				self.add_query_param('OptionalDims.' + str(i + 1) + '.Type' , OptionalDimss[i].get('Type'))
			if OptionalDimss[i].get('Value') is not None:
				self.add_query_param('OptionalDims.' + str(i + 1) + '.Value' , OptionalDimss[i].get('Value'))
			if OptionalDimss[i].get('Key') is not None:
				self.add_query_param('OptionalDims.' + str(i + 1) + '.Key' , OptionalDimss[i].get('Key'))


	def get_Measuress(self):
		return self.get_query_params().get('Measuress')

	def set_Measuress(self,Measuress):
		for i in range(len(Measuress)):	
			if Measuress[i] is not None:
				self.add_query_param('Measures.' + str(i + 1) , Measuress[i]);

	def get_IntervalInSec(self):
		return self.get_query_params().get('IntervalInSec')

	def set_IntervalInSec(self,IntervalInSec):
		self.add_query_param('IntervalInSec',IntervalInSec)

	def get_IsDrillDown(self):
		return self.get_query_params().get('IsDrillDown')

	def set_IsDrillDown(self,IsDrillDown):
		self.add_query_param('IsDrillDown',IsDrillDown)

	def get_HungryMode(self):
		return self.get_query_params().get('HungryMode')

	def set_HungryMode(self,HungryMode):
		self.add_query_param('HungryMode',HungryMode)

	def get_OrderByKey(self):
		return self.get_query_params().get('OrderByKey')

	def set_OrderByKey(self,OrderByKey):
		self.add_query_param('OrderByKey',OrderByKey)

	def get_Limit(self):
		return self.get_query_params().get('Limit')

	def set_Limit(self,Limit):
		self.add_query_param('Limit',Limit)

	def get_DatasetId(self):
		return self.get_query_params().get('DatasetId')

	def set_DatasetId(self,DatasetId):
		self.add_query_param('DatasetId',DatasetId)

	def get_RequiredDimss(self):
		return self.get_query_params().get('RequiredDimss')

	def set_RequiredDimss(self,RequiredDimss):
		for i in range(len(RequiredDimss)):	
			if RequiredDimss[i].get('Type') is not None:
				self.add_query_param('RequiredDims.' + str(i + 1) + '.Type' , RequiredDimss[i].get('Type'))
			if RequiredDimss[i].get('Value') is not None:
				self.add_query_param('RequiredDims.' + str(i + 1) + '.Value' , RequiredDimss[i].get('Value'))
			if RequiredDimss[i].get('Key') is not None:
				self.add_query_param('RequiredDims.' + str(i + 1) + '.Key' , RequiredDimss[i].get('Key'))


	def get_Dimensionss(self):
		return self.get_query_params().get('Dimensionss')

	def set_Dimensionss(self,Dimensionss):
		for i in range(len(Dimensionss)):	
			if Dimensionss[i].get('Type') is not None:
				self.add_query_param('Dimensions.' + str(i + 1) + '.Type' , Dimensionss[i].get('Type'))
			if Dimensionss[i].get('Value') is not None:
				self.add_query_param('Dimensions.' + str(i + 1) + '.Value' , Dimensionss[i].get('Value'))
			if Dimensionss[i].get('Key') is not None:
				self.add_query_param('Dimensions.' + str(i + 1) + '.Key' , Dimensionss[i].get('Key'))
