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

class DeleteSurveyResourcesRequest(RoaRequest):

	def __init__(self):
		RoaRequest.__init__(self, 'apds', '2022-03-31', 'DeleteSurveyResources')
		self.set_uri_pattern('/okss-services/confirm-resource/destroy')
		self.set_method('POST')

	def get_ids(self): # string
		return self.get_query_params().get('ids')

	def set_ids(self, ids):  # string
		self.add_query_param('ids', ids)
