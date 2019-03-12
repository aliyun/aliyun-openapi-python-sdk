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
class CreateMulticastGroupRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'LinkWAN', '2018-12-30', 'CreateMulticastGroup','linkwan')

	def get_ClassMode(self):
		return self.get_body_params().get('ClassMode')

	def set_ClassMode(self,ClassMode):
		self.add_body_params('ClassMode', ClassMode)

	def get_Frequency(self):
		return self.get_body_params().get('Frequency')

	def set_Frequency(self,Frequency):
		self.add_body_params('Frequency', Frequency)

	def get_LoraVersion(self):
		return self.get_body_params().get('LoraVersion')

	def set_LoraVersion(self,LoraVersion):
		self.add_body_params('LoraVersion', LoraVersion)

	def get_Periodicity(self):
		return self.get_body_params().get('Periodicity')

	def set_Periodicity(self,Periodicity):
		self.add_body_params('Periodicity', Periodicity)

	def get_DataRate(self):
		return self.get_body_params().get('DataRate')

	def set_DataRate(self,DataRate):
		self.add_body_params('DataRate', DataRate)