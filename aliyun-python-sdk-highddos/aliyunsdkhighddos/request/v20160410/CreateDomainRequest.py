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
class CreateDomainRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'HighDDos', '2016-04-10', 'CreateDomain')

	def get_InstanceId(self):
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self,InstanceId):
		self.add_query_param('InstanceId',InstanceId)

	def get_Domain(self):
		return self.get_query_params().get('Domain')

	def set_Domain(self,Domain):
		self.add_query_param('Domain',Domain)

	def get_Protocols(self):
		return self.get_query_params().get('Protocols')

	def set_Protocols(self,Protocols):
		self.add_query_param('Protocols',Protocols)

	def get_SourceIps(self):
		return self.get_query_params().get('SourceIps')

	def set_SourceIps(self,SourceIps):
		self.add_query_param('SourceIps',SourceIps)

	def get_WafEnable(self):
		return self.get_query_params().get('WafEnable')

	def set_WafEnable(self,WafEnable):
		self.add_query_param('WafEnable',WafEnable)

	def get_CcEnable(self):
		return self.get_query_params().get('CcEnable')

	def set_CcEnable(self,CcEnable):
		self.add_query_param('CcEnable',CcEnable)