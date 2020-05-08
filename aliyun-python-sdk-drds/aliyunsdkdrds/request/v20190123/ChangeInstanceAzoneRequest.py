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

class ChangeInstanceAzoneRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Drds', '2019-01-23', 'ChangeInstanceAzone','drds')

	def get_OriginAzoneId(self):
		return self.get_query_params().get('OriginAzoneId')

	def set_OriginAzoneId(self,OriginAzoneId):
		self.add_query_param('OriginAzoneId',OriginAzoneId)

	def get_TargetAzoneId(self):
		return self.get_query_params().get('TargetAzoneId')

	def set_TargetAzoneId(self,TargetAzoneId):
		self.add_query_param('TargetAzoneId',TargetAzoneId)

	def get_DrdsRegionId(self):
		return self.get_query_params().get('DrdsRegionId')

	def set_DrdsRegionId(self,DrdsRegionId):
		self.add_query_param('DrdsRegionId',DrdsRegionId)

	def get_DrdsInstanceId(self):
		return self.get_query_params().get('DrdsInstanceId')

	def set_DrdsInstanceId(self,DrdsInstanceId):
		self.add_query_param('DrdsInstanceId',DrdsInstanceId)