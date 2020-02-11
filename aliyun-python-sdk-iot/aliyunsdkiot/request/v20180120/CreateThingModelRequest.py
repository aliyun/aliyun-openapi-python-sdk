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
from aliyunsdkiot.endpoint import endpoint_data

class CreateThingModelRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Iot', '2018-01-20', 'CreateThingModel','iot')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ProductKey(self):
		return self.get_query_params().get('ProductKey')

	def set_ProductKey(self,ProductKey):
		self.add_query_param('ProductKey',ProductKey)

	def get_ApiProduct(self):
		return self.get_body_params().get('ApiProduct')

	def set_ApiProduct(self,ApiProduct):
		self.add_body_params('ApiProduct', ApiProduct)

	def get_ThingModelJson(self):
		return self.get_query_params().get('ThingModelJson')

	def set_ThingModelJson(self,ThingModelJson):
		self.add_query_param('ThingModelJson',ThingModelJson)

	def get_ApiRevision(self):
		return self.get_body_params().get('ApiRevision')

	def set_ApiRevision(self,ApiRevision):
		self.add_body_params('ApiRevision', ApiRevision)