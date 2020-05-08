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


class ReserveDomainRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Domain', '2018-02-08', 'ReserveDomain')

	def get_Channelss(self):
		return self.get_body_params().get('Channelss')

	def set_Channelss(self,Channelss):
		for i in range(len(Channelss)):	
			if Channelss[i] is not None:
				self.add_body_params('Channels.' + str(i + 1) , Channelss[i]);

	def get_DomainName(self):
		return self.get_body_params().get('DomainName')

	def set_DomainName(self,DomainName):
		self.add_body_params('DomainName', DomainName)