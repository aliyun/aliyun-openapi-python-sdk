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
class ResizeClusterRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Emr', '2016-04-08', 'ResizeCluster')

	def get_ClusterId(self):
		return self.get_query_params().get('ClusterId')

	def set_ClusterId(self,ClusterId):
		self.add_query_param('ClusterId',ClusterId)

	def get_NewMasterInstances(self):
		return self.get_query_params().get('NewMasterInstances')

	def set_NewMasterInstances(self,NewMasterInstances):
		self.add_query_param('NewMasterInstances',NewMasterInstances)

	def get_NewCoreInstances(self):
		return self.get_query_params().get('NewCoreInstances')

	def set_NewCoreInstances(self,NewCoreInstances):
		self.add_query_param('NewCoreInstances',NewCoreInstances)

	def get_NewTaskInstances(self):
		return self.get_query_params().get('NewTaskInstances')

	def set_NewTaskInstances(self,NewTaskInstances):
		self.add_query_param('NewTaskInstances',NewTaskInstances)

	def get_ChargeType(self):
		return self.get_query_params().get('ChargeType')

	def set_ChargeType(self,ChargeType):
		self.add_query_param('ChargeType',ChargeType)

	def get_Period(self):
		return self.get_query_params().get('Period')

	def set_Period(self,Period):
		self.add_query_param('Period',Period)

	def get_AutoRenew(self):
		return self.get_query_params().get('AutoRenew')

	def set_AutoRenew(self,AutoRenew):
		self.add_query_param('AutoRenew',AutoRenew)