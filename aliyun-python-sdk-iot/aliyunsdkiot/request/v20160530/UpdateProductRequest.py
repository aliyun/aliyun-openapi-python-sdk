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
class UpdateProductRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Iot', '2016-05-30', 'UpdateProduct')

	def get_ProductName(self):
		return self.get_query_params().get('ProductName')

	def set_ProductName(self,ProductName):
		self.add_query_param('ProductName',ProductName)

	def get_ProductDesc(self):
		return self.get_query_params().get('ProductDesc')

	def set_ProductDesc(self,ProductDesc):
		self.add_query_param('ProductDesc',ProductDesc)

	def get_ExtProps(self):
		return self.get_query_params().get('ExtProps')

	def set_ExtProps(self,ExtProps):
		self.add_query_param('ExtProps',ExtProps)

	def get_CatId(self):
		return self.get_query_params().get('CatId')

	def set_CatId(self,CatId):
		self.add_query_param('CatId',CatId)

	def get_ProductKey(self):
		return self.get_query_params().get('ProductKey')

	def set_ProductKey(self,ProductKey):
		self.add_query_param('ProductKey',ProductKey)