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
class SignResultNotifyRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'finmall', '2018-07-23', 'SignResultNotify','finmall')
		self.set_method('POST')

	def get_DocId(self):
		return self.get_query_params().get('DocId')

	def set_DocId(self,DocId):
		self.add_query_param('DocId',DocId)

	def get_DocContent(self):
		return self.get_body_params().get('DocContent')

	def set_DocContent(self,DocContent):
		self.add_body_params('DocContent', DocContent)

	def get_Sign(self):
		return self.get_query_params().get('Sign')

	def set_Sign(self,Sign):
		self.add_query_param('Sign',Sign)

	def get_ResultCode(self):
		return self.get_query_params().get('ResultCode')

	def set_ResultCode(self,ResultCode):
		self.add_query_param('ResultCode',ResultCode)

	def get_Time(self):
		return self.get_query_params().get('Time')

	def set_Time(self,Time):
		self.add_query_param('Time',Time)

	def get_TransactionId(self):
		return self.get_query_params().get('TransactionId')

	def set_TransactionId(self,TransactionId):
		self.add_query_param('TransactionId',TransactionId)

	def get_ResultDesc(self):
		return self.get_query_params().get('ResultDesc')

	def set_ResultDesc(self,ResultDesc):
		self.add_query_param('ResultDesc',ResultDesc)