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

class CreateImportJobRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'hcs-mgw', '2017-10-24', 'CreateImportJob')
		self.set_method('POST')

	def get_IsCustomizedInstance(self):
		return self.get_query_params().get('IsCustomizedInstance')

	def set_IsCustomizedInstance(self,IsCustomizedInstance):
		self.add_query_param('IsCustomizedInstance',IsCustomizedInstance)

	def get_DestAddressRegionId(self):
		return self.get_query_params().get('DestAddressRegionId')

	def set_DestAddressRegionId(self,DestAddressRegionId):
		self.add_query_param('DestAddressRegionId',DestAddressRegionId)

	def get_DestBucket(self):
		return self.get_query_params().get('DestBucket')

	def set_DestBucket(self,DestBucket):
		self.add_query_param('DestBucket',DestBucket)

	def get_DestPrefix(self):
		return self.get_query_params().get('DestPrefix')

	def set_DestPrefix(self,DestPrefix):
		self.add_query_param('DestPrefix',DestPrefix)

	def get_TotalObjectNum(self):
		return self.get_query_params().get('TotalObjectNum')

	def set_TotalObjectNum(self,TotalObjectNum):
		self.add_query_param('TotalObjectNum',TotalObjectNum)

	def get_CustomizedInstances(self):
		return self.get_query_params().get('CustomizedInstances')

	def set_CustomizedInstances(self,CustomizedInstances):
		self.add_query_param('CustomizedInstances',CustomizedInstances)

	def get_IncrementalInterval(self):
		return self.get_query_params().get('IncrementalInterval')

	def set_IncrementalInterval(self,IncrementalInterval):
		self.add_query_param('IncrementalInterval',IncrementalInterval)

	def get_NetFlowLimiter(self):
		return self.get_query_params().get('NetFlowLimiter')

	def set_NetFlowLimiter(self,NetFlowLimiter):
		self.add_query_param('NetFlowLimiter',NetFlowLimiter)

	def get_SrcListFilePath(self):
		return self.get_query_params().get('SrcListFilePath')

	def set_SrcListFilePath(self,SrcListFilePath):
		self.add_query_param('SrcListFilePath',SrcListFilePath)

	def get_DestAccessKeyId(self):
		return self.get_query_params().get('DestAccessKeyId')

	def set_DestAccessKeyId(self,DestAccessKeyId):
		self.add_query_param('DestAccessKeyId',DestAccessKeyId)

	def get_SrcSubAddress(self):
		return self.get_query_params().get('SrcSubAddress')

	def set_SrcSubAddress(self,SrcSubAddress):
		self.add_query_param('SrcSubAddress',SrcSubAddress)

	def get_TotalObjectSize(self):
		return self.get_query_params().get('TotalObjectSize')

	def set_TotalObjectSize(self,TotalObjectSize):
		self.add_query_param('TotalObjectSize',TotalObjectSize)

	def get_SrcDomain(self):
		return self.get_query_params().get('SrcDomain')

	def set_SrcDomain(self,SrcDomain):
		self.add_query_param('SrcDomain',SrcDomain)

	def get_SrcAddressRegionId(self):
		return self.get_query_params().get('SrcAddressRegionId')

	def set_SrcAddressRegionId(self,SrcAddressRegionId):
		self.add_query_param('SrcAddressRegionId',SrcAddressRegionId)

	def get_IncrementalMode(self):
		return self.get_query_params().get('IncrementalMode')

	def set_IncrementalMode(self,IncrementalMode):
		self.add_query_param('IncrementalMode',IncrementalMode)

	def get_SrcAddressType(self):
		return self.get_query_params().get('SrcAddressType')

	def set_SrcAddressType(self,SrcAddressType):
		self.add_query_param('SrcAddressType',SrcAddressType)

	def get_DestAccessKeySecret(self):
		return self.get_query_params().get('DestAccessKeySecret')

	def set_DestAccessKeySecret(self,DestAccessKeySecret):
		self.add_query_param('DestAccessKeySecret',DestAccessKeySecret)

	def get_SrcAppid(self):
		return self.get_query_params().get('SrcAppid')

	def set_SrcAppid(self,SrcAppid):
		self.add_query_param('SrcAppid',SrcAppid)

	def get_ExpectedImportTime(self):
		return self.get_query_params().get('ExpectedImportTime')

	def set_ExpectedImportTime(self,ExpectedImportTime):
		self.add_query_param('ExpectedImportTime',ExpectedImportTime)

	def get_SrcAddress(self):
		return self.get_query_params().get('SrcAddress')

	def set_SrcAddress(self,SrcAddress):
		self.add_query_param('SrcAddress',SrcAddress)

	def get_SrcAccessKeyId(self):
		return self.get_query_params().get('SrcAccessKeyId')

	def set_SrcAccessKeyId(self,SrcAccessKeyId):
		self.add_query_param('SrcAccessKeyId',SrcAccessKeyId)

	def get_Name(self):
		return self.get_query_params().get('Name')

	def set_Name(self,Name):
		self.add_query_param('Name',Name)

	def get_IncrementalRepeatCount(self):
		return self.get_query_params().get('IncrementalRepeatCount')

	def set_IncrementalRepeatCount(self,IncrementalRepeatCount):
		self.add_query_param('IncrementalRepeatCount',IncrementalRepeatCount)

	def get_SrcAccessKeySecret(self):
		return self.get_query_params().get('SrcAccessKeySecret')

	def set_SrcAccessKeySecret(self,SrcAccessKeySecret):
		self.add_query_param('SrcAccessKeySecret',SrcAccessKeySecret)