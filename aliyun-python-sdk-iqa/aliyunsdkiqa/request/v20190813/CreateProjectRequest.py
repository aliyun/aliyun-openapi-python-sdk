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

class CreateProjectRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'iqa', '2019-08-13', 'CreateProject','iqa')

	def get_ProjectName(self):
		return self.get_body_params().get('ProjectName')

	def set_ProjectName(self,ProjectName):
		self.add_body_params('ProjectName', ProjectName)

	def get_ModelId(self):
		return self.get_body_params().get('ModelId')

	def set_ModelId(self,ModelId):
		self.add_body_params('ModelId', ModelId)

	def get_ProjectType(self):
		return self.get_body_params().get('ProjectType')

	def set_ProjectType(self,ProjectType):
		self.add_body_params('ProjectType', ProjectType)