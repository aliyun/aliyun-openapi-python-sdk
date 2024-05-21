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
class ConfigAutoRenewRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'cloudwf', '2017-03-28', 'ConfigAutoRenew','cloudwf')

	def get_OffsetDays(self):
		return self.get_query_params().get('OffsetDays')

	def set_OffsetDays(self,OffsetDays):
		self.add_query_param('OffsetDays',OffsetDays)

	def get_Months(self):
		return self.get_query_params().get('Months')

	def set_Months(self,Months):
		self.add_query_param('Months',Months)

	def get_AutoRenew(self):
		return self.get_query_params().get('AutoRenew')

	def set_AutoRenew(self,AutoRenew):
		self.add_query_param('AutoRenew',AutoRenew)

	def get_ApLists(self):
		return self.get_query_params().get('ApLists')

	def set_ApLists(self,ApLists):
		for i in range(len(ApLists)):	
			if ApLists[i] is not None:
				self.add_query_param('ApList.' + str(i + 1) , ApLists[i]);