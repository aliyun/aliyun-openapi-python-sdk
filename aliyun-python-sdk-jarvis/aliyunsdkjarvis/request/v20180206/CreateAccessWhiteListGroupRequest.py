# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
class CreateAccessWhiteListGroupRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'jarvis', '2018-02-06', 'CreateAccessWhiteListGroup')

	def get_Note(self):
		return self.get_query_params().get('Note')

	def set_Note(self,Note):
		self.add_query_param('Note',Note)

	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_SrcIP(self):
		return self.get_query_params().get('SrcIP')

	def set_SrcIP(self,SrcIP):
		self.add_query_param('SrcIP',SrcIP)

	def get_SourceIp(self):
		return self.get_query_params().get('SourceIp')

	def set_SourceIp(self,SourceIp):
		self.add_query_param('SourceIp',SourceIp)

	def get_DstPort(self):
		return self.get_query_params().get('DstPort')

	def set_DstPort(self,DstPort):
		self.add_query_param('DstPort',DstPort)

	def get_InstanceIdList(self):
		return self.get_query_params().get('InstanceIdList')

	def set_InstanceIdList(self,InstanceIdList):
		self.add_query_param('InstanceIdList',InstanceIdList)

	def get_LiveTime(self):
		return self.get_query_params().get('LiveTime')

	def set_LiveTime(self,LiveTime):
		self.add_query_param('LiveTime',LiveTime)

	def get_ProductName(self):
		return self.get_query_params().get('ProductName')

	def set_ProductName(self,ProductName):
		self.add_query_param('ProductName',ProductName)

	def get_WhiteListType(self):
		return self.get_query_params().get('WhiteListType')

	def set_WhiteListType(self,WhiteListType):
		self.add_query_param('WhiteListType',WhiteListType)

	def get_Lang(self):
		return self.get_query_params().get('Lang')

	def set_Lang(self,Lang):
		self.add_query_param('Lang',Lang)

	def get_SourceCode(self):
		return self.get_query_params().get('SourceCode')

	def set_SourceCode(self,SourceCode):
		self.add_query_param('SourceCode',SourceCode)