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

from aliyunsdkcore.request import RoaRequest
import json

class AICreateSessionMessageRequest(RoaRequest):

	def __init__(self):
		RoaRequest.__init__(self, 'qianzhou', '2021-11-11', 'AICreateSessionMessage')
		self.set_uri_pattern('/popapi/AICreateSessionMessage')
		self.set_method('POST')

	def get_employee_id(self): # String
		return self.get_query_params().get('employee_id')

	def set_employee_id(self, employee_id):  # String
		self.add_query_param('employee_id', employee_id)
	def get_body(self): # Struct
		return self.get_body_params().get('body')

	def set_body(self, body):  # Struct
		self.add_body_params("body", json.dumps(body))
