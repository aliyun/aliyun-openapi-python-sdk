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

class ConfigureDrdsDbInstancesRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Drds', '2019-01-23', 'ConfigureDrdsDbInstances','drds')

	def get_DbName(self):
		return self.get_query_params().get('DbName')

	def set_DbName(self,DbName):
		self.add_query_param('DbName',DbName)

	def get_DbInstances(self):
		return self.get_query_params().get('DbInstances')

	def set_DbInstances(self,DbInstances):
		for i in range(len(DbInstances)):	
			if DbInstances[i].get('SlaveDbInstanceType') is not None:
				self.add_query_param('DbInstance.' + str(i + 1) + '.SlaveDbInstanceType' , DbInstances[i].get('SlaveDbInstanceType'))
			if DbInstances[i].get('SlaveDbInstanceId') is not None:
				self.add_query_param('DbInstance.' + str(i + 1) + '.SlaveDbInstanceId' , DbInstances[i].get('SlaveDbInstanceId'))
			if DbInstances[i].get('MasterDbInstanceId') is not None:
				self.add_query_param('DbInstance.' + str(i + 1) + '.MasterDbInstanceId' , DbInstances[i].get('MasterDbInstanceId'))


	def get_DrdsInstanceId(self):
		return self.get_query_params().get('DrdsInstanceId')

	def set_DrdsInstanceId(self,DrdsInstanceId):
		self.add_query_param('DrdsInstanceId',DrdsInstanceId)