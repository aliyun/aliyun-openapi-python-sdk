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

class RearrangeDbToInstanceRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Drds', '2019-01-23', 'RearrangeDbToInstance','drds')

	def get_ChooseSubDb(self):
		return self.get_query_params().get('ChooseSubDb')

	def set_ChooseSubDb(self,ChooseSubDb):
		self.add_query_param('ChooseSubDb',ChooseSubDb)

	def get_InstanceLists(self):
		return self.get_query_params().get('InstanceLists')

	def set_InstanceLists(self,InstanceLists):
		for i in range(len(InstanceLists)):	
			if InstanceLists[i] is not None:
				self.add_query_param('InstanceList.' + str(i + 1) , InstanceLists[i]);

	def get_DbName(self):
		return self.get_query_params().get('DbName')

	def set_DbName(self,DbName):
		self.add_query_param('DbName',DbName)

	def get_OrderId(self):
		return self.get_query_params().get('OrderId')

	def set_OrderId(self,OrderId):
		self.add_query_param('OrderId',OrderId)

	def get_ChooseRds(self):
		return self.get_query_params().get('ChooseRds')

	def set_ChooseRds(self,ChooseRds):
		self.add_query_param('ChooseRds',ChooseRds)

	def get_DrdsInstanceId(self):
		return self.get_query_params().get('DrdsInstanceId')

	def set_DrdsInstanceId(self,DrdsInstanceId):
		self.add_query_param('DrdsInstanceId',DrdsInstanceId)