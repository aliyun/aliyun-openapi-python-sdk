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

class BatchAuditTest01Request(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ft', '2018-07-13', 'BatchAuditTest01')

	def get_Demo01(self):
		return self.get_query_params().get('Demo01')

	def set_Demo01(self,Demo01):
		self.add_query_param('Demo01',Demo01)

	def get_Test010101(self):
		return self.get_body_params().get('Test010101')

	def set_Test010101(self,Test010101):
		self.add_body_params('Test010101', Test010101)

	def get_Name(self):
		return self.get_query_params().get('Name')

	def set_Name(self,Name):
		self.add_query_param('Name',Name)

	def get_BatchAuditTest01(self):
		return self.get_query_params().get('BatchAuditTest01')

	def set_BatchAuditTest01(self,BatchAuditTest01):
		self.add_query_param('BatchAuditTest01',BatchAuditTest01)