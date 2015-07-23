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
class ConfigDdosRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Yundun', '2015-04-16', 'ConfigDdos')

	def get_InstanceId(self):
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self,InstanceId):
		self.add_query_param('InstanceId',InstanceId)

	def get_InstanceType(self):
		return self.get_query_params().get('InstanceType')

	def set_InstanceType(self,InstanceType):
		self.add_query_param('InstanceType',InstanceType)

	def get_FlowPosition(self):
		return self.get_query_params().get('FlowPosition')

	def set_FlowPosition(self,FlowPosition):
		self.add_query_param('FlowPosition',FlowPosition)

	def get_StrategyPosition(self):
		return self.get_query_params().get('StrategyPosition')

	def set_StrategyPosition(self,StrategyPosition):
		self.add_query_param('StrategyPosition',StrategyPosition)

	def get_Level(self):
		return self.get_query_params().get('Level')

	def set_Level(self,Level):
		self.add_query_param('Level',Level)