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

class CreateImportJobExRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'hcs-mgw', '2017-10-24', 'CreateImportJobEx')
		self.set_method('POST')

	def get_IsCustomizedInstance(self):
		return self.get_query_params().get('IsCustomizedInstance')

	def set_IsCustomizedInstance(self,IsCustomizedInstance):
		self.add_query_param('IsCustomizedInstance',IsCustomizedInstance)

	def get_EnableMultiVersioning(self):
		return self.get_query_params().get('EnableMultiVersioning')

	def set_EnableMultiVersioning(self,EnableMultiVersioning):
		self.add_query_param('EnableMultiVersioning',EnableMultiVersioning)

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

	def get_IncludeDirOrFiles(self):
		return self.get_query_params().get('IncludeDirOrFiles')

	def set_IncludeDirOrFiles(self,IncludeDirOrFiles):
		self.add_query_param('IncludeDirOrFiles',IncludeDirOrFiles)

	def get_LastModifiedTime(self):
		return self.get_query_params().get('LastModifiedTime')

	def set_LastModifiedTime(self,LastModifiedTime):
		self.add_query_param('LastModifiedTime',LastModifiedTime)

	def get_TotalObjectSize(self):
		return self.get_query_params().get('TotalObjectSize')

	def set_TotalObjectSize(self,TotalObjectSize):
		self.add_query_param('TotalObjectSize',TotalObjectSize)

	def get_ExcludeDirOrFiles(self):
		return self.get_query_params().get('ExcludeDirOrFiles')

	def set_ExcludeDirOrFiles(self,ExcludeDirOrFiles):
		self.add_query_param('ExcludeDirOrFiles',ExcludeDirOrFiles)

	def get_FilterMode(self):
		return self.get_query_params().get('FilterMode')

	def set_FilterMode(self,FilterMode):
		self.add_query_param('FilterMode',FilterMode)

	def get_CoverageRule(self):
		return self.get_query_params().get('CoverageRule')

	def set_CoverageRule(self,CoverageRule):
		self.add_query_param('CoverageRule',CoverageRule)

	def get_IncrementalMode(self):
		return self.get_query_params().get('IncrementalMode')

	def set_IncrementalMode(self,IncrementalMode):
		self.add_query_param('IncrementalMode',IncrementalMode)

	def get_ExpectedImportTime(self):
		return self.get_query_params().get('ExpectedImportTime')

	def set_ExpectedImportTime(self,ExpectedImportTime):
		self.add_query_param('ExpectedImportTime',ExpectedImportTime)

	def get_AliasName(self):
		return self.get_query_params().get('AliasName')

	def set_AliasName(self,AliasName):
		self.add_query_param('AliasName',AliasName)

	def get_SrcAddress(self):
		return self.get_query_params().get('SrcAddress')

	def set_SrcAddress(self,SrcAddress):
		self.add_query_param('SrcAddress',SrcAddress)

	def get_Name(self):
		return self.get_query_params().get('Name')

	def set_Name(self,Name):
		self.add_query_param('Name',Name)

	def get_IncrementalRepeatCount(self):
		return self.get_query_params().get('IncrementalRepeatCount')

	def set_IncrementalRepeatCount(self,IncrementalRepeatCount):
		self.add_query_param('IncrementalRepeatCount',IncrementalRepeatCount)

	def get_DestAddress(self):
		return self.get_query_params().get('DestAddress')

	def set_DestAddress(self,DestAddress):
		self.add_query_param('DestAddress',DestAddress)