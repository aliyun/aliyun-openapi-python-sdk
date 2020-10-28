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
from aliyunsdkdrds.endpoint import endpoint_data

class SubmitSmoothExpandTaskRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Drds', '2019-01-23', 'SubmitSmoothExpandTask','Drds')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_DrdsInstanceId(self):
		return self.get_query_params().get('DrdsInstanceId')

	def set_DrdsInstanceId(self,DrdsInstanceId):
		self.add_query_param('DrdsInstanceId',DrdsInstanceId)

	def get_DbInstanceIsCreating(self):
		return self.get_query_params().get('DbInstanceIsCreating')

	def set_DbInstanceIsCreating(self,DbInstanceIsCreating):
		self.add_query_param('DbInstanceIsCreating',DbInstanceIsCreating)

	def get_RdsSuperInstancess(self):
		return self.get_query_params().get('RdsSuperInstances')

	def set_RdsSuperInstancess(self, RdsSuperInstancess):
		for depth1 in range(len(RdsSuperInstancess)):
			if RdsSuperInstancess[depth1].get('Password') is not None:
				self.add_query_param('RdsSuperInstances.' + str(depth1 + 1) + '.Password', RdsSuperInstancess[depth1].get('Password'))
			if RdsSuperInstancess[depth1].get('AccountName') is not None:
				self.add_query_param('RdsSuperInstances.' + str(depth1 + 1) + '.AccountName', RdsSuperInstancess[depth1].get('AccountName'))
			if RdsSuperInstancess[depth1].get('RdsName') is not None:
				self.add_query_param('RdsSuperInstances.' + str(depth1 + 1) + '.RdsName', RdsSuperInstancess[depth1].get('RdsName'))

	def get_DbName(self):
		return self.get_query_params().get('DbName')

	def set_DbName(self,DbName):
		self.add_query_param('DbName',DbName)

	def get_TransferTaskInfoss(self):
		return self.get_query_params().get('TransferTaskInfos')

	def set_TransferTaskInfoss(self, TransferTaskInfoss):
		for depth1 in range(len(TransferTaskInfoss)):
			if TransferTaskInfoss[depth1].get('DbName') is not None:
				self.add_query_param('TransferTaskInfos.' + str(depth1 + 1) + '.DbName', TransferTaskInfoss[depth1].get('DbName'))
			if TransferTaskInfoss[depth1].get('SrcInstanceName') is not None:
				self.add_query_param('TransferTaskInfos.' + str(depth1 + 1) + '.SrcInstanceName', TransferTaskInfoss[depth1].get('SrcInstanceName'))
			if TransferTaskInfoss[depth1].get('InstanceType') is not None:
				self.add_query_param('TransferTaskInfos.' + str(depth1 + 1) + '.InstanceType', TransferTaskInfoss[depth1].get('InstanceType'))
			if TransferTaskInfoss[depth1].get('DstInstanceName') is not None:
				self.add_query_param('TransferTaskInfos.' + str(depth1 + 1) + '.DstInstanceName', TransferTaskInfoss[depth1].get('DstInstanceName'))