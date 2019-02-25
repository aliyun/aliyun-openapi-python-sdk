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
class UpdateDataDispatchConfigRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'LinkWAN', '2018-12-30', 'UpdateDataDispatchConfig','linkwan')
		self.set_protocol_type('https');

	def get_UplinkTopic(self):
		return self.get_body_params().get('UplinkTopic')

	def set_UplinkTopic(self,UplinkTopic):
		self.add_body_params('UplinkTopic', UplinkTopic)

	def get_ProductKey(self):
		return self.get_body_params().get('ProductKey')

	def set_ProductKey(self,ProductKey):
		self.add_body_params('ProductKey', ProductKey)

	def get_ProductType(self):
		return self.get_body_params().get('ProductType')

	def set_ProductType(self,ProductType):
		self.add_body_params('ProductType', ProductType)

	def get_ProductName(self):
		return self.get_body_params().get('ProductName')

	def set_ProductName(self,ProductName):
		self.add_body_params('ProductName', ProductName)

	def get_UplinkRegionName(self):
		return self.get_body_params().get('UplinkRegionName')

	def set_UplinkRegionName(self,UplinkRegionName):
		self.add_body_params('UplinkRegionName', UplinkRegionName)

	def get_NodeGroupId(self):
		return self.get_body_params().get('NodeGroupId')

	def set_NodeGroupId(self,NodeGroupId):
		self.add_body_params('NodeGroupId', NodeGroupId)

	def get_DataDispatchDestination(self):
		return self.get_body_params().get('DataDispatchDestination')

	def set_DataDispatchDestination(self,DataDispatchDestination):
		self.add_body_params('DataDispatchDestination', DataDispatchDestination)