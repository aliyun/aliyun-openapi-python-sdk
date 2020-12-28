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
from aliyunsdknlp_automl.endpoint import endpoint_data

class InvokeActionRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'nlp-automl', '2019-07-01', 'InvokeAction','nlpautoml')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_InvokeProduct(self):
		return self.get_query_params().get('InvokeProduct')

	def set_InvokeProduct(self,InvokeProduct):
		self.add_query_param('InvokeProduct',InvokeProduct)

	def get_InvokeAction(self):
		return self.get_body_params().get('InvokeAction')

	def set_InvokeAction(self,InvokeAction):
		self.add_body_params('InvokeAction', InvokeAction)

	def get_InvokeParams(self):
		return self.get_body_params().get('InvokeParams')

	def set_InvokeParams(self,InvokeParams):
		self.add_body_params('InvokeParams', InvokeParams)

	def get_InvokeRegion(self):
		return self.get_query_params().get('InvokeRegion')

	def set_InvokeRegion(self,InvokeRegion):
		self.add_query_param('InvokeRegion',InvokeRegion)