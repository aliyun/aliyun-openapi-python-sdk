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
class StopMixStreamsServiceRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Cdn', '2014-11-11', 'StopMixStreamsService')

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_SecurityToken(self):
		return self.get_query_params().get('SecurityToken')

	def set_SecurityToken(self,SecurityToken):
		self.add_query_param('SecurityToken',SecurityToken)

	def get_MainDomainName(self):
		return self.get_query_params().get('MainDomainName')

	def set_MainDomainName(self,MainDomainName):
		self.add_query_param('MainDomainName',MainDomainName)

	def get_MainAppName(self):
		return self.get_query_params().get('MainAppName')

	def set_MainAppName(self,MainAppName):
		self.add_query_param('MainAppName',MainAppName)

	def get_MainStreamName(self):
		return self.get_query_params().get('MainStreamName')

	def set_MainStreamName(self,MainStreamName):
		self.add_query_param('MainStreamName',MainStreamName)

	def get_MixDomainName(self):
		return self.get_query_params().get('MixDomainName')

	def set_MixDomainName(self,MixDomainName):
		self.add_query_param('MixDomainName',MixDomainName)

	def get_MixAppName(self):
		return self.get_query_params().get('MixAppName')

	def set_MixAppName(self,MixAppName):
		self.add_query_param('MixAppName',MixAppName)

	def get_MixStreamName(self):
		return self.get_query_params().get('MixStreamName')

	def set_MixStreamName(self,MixStreamName):
		self.add_query_param('MixStreamName',MixStreamName)