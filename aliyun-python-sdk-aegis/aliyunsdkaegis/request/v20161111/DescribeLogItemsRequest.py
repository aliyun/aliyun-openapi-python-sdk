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
class DescribeLogItemsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'aegis', '2016-11-11', 'DescribeLogItems','vipaegis')

	def get_LoginOffset(self):
		return self.get_query_params().get('LoginOffset')

	def set_LoginOffset(self,LoginOffset):
		self.add_query_param('LoginOffset',LoginOffset)

	def get_ProcessSnapshotOffset(self):
		return self.get_query_params().get('ProcessSnapshotOffset')

	def set_ProcessSnapshotOffset(self,ProcessSnapshotOffset):
		self.add_query_param('ProcessSnapshotOffset',ProcessSnapshotOffset)

	def get_PortSnapshotOffset(self):
		return self.get_query_params().get('PortSnapshotOffset')

	def set_PortSnapshotOffset(self,PortSnapshotOffset):
		self.add_query_param('PortSnapshotOffset',PortSnapshotOffset)

	def get_Query(self):
		return self.get_query_params().get('Query')

	def set_Query(self,Query):
		self.add_query_param('Query',Query)

	def get_EndTime(self):
		return self.get_query_params().get('EndTime')

	def set_EndTime(self,EndTime):
		self.add_query_param('EndTime',EndTime)

	def get_CurrentPage(self):
		return self.get_query_params().get('CurrentPage')

	def set_CurrentPage(self,CurrentPage):
		self.add_query_param('CurrentPage',CurrentPage)

	def get_NetworkOffset(self):
		return self.get_query_params().get('NetworkOffset')

	def set_NetworkOffset(self,NetworkOffset):
		self.add_query_param('NetworkOffset',NetworkOffset)

	def get_StartTime(self):
		return self.get_query_params().get('StartTime')

	def set_StartTime(self,StartTime):
		self.add_query_param('StartTime',StartTime)

	def get_AccountSnapshotOffset(self):
		return self.get_query_params().get('AccountSnapshotOffset')

	def set_AccountSnapshotOffset(self,AccountSnapshotOffset):
		self.add_query_param('AccountSnapshotOffset',AccountSnapshotOffset)

	def get_ProcessOffset(self):
		return self.get_query_params().get('ProcessOffset')

	def set_ProcessOffset(self,ProcessOffset):
		self.add_query_param('ProcessOffset',ProcessOffset)

	def get_SourceIp(self):
		return self.get_query_params().get('SourceIp')

	def set_SourceIp(self,SourceIp):
		self.add_query_param('SourceIp',SourceIp)

	def get_CrackOffset(self):
		return self.get_query_params().get('CrackOffset')

	def set_CrackOffset(self,CrackOffset):
		self.add_query_param('CrackOffset',CrackOffset)

	def get_PageSize(self):
		return self.get_query_params().get('PageSize')

	def set_PageSize(self,PageSize):
		self.add_query_param('PageSize',PageSize)