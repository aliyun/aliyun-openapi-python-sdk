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
from aliyunsdkhitsdb.endpoint import endpoint_data

class ExploreHiTSDBInstanceDataRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'hitsdb', '2017-06-01', 'ExploreHiTSDBInstanceData','hitsdb')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ReverseVpcIp(self):
		return self.get_query_params().get('ReverseVpcIp')

	def set_ReverseVpcIp(self,ReverseVpcIp):
		self.add_query_param('ReverseVpcIp',ReverseVpcIp)

	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_ReverseVpcPort(self):
		return self.get_query_params().get('ReverseVpcPort')

	def set_ReverseVpcPort(self,ReverseVpcPort):
		self.add_query_param('ReverseVpcPort',ReverseVpcPort)

	def get_PassWord(self):
		return self.get_query_params().get('PassWord')

	def set_PassWord(self,PassWord):
		self.add_query_param('PassWord',PassWord)

	def get_SecurityToken(self):
		return self.get_query_params().get('SecurityToken')

	def set_SecurityToken(self,SecurityToken):
		self.add_query_param('SecurityToken',SecurityToken)

	def get_End(self):
		return self.get_query_params().get('End')

	def set_End(self,End):
		self.add_query_param('End',End)

	def get_ResourceOwnerAccount(self):
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self,ResourceOwnerAccount):
		self.add_query_param('ResourceOwnerAccount',ResourceOwnerAccount)

	def get_OwnerAccount(self):
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self,OwnerAccount):
		self.add_query_param('OwnerAccount',OwnerAccount)

	def get_Aggregator(self):
		return self.get_query_params().get('Aggregator')

	def set_Aggregator(self,Aggregator):
		self.add_query_param('Aggregator',Aggregator)

	def get_Start(self):
		return self.get_query_params().get('Start')

	def set_Start(self,Start):
		self.add_query_param('Start',Start)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_TagFilter(self):
		return self.get_query_params().get('TagFilter')

	def set_TagFilter(self,TagFilter):
		self.add_query_param('TagFilter',TagFilter)

	def get_InstanceId(self):
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self,InstanceId):
		self.add_query_param('InstanceId',InstanceId)

	def get_Metric(self):
		return self.get_query_params().get('Metric')

	def set_Metric(self,Metric):
		self.add_query_param('Metric',Metric)

	def get_DownSampleAggregator(self):
		return self.get_query_params().get('DownSampleAggregator')

	def set_DownSampleAggregator(self,DownSampleAggregator):
		self.add_query_param('DownSampleAggregator',DownSampleAggregator)

	def get_DownSampleTime(self):
		return self.get_query_params().get('DownSampleTime')

	def set_DownSampleTime(self,DownSampleTime):
		self.add_query_param('DownSampleTime',DownSampleTime)

	def get_UserName(self):
		return self.get_query_params().get('UserName')

	def set_UserName(self,UserName):
		self.add_query_param('UserName',UserName)