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
class TaskConfigEnableRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Cms', '2018-03-08', 'TaskConfigEnable','cms')

	def get_IdLists(self):
		return self.get_query_params().get('IdLists')

	def set_IdLists(self,IdLists):
		for i in range(len(IdLists)):	
			if IdLists[i] is not None:
				self.add_query_param('IdList.' + str(i + 1) , IdLists[i]);

	def get_Enabled(self):
		return self.get_query_params().get('Enabled')

	def set_Enabled(self,Enabled):
		self.add_query_param('Enabled',Enabled)