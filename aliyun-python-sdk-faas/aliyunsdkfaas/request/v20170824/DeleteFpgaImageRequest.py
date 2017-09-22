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
class DeleteFpgaImageRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'faas', '2017-08-24', 'DeleteFpgaImage')
		self.set_method('POST')

	def get_FpgaImageUUID(self):
		return self.get_query_params().get('FpgaImageUUID')

	def set_FpgaImageUUID(self,FpgaImageUUID):
		self.add_query_param('FpgaImageUUID',FpgaImageUUID)

	def get_callerUid(self):
		return self.get_query_params().get('callerUid')

	def set_callerUid(self,callerUid):
		self.add_query_param('callerUid',callerUid)