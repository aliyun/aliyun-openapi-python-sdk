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
from aliyunsdkemr.endpoint import endpoint_data

class ResizeClusterV2Request(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Emr', '2016-04-08', 'ResizeClusterV2','emr')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_IsOpenPublicIp(self):
		return self.get_query_params().get('IsOpenPublicIp')

	def set_IsOpenPublicIp(self,IsOpenPublicIp):
		self.add_query_param('IsOpenPublicIp',IsOpenPublicIp)

	def get_AutoPayOrder(self):
		return self.get_query_params().get('AutoPayOrder')

	def set_AutoPayOrder(self,AutoPayOrder):
		self.add_query_param('AutoPayOrder',AutoPayOrder)

	def get_ClusterId(self):
		return self.get_query_params().get('ClusterId')

	def set_ClusterId(self,ClusterId):
		self.add_query_param('ClusterId',ClusterId)

	def get_VswitchId(self):
		return self.get_query_params().get('VswitchId')

	def set_VswitchId(self,VswitchId):
		self.add_query_param('VswitchId',VswitchId)

	def get_HostComponentInfos(self):
		return self.get_query_params().get('HostComponentInfo')

	def set_HostComponentInfos(self, HostComponentInfos):
		for depth1 in range(len(HostComponentInfos)):
			if HostComponentInfos[depth1].get('HostName') is not None:
				self.add_query_param('HostComponentInfo.' + str(depth1 + 1) + '.HostName', HostComponentInfos[depth1].get('HostName'))
			if HostComponentInfos[depth1].get('ComponentNameList') is not None:
				for depth2 in range(len(HostComponentInfos[depth1].get('ComponentNameList'))):
					if HostComponentInfos[depth1].get('ComponentNameList')[depth2] is not None:
						self.add_query_param('HostComponentInfo.' + str(depth1 + 1) + '.ComponentNameList.' + str(depth2 + 1) , HostComponentInfos[depth1].get('ComponentNameList')[depth2])
			if HostComponentInfos[depth1].get('ServiceName') is not None:
				self.add_query_param('HostComponentInfo.' + str(depth1 + 1) + '.ServiceName', HostComponentInfos[depth1].get('ServiceName'))

	def get_ClickhouseConf(self):
		return self.get_query_params().get('ClickhouseConf')

	def set_ClickhouseConf(self,ClickhouseConf):
		self.add_query_param('ClickhouseConf',ClickhouseConf)

	def get_HostGroups(self):
		return self.get_query_params().get('HostGroup')

	def set_HostGroups(self, HostGroups):
		for depth1 in range(len(HostGroups)):
			if HostGroups[depth1].get('Period') is not None:
				self.add_query_param('HostGroup.' + str(depth1 + 1) + '.Period', HostGroups[depth1].get('Period'))
			if HostGroups[depth1].get('SysDiskCapacity') is not None:
				self.add_query_param('HostGroup.' + str(depth1 + 1) + '.SysDiskCapacity', HostGroups[depth1].get('SysDiskCapacity'))
			if HostGroups[depth1].get('HostKeyPairName') is not None:
				self.add_query_param('HostGroup.' + str(depth1 + 1) + '.HostKeyPairName', HostGroups[depth1].get('HostKeyPairName'))
			if HostGroups[depth1].get('PrivatePoolOptionsId') is not None:
				self.add_query_param('HostGroup.' + str(depth1 + 1) + '.PrivatePoolOptionsId', HostGroups[depth1].get('PrivatePoolOptionsId'))
			if HostGroups[depth1].get('DiskCapacity') is not None:
				self.add_query_param('HostGroup.' + str(depth1 + 1) + '.DiskCapacity', HostGroups[depth1].get('DiskCapacity'))
			if HostGroups[depth1].get('SysDiskType') is not None:
				self.add_query_param('HostGroup.' + str(depth1 + 1) + '.SysDiskType', HostGroups[depth1].get('SysDiskType'))
			if HostGroups[depth1].get('ClusterId') is not None:
				self.add_query_param('HostGroup.' + str(depth1 + 1) + '.ClusterId', HostGroups[depth1].get('ClusterId'))
			if HostGroups[depth1].get('DiskType') is not None:
				self.add_query_param('HostGroup.' + str(depth1 + 1) + '.DiskType', HostGroups[depth1].get('DiskType'))
			if HostGroups[depth1].get('HostGroupName') is not None:
				self.add_query_param('HostGroup.' + str(depth1 + 1) + '.HostGroupName', HostGroups[depth1].get('HostGroupName'))
			if HostGroups[depth1].get('VswitchId') is not None:
				self.add_query_param('HostGroup.' + str(depth1 + 1) + '.VswitchId', HostGroups[depth1].get('VswitchId'))
			if HostGroups[depth1].get('DiskCount') is not None:
				self.add_query_param('HostGroup.' + str(depth1 + 1) + '.DiskCount', HostGroups[depth1].get('DiskCount'))
			if HostGroups[depth1].get('AutoRenew') is not None:
				self.add_query_param('HostGroup.' + str(depth1 + 1) + '.AutoRenew', HostGroups[depth1].get('AutoRenew'))
			if HostGroups[depth1].get('HostGroupId') is not None:
				self.add_query_param('HostGroup.' + str(depth1 + 1) + '.HostGroupId', HostGroups[depth1].get('HostGroupId'))
			if HostGroups[depth1].get('NodeCount') is not None:
				self.add_query_param('HostGroup.' + str(depth1 + 1) + '.NodeCount', HostGroups[depth1].get('NodeCount'))
			if HostGroups[depth1].get('InstanceType') is not None:
				self.add_query_param('HostGroup.' + str(depth1 + 1) + '.InstanceType', HostGroups[depth1].get('InstanceType'))
			if HostGroups[depth1].get('Comment') is not None:
				self.add_query_param('HostGroup.' + str(depth1 + 1) + '.Comment', HostGroups[depth1].get('Comment'))
			if HostGroups[depth1].get('ChargeType') is not None:
				self.add_query_param('HostGroup.' + str(depth1 + 1) + '.ChargeType', HostGroups[depth1].get('ChargeType'))
			if HostGroups[depth1].get('CreateType') is not None:
				self.add_query_param('HostGroup.' + str(depth1 + 1) + '.CreateType', HostGroups[depth1].get('CreateType'))
			if HostGroups[depth1].get('HostPassword') is not None:
				self.add_query_param('HostGroup.' + str(depth1 + 1) + '.HostPassword', HostGroups[depth1].get('HostPassword'))
			if HostGroups[depth1].get('HostGroupType') is not None:
				self.add_query_param('HostGroup.' + str(depth1 + 1) + '.HostGroupType', HostGroups[depth1].get('HostGroupType'))
			if HostGroups[depth1].get('PrivatePoolOptionsMatchCriteria') is not None:
				self.add_query_param('HostGroup.' + str(depth1 + 1) + '.PrivatePoolOptionsMatchCriteria', HostGroups[depth1].get('PrivatePoolOptionsMatchCriteria'))

	def get_PromotionInfos(self):
		return self.get_query_params().get('PromotionInfo')

	def set_PromotionInfos(self, PromotionInfos):
		for depth1 in range(len(PromotionInfos)):
			if PromotionInfos[depth1].get('PromotionOptionCode') is not None:
				self.add_query_param('PromotionInfo.' + str(depth1 + 1) + '.PromotionOptionCode', PromotionInfos[depth1].get('PromotionOptionCode'))
			if PromotionInfos[depth1].get('ProductCode') is not None:
				self.add_query_param('PromotionInfo.' + str(depth1 + 1) + '.ProductCode', PromotionInfos[depth1].get('ProductCode'))
			if PromotionInfos[depth1].get('PromotionOptionNo') is not None:
				self.add_query_param('PromotionInfo.' + str(depth1 + 1) + '.PromotionOptionNo', PromotionInfos[depth1].get('PromotionOptionNo'))