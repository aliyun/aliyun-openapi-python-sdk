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

class VerifyIntelligentCaptchaRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'captcha', '2023-03-05', 'VerifyIntelligentCaptcha')
		self.set_method('POST')

	def get_CaptchaVerifyParam(self): # String
		return self.get_body_params().get('CaptchaVerifyParam')

	def set_CaptchaVerifyParam(self, CaptchaVerifyParam):  # String
		self.add_body_params('CaptchaVerifyParam', CaptchaVerifyParam)
	def get_SceneId(self): # String
		return self.get_body_params().get('SceneId')

	def set_SceneId(self, SceneId):  # String
		self.add_body_params('SceneId', SceneId)
