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

class AddHpHostRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Emr', '2016-04-08', 'AddHpHost','emr')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_HpHosts(self):
		return self.get_query_params().get('HpHosts')

	def set_HpHosts(self,HpHosts):
		for i in range(len(HpHosts)):	
			if HpHosts[i].get('CpuCore') is not None:
				self.add_query_param('HpHost.' + str(i + 1) + '.CpuCore' , HpHosts[i].get('CpuCore'))
			if HpHosts[i].get('MemSize') is not None:
				self.add_query_param('HpHost.' + str(i + 1) + '.MemSize' , HpHosts[i].get('MemSize'))
			if HpHosts[i].get('RackInfo') is not None:
				self.add_query_param('HpHost.' + str(i + 1) + '.RackInfo' , HpHosts[i].get('RackInfo'))
			if HpHosts[i].get('Role') is not None:
				self.add_query_param('HpHost.' + str(i + 1) + '.Role' , HpHosts[i].get('Role'))
			if HpHosts[i].get('SerialNumber') is not None:
				self.add_query_param('HpHost.' + str(i + 1) + '.SerialNumber' , HpHosts[i].get('SerialNumber'))
			if HpHosts[i].get('HostType') is not None:
				self.add_query_param('HpHost.' + str(i + 1) + '.HostType' , HpHosts[i].get('HostType'))
			if HpHosts[i].get('SecurityGroupId') is not None:
				self.add_query_param('HpHost.' + str(i + 1) + '.SecurityGroupId' , HpHosts[i].get('SecurityGroupId'))
			for j in range(len(HpHosts[i].get('HpHostDisks'))):
				if HpHosts[i].get('HpHostDisks')[j] is not None:
					self.add_query_param('HpHost.' + str(i + 1) + '.HpHostDisk.'+str(j + 1), HpHosts[i].get('HpHostDisks')[j])
			if HpHosts[i].get('VswitchId') is not None:
				self.add_query_param('HpHost.' + str(i + 1) + '.VswitchId' , HpHosts[i].get('VswitchId'))
			if HpHosts[i].get('ExternalKey') is not None:
				self.add_query_param('HpHost.' + str(i + 1) + '.ExternalKey' , HpHosts[i].get('ExternalKey'))
			if HpHosts[i].get('HostName') is not None:
				self.add_query_param('HpHost.' + str(i + 1) + '.HostName' , HpHosts[i].get('HostName'))
			if HpHosts[i].get('VpcId') is not None:
				self.add_query_param('HpHost.' + str(i + 1) + '.VpcId' , HpHosts[i].get('VpcId'))
			if HpHosts[i].get('InnerIp') is not None:
				self.add_query_param('HpHost.' + str(i + 1) + '.InnerIp' , HpHosts[i].get('InnerIp'))
			if HpHosts[i].get('ExternalIp') is not None:
				self.add_query_param('HpHost.' + str(i + 1) + '.ExternalIp' , HpHosts[i].get('ExternalIp'))


	def get_HpBizId(self):
		return self.get_query_params().get('HpBizId')

	def set_HpBizId(self,HpBizId):
		self.add_query_param('HpBizId',HpBizId)