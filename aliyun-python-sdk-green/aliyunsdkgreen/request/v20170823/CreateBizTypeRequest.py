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
from aliyunsdkgreen.endpoint import endpoint_data

class CreateBizTypeRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Green', '2017-08-23', 'CreateBizType','green')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_BizTypeImport(self):
		return self.get_query_params().get('BizTypeImport')

	def set_BizTypeImport(self,BizTypeImport):
		self.add_query_param('BizTypeImport',BizTypeImport)

	def get_CiteTemplate(self):
		return self.get_query_params().get('CiteTemplate')

	def set_CiteTemplate(self,CiteTemplate):
		self.add_query_param('CiteTemplate',CiteTemplate)

	def get_IndustryInfo(self):
		return self.get_query_params().get('IndustryInfo')

	def set_IndustryInfo(self,IndustryInfo):
		self.add_query_param('IndustryInfo',IndustryInfo)

	def get_BizTypeName(self):
		return self.get_query_params().get('BizTypeName')

	def set_BizTypeName(self,BizTypeName):
		self.add_query_param('BizTypeName',BizTypeName)