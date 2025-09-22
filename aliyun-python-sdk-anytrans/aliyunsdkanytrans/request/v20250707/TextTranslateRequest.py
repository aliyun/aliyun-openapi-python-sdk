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
import json

class TextTranslateRequest(RoaRequest):

	def __init__(self):
		RoaRequest.__init__(self, 'AnyTrans', '2025-07-07', 'TextTranslate')
		self.set_protocol_type('https')
		self.set_uri_pattern('/anytrans/translate/text')
		self.set_method('POST')

	def get_ext(self): # Struct
		return self.get_body_params().get('ext')

	def set_ext(self, ext):  # Struct
		self.add_body_params("ext", json.dumps(ext))
	def get_sourceLanguage(self): # String
		return self.get_body_params().get('sourceLanguage')

	def set_sourceLanguage(self, sourceLanguage):  # String
		self.add_body_params('sourceLanguage', sourceLanguage)
	def get_format(self): # String
		return self.get_body_params().get('format')

	def set_format(self, format):  # String
		self.add_body_params('format', format)
	def get_scene(self): # String
		return self.get_body_params().get('scene')

	def set_scene(self, scene):  # String
		self.add_body_params('scene', scene)
	def get_targetLanguage(self): # String
		return self.get_body_params().get('targetLanguage')

	def set_targetLanguage(self, targetLanguage):  # String
		self.add_body_params('targetLanguage', targetLanguage)
	def get_text(self): # String
		return self.get_body_params().get('text')

	def set_text(self, text):  # String
		self.add_body_params('text', text)
	def get_workspaceId(self): # String
		return self.get_body_params().get('workspaceId')

	def set_workspaceId(self, workspaceId):  # String
		self.add_body_params('workspaceId', workspaceId)
