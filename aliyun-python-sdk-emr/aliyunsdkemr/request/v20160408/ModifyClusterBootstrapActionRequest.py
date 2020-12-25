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
from aliyunsdkemr.endpoint import endpoint_data

class ModifyClusterBootstrapActionRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Emr', '2016-04-08', 'ModifyClusterBootstrapAction','emr')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_ClusterId(self):
		return self.get_query_params().get('ClusterId')

	def set_ClusterId(self,ClusterId):
		self.add_query_param('ClusterId',ClusterId)

	def get_BootstrapActions(self):
		return self.get_query_params().get('BootstrapAction')

	def set_BootstrapActions(self, BootstrapActions):
		for depth1 in range(len(BootstrapActions)):
			if BootstrapActions[depth1].get('Path') is not None:
				self.add_query_param('BootstrapAction.' + str(depth1 + 1) + '.Path', BootstrapActions[depth1].get('Path'))
			if BootstrapActions[depth1].get('ExecutionTarget') is not None:
				self.add_query_param('BootstrapAction.' + str(depth1 + 1) + '.ExecutionTarget', BootstrapActions[depth1].get('ExecutionTarget'))
			if BootstrapActions[depth1].get('ExecutionMoment') is not None:
				self.add_query_param('BootstrapAction.' + str(depth1 + 1) + '.ExecutionMoment', BootstrapActions[depth1].get('ExecutionMoment'))
			if BootstrapActions[depth1].get('Arg') is not None:
				self.add_query_param('BootstrapAction.' + str(depth1 + 1) + '.Arg', BootstrapActions[depth1].get('Arg'))
			if BootstrapActions[depth1].get('Name') is not None:
				self.add_query_param('BootstrapAction.' + str(depth1 + 1) + '.Name', BootstrapActions[depth1].get('Name'))
			if BootstrapActions[depth1].get('ExecutionFailStrategy') is not None:
				self.add_query_param('BootstrapAction.' + str(depth1 + 1) + '.ExecutionFailStrategy', BootstrapActions[depth1].get('ExecutionFailStrategy'))

	def get_Id(self):
		return self.get_query_params().get('Id')

	def set_Id(self,Id):
		self.add_query_param('Id',Id)