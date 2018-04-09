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
class QueryPriceForModifyConfigRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Emr', '2016-04-08', 'QueryPriceForModifyConfig')

	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_ModifyConfigSpecs(self):
		return self.get_query_params().get('ModifyConfigSpecs')

	def set_ModifyConfigSpecs(self,ModifyConfigSpecs):
		for i in range(len(ModifyConfigSpecs)):	
			if ModifyConfigSpecs[i].get('HostGroupId') is not None:
				self.add_query_param('ModifyConfigSpec.' + str(i + 1) + '.HostGroupId' , ModifyConfigSpecs[i].get('HostGroupId'))
			if ModifyConfigSpecs[i].get('NewInstanceType') is not None:
				self.add_query_param('ModifyConfigSpec.' + str(i + 1) + '.NewInstanceType' , ModifyConfigSpecs[i].get('NewInstanceType'))
			if ModifyConfigSpecs[i].get('NewDiskSize') is not None:
				self.add_query_param('ModifyConfigSpec.' + str(i + 1) + '.NewDiskSize' , ModifyConfigSpecs[i].get('NewDiskSize'))


	def get_ClusterId(self):
		return self.get_query_params().get('ClusterId')

	def set_ClusterId(self,ClusterId):
		self.add_query_param('ClusterId',ClusterId)