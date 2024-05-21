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
class GetScanProbeTimeSerRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'cloudwf', '2017-03-28', 'GetScanProbeTimeSer','cloudwf')

	def get_ZoomStart(self):
		return self.get_query_params().get('ZoomStart')

	def set_ZoomStart(self,ZoomStart):
		self.add_query_param('ZoomStart',ZoomStart)

	def get_CompanyId(self):
		return self.get_query_params().get('CompanyId')

	def set_CompanyId(self,CompanyId):
		self.add_query_param('CompanyId',CompanyId)

	def get_ApgroupId(self):
		return self.get_query_params().get('ApgroupId')

	def set_ApgroupId(self,ApgroupId):
		self.add_query_param('ApgroupId',ApgroupId)

	def get_Start(self):
		return self.get_query_params().get('Start')

	def set_Start(self,Start):
		self.add_query_param('Start',Start)

	def get_ZoomEnd(self):
		return self.get_query_params().get('ZoomEnd')

	def set_ZoomEnd(self,ZoomEnd):
		self.add_query_param('ZoomEnd',ZoomEnd)

	def get_End(self):
		return self.get_query_params().get('End')

	def set_End(self,End):
		self.add_query_param('End',End)