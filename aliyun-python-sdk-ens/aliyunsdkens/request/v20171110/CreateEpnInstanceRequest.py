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

class CreateEpnInstanceRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ens', '2017-11-10', 'CreateEpnInstance','ens')
		self.set_method('POST')

	def get_NetworkingModel(self):
		return self.get_query_params().get('NetworkingModel')

	def set_NetworkingModel(self,NetworkingModel):
		self.add_query_param('NetworkingModel',NetworkingModel)

	def get_InternetMaxBandwidthOut(self):
		return self.get_query_params().get('InternetMaxBandwidthOut')

	def set_InternetMaxBandwidthOut(self,InternetMaxBandwidthOut):
		self.add_query_param('InternetMaxBandwidthOut',InternetMaxBandwidthOut)

	def get_EPNInstanceType(self):
		return self.get_query_params().get('EPNInstanceType')

	def set_EPNInstanceType(self,EPNInstanceType):
		self.add_query_param('EPNInstanceType',EPNInstanceType)

	def get_InternetChargeType(self):
		return self.get_query_params().get('InternetChargeType')

	def set_InternetChargeType(self,InternetChargeType):
		self.add_query_param('InternetChargeType',InternetChargeType)

	def get_EPNInstanceName(self):
		return self.get_query_params().get('EPNInstanceName')

	def set_EPNInstanceName(self,EPNInstanceName):
		self.add_query_param('EPNInstanceName',EPNInstanceName)