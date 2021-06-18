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
from aliyunsdksas.endpoint import endpoint_data

class CreateAssetRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Sas', '2018-12-03', 'CreateAsset','sas')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_InternetIp(self):
		return self.get_query_params().get('InternetIp')

	def set_InternetIp(self,InternetIp):
		self.add_query_param('InternetIp',InternetIp)

	def get_OsName(self):
		return self.get_query_params().get('OsName')

	def set_OsName(self,OsName):
		self.add_query_param('OsName',OsName)

	def get_Os(self):
		return self.get_query_params().get('Os')

	def set_Os(self,Os):
		self.add_query_param('Os',Os)

	def get_InstanceName(self):
		return self.get_query_params().get('InstanceName')

	def set_InstanceName(self,InstanceName):
		self.add_query_param('InstanceName',InstanceName)

	def get_IntranetIp(self):
		return self.get_query_params().get('IntranetIp')

	def set_IntranetIp(self,IntranetIp):
		self.add_query_param('IntranetIp',IntranetIp)

	def get_Status(self):
		return self.get_query_params().get('Status')

	def set_Status(self,Status):
		self.add_query_param('Status',Status)