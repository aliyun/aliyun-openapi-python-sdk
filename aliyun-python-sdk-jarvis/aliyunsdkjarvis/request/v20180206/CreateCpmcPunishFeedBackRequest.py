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
class CreateCpmcPunishFeedBackRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'jarvis', '2018-02-06', 'CreateCpmcPunishFeedBack')

	def get_FeedBack(self):
		return self.get_query_params().get('FeedBack')

	def set_FeedBack(self,FeedBack):
		self.add_query_param('FeedBack',FeedBack)

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

	def get_ProtocolName(self):
		return self.get_query_params().get('ProtocolName')

	def set_ProtocolName(self,ProtocolName):
		self.add_query_param('ProtocolName',ProtocolName)

	def get_SrcPort(self):
		return self.get_query_params().get('SrcPort')

	def set_SrcPort(self,SrcPort):
		self.add_query_param('SrcPort',SrcPort)

	def get_PunishType(self):
		return self.get_query_params().get('PunishType')

	def set_PunishType(self,PunishType):
		self.add_query_param('PunishType',PunishType)

	def get_GmtCreate(self):
		return self.get_query_params().get('GmtCreate')

	def set_GmtCreate(self,GmtCreate):
		self.add_query_param('GmtCreate',GmtCreate)

	def get_DstIP(self):
		return self.get_query_params().get('DstIP')

	def set_DstIP(self,DstIP):
		self.add_query_param('DstIP',DstIP)

	def get_Lang(self):
		return self.get_query_params().get('Lang')

	def set_Lang(self,Lang):
		self.add_query_param('Lang',Lang)

	def get_SourceCode(self):
		return self.get_query_params().get('SourceCode')

	def set_SourceCode(self,SourceCode):
		self.add_query_param('SourceCode',SourceCode)