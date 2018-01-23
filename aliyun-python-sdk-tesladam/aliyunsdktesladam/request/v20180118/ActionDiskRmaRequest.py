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
class ActionDiskRmaRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'TeslaDam', '2018-01-18', 'ActionDiskRma')

	def get_DiskName(self):
		return self.get_query_params().get('DiskName')

	def set_DiskName(self,DiskName):
		self.add_query_param('DiskName',DiskName)

	def get_ExecutionId(self):
		return self.get_query_params().get('ExecutionId')

	def set_ExecutionId(self,ExecutionId):
		self.add_query_param('ExecutionId',ExecutionId)

	def get_DiskSlot(self):
		return self.get_query_params().get('DiskSlot')

	def set_DiskSlot(self,DiskSlot):
		self.add_query_param('DiskSlot',DiskSlot)

	def get_Hostname(self):
		return self.get_query_params().get('Hostname')

	def set_Hostname(self,Hostname):
		self.add_query_param('Hostname',Hostname)

	def get_DiskMount(self):
		return self.get_query_params().get('DiskMount')

	def set_DiskMount(self,DiskMount):
		self.add_query_param('DiskMount',DiskMount)

	def get_DiskReason(self):
		return self.get_query_params().get('DiskReason')

	def set_DiskReason(self,DiskReason):
		self.add_query_param('DiskReason',DiskReason)

	def get_DiskSn(self):
		return self.get_query_params().get('DiskSn')

	def set_DiskSn(self,DiskSn):
		self.add_query_param('DiskSn',DiskSn)