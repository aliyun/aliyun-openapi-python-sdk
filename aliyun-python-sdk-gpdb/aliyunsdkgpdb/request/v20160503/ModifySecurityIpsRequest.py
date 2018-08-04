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
class ModifySecurityIpsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'gpdb', '2016-05-03', 'ModifySecurityIps','gpdb')

	def get_SecurityIPList(self):
		return self.get_query_params().get('SecurityIPList')

	def set_SecurityIPList(self,SecurityIPList):
		self.add_query_param('SecurityIPList',SecurityIPList)

	def get_DBInstanceIPArrayName(self):
		return self.get_query_params().get('DBInstanceIPArrayName')

	def set_DBInstanceIPArrayName(self,DBInstanceIPArrayName):
		self.add_query_param('DBInstanceIPArrayName',DBInstanceIPArrayName)

	def get_DBInstanceIPArrayAttribute(self):
		return self.get_query_params().get('DBInstanceIPArrayAttribute')

	def set_DBInstanceIPArrayAttribute(self,DBInstanceIPArrayAttribute):
		self.add_query_param('DBInstanceIPArrayAttribute',DBInstanceIPArrayAttribute)

	def get_DBInstanceId(self):
		return self.get_query_params().get('DBInstanceId')

	def set_DBInstanceId(self,DBInstanceId):
		self.add_query_param('DBInstanceId',DBInstanceId)