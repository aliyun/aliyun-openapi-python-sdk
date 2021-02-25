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

class RevokeFeedbackRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'safconsole', '2021-01-12', 'RevokeFeedback','saf')
		self.set_method('POST')

	def get_SampleType(self):
		return self.get_body_params().get('SampleType')

	def set_SampleType(self,SampleType):
		self.add_body_params('SampleType', SampleType)

	def get_Value(self):
		return self.get_body_params().get('Value')

	def set_Value(self,Value):
		self.add_body_params('Value', Value)