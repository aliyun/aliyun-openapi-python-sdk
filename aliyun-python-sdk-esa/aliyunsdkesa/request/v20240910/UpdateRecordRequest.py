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

class UpdateRecordRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'ESA', '2024-09-10', 'UpdateRecord')
		self.set_protocol_type('https')
		self.set_method('POST')

	def get_RecordId(self): # Long
		return self.get_query_params().get('RecordId')

	def set_RecordId(self, RecordId):  # Long
		self.add_query_param('RecordId', RecordId)
	def get_HostPolicy(self): # String
		return self.get_query_params().get('HostPolicy')

	def set_HostPolicy(self, HostPolicy):  # String
		self.add_query_param('HostPolicy', HostPolicy)
	def get_Data(self): # String
		return self.get_query_params().get('Data')

	def set_Data(self, Data):  # String
		self.add_query_param('Data', Data)
	def get_BizName(self): # String
		return self.get_query_params().get('BizName')

	def set_BizName(self, BizName):  # String
		self.add_query_param('BizName', BizName)
	def get_AuthConf(self): # Struct
		return self.get_query_params().get('AuthConf')

	def set_AuthConf(self, AuthConf):  # Struct
		self.add_query_param("AuthConf", json.dumps(AuthConf))
	def get_SourceType(self): # String
		return self.get_query_params().get('SourceType')

	def set_SourceType(self, SourceType):  # String
		self.add_query_param('SourceType', SourceType)
	def get_Comment(self): # String
		return self.get_query_params().get('Comment')

	def set_Comment(self, Comment):  # String
		self.add_query_param('Comment', Comment)
	def get_Proxied(self): # Boolean
		return self.get_query_params().get('Proxied')

	def set_Proxied(self, Proxied):  # Boolean
		self.add_query_param('Proxied', Proxied)
	def get_Ttl(self): # Integer
		return self.get_query_params().get('Ttl')

	def set_Ttl(self, Ttl):  # Integer
		self.add_query_param('Ttl', Ttl)
