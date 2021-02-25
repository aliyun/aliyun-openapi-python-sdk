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

class QueryIndustryDeviceDataRequest(RoaRequest):

	def __init__(self):
		RoaRequest.__init__(self, 'et-industry-openapi', '2020-08-24', 'QueryIndustryDeviceData')
		self.set_uri_pattern('/api/igate/timeseries/query/pop/multifieldlatest')
		self.set_method('POST')

	def get_Request(self):
		return self.get_body_params().get('Request')

	def set_Request(self,Request):
		self.add_body_params('Request', Request)