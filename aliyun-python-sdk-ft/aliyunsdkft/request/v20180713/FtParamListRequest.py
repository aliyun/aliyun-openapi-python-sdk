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

class FtParamListRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ft', '2018-07-13', 'FtParamList')

	def get_Disks(self):
		return self.get_query_params().get('Disks')

	def set_Disks(self,Disks):
		for i in range(len(Disks)):	
			for j in range(len(Disks[i].get('Sizes'))):
				if Disks[i].get('Sizes')[j] is not None:
					self.add_query_param('Disk.' + str(i + 1) + '.Size.'+str(j + 1), Disks[i].get('Sizes')[j])
			for j in range(len(Disks[i].get('Types'))):
				if Disks[i].get('Types')[j] is not None:
					self.add_query_param('Disk.' + str(i + 1) + '.Type.'+str(j + 1), Disks[i].get('Types')[j])


	def get_Name(self):
		return self.get_query_params().get('Name')

	def set_Name(self,Name):
		self.add_query_param('Name',Name)