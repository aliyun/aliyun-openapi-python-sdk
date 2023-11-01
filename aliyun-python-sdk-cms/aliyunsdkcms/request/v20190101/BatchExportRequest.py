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
import json

class BatchExportRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Cms', '2019-01-01', 'BatchExport','cms')
		self.set_method('POST')

	def get_Cursor(self): # String
		return self.get_body_params().get('Cursor')

	def set_Cursor(self, Cursor):  # String
		self.add_body_params('Cursor', Cursor)
	def get_Length(self): # Integer
		return self.get_body_params().get('Length')

	def set_Length(self, Length):  # Integer
		self.add_body_params('Length', Length)
	def get_Metric(self): # String
		return self.get_body_params().get('Metric')

	def set_Metric(self, Metric):  # String
		self.add_body_params('Metric', Metric)
	def get_Namespace(self): # String
		return self.get_body_params().get('Namespace')

	def set_Namespace(self, Namespace):  # String
		self.add_body_params('Namespace', Namespace)
	def get_Measurements(self): # Array
		return self.get_body_params().get('Measurements')

	def set_Measurements(self, Measurements):  # Array
		self.add_body_params("Measurements", json.dumps(Measurements))
