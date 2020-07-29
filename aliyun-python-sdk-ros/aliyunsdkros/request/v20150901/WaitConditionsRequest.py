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

from aliyunsdkcore.request import RoaRequest
from aliyunsdkros.endpoint import endpoint_data

class WaitConditionsRequest(RoaRequest):

	def __init__(self):
		RoaRequest.__init__(self, 'ROS', '2015-09-01', 'WaitConditions','ros')
		self.set_uri_pattern('/waitcondition')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_resource(self):
		return self.get_query_params().get('resource')

	def set_resource(self,resource):
		self.add_query_param('resource',resource)

	def get_signature(self):
		return self.get_query_params().get('signature')

	def set_signature(self,signature):
		self.add_query_param('signature',signature)

	def get_stackid(self):
		return self.get_query_params().get('stackid')

	def set_stackid(self,stackid):
		self.add_query_param('stackid',stackid)

	def get_expire(self):
		return self.get_query_params().get('expire')

	def set_expire(self,expire):
		self.add_query_param('expire',expire)

	def get_stackname(self):
		return self.get_query_params().get('stackname')

	def set_stackname(self,stackname):
		self.add_query_param('stackname',stackname)