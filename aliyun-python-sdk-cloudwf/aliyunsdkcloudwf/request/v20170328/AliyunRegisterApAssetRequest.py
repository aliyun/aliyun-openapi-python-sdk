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
class AliyunRegisterApAssetRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'cloudwf', '2017-03-28', 'AliyunRegisterApAsset','cloudwf')

	def get_ApgroupId(self):
		return self.get_query_params().get('ApgroupId')

	def set_ApgroupId(self,ApgroupId):
		self.add_query_param('ApgroupId',ApgroupId)

	def get_Mac(self):
		return self.get_query_params().get('Mac')

	def set_Mac(self,Mac):
		self.add_query_param('Mac',Mac)

	def get_SerialNo(self):
		return self.get_query_params().get('SerialNo')

	def set_SerialNo(self,SerialNo):
		self.add_query_param('SerialNo',SerialNo)