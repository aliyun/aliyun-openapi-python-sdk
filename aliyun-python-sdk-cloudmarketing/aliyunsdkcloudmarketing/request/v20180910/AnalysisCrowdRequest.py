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

class AnalysisCrowdRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'cloudmarketing', '2018-09-10', 'AnalysisCrowd')
		self.set_method('POST')

	def get_TagIdss(self):
		return self.get_query_params().get('TagIdss')

	def set_TagIdss(self, TagIdss):
		for depth1 in range(len(TagIdss)):
			if TagIdss[depth1] is not None:
				self.add_query_param('TagIds.' + str(depth1 + 1) , TagIdss[depth1])

	def get_CrowdId(self):
		return self.get_query_params().get('CrowdId')

	def set_CrowdId(self,CrowdId):
		self.add_query_param('CrowdId',CrowdId)