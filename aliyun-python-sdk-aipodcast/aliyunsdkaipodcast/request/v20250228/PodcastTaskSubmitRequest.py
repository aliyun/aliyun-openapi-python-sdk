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

class PodcastTaskSubmitRequest(RoaRequest):

	def __init__(self):
		RoaRequest.__init__(self, 'AIPodcast', '2025-02-28', 'PodcastTaskSubmit')
		self.set_protocol_type('https')
		self.set_uri_pattern('/podcast/task/submit')
		self.set_method('POST')

	def get_counts(self): # Integer
		return self.get_body_params().get('counts')

	def set_counts(self, counts):  # Integer
		self.add_body_params('counts', counts)
	def get_fileUrls(self): # Array
		return self.get_body_params().get('fileUrls')

	def set_fileUrls(self, fileUrls):  # Array
		self.add_body_params("fileUrls", json.dumps(fileUrls))
	def get_text(self): # String
		return self.get_body_params().get('text')

	def set_text(self, text):  # String
		self.add_body_params('text', text)
	def get_voices(self): # Array
		return self.get_body_params().get('voices')

	def set_voices(self, voices):  # Array
		self.add_body_params("voices", json.dumps(voices))
	def get_topic(self): # String
		return self.get_body_params().get('topic')

	def set_topic(self, topic):  # String
		self.add_body_params('topic', topic)
	def get_workspaceId(self): # String
		return self.get_body_params().get('workspaceId')

	def set_workspaceId(self, workspaceId):  # String
		self.add_body_params('workspaceId', workspaceId)
