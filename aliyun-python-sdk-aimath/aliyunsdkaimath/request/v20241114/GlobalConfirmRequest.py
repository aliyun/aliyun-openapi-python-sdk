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

class GlobalConfirmRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'AIMath', '2024-11-14', 'GlobalConfirm')
		self.set_protocol_type('https')
		self.set_method('POST')

	def get_Tag(self): # String
		return self.get_body_params().get('Tag')

	def set_Tag(self, Tag):  # String
		self.add_body_params('Tag', Tag)
	def get_ExerciseCode(self): # String
		return self.get_body_params().get('ExerciseCode')

	def set_ExerciseCode(self, ExerciseCode):  # String
		self.add_body_params('ExerciseCode', ExerciseCode)
