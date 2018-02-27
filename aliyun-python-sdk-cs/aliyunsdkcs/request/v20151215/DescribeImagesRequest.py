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

from aliyunsdkcore.request import RoaRequest
class DescribeImagesRequest(RoaRequest):

	def __init__(self):
		RoaRequest.__init__(self, 'CS', '2015-12-15', 'DescribeImages')
		self.set_uri_pattern('/images')
		self.set_method('GET')

	def get_ImageName(self):
		return self.get_query_params().get('ImageName')

	def set_ImageName(self,ImageName):
		self.add_query_param('ImageName',ImageName)

	def get_DockerVersion(self):
		return self.get_query_params().get('DockerVersion')

	def set_DockerVersion(self,DockerVersion):
		self.add_query_param('DockerVersion',DockerVersion)