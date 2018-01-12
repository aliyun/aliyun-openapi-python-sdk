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
class RenewClusterRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Emr', '2016-04-08', 'RenewCluster')

	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_ClusterId(self):
		return self.get_query_params().get('ClusterId')

	def set_ClusterId(self,ClusterId):
		self.add_query_param('ClusterId',ClusterId)

	def get_RenewEcsDos(self):
		return self.get_query_params().get('RenewEcsDos')

	def set_RenewEcsDos(self,RenewEcsDos):
		for i in range(len(RenewEcsDos)):	
			self.add_query_param('RenewEcsDo.' + str(i + 1) + '.EcsId' , RenewEcsDos[i].get('EcsId'))
			self.add_query_param('RenewEcsDo.' + str(i + 1) + '.EcsPeriod' , RenewEcsDos[i].get('EcsPeriod'))
			self.add_query_param('RenewEcsDo.' + str(i + 1) + '.EmrPeriod' , RenewEcsDos[i].get('EmrPeriod'))
