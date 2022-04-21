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
from aliyunsdkvoicenavigator.endpoint import endpoint_data

class ModifyAsrConfigRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'VoiceNavigator', '2018-06-12', 'ModifyAsrConfig','voicebot')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_AsrVocabularyId(self): # String
		return self.get_query_params().get('AsrVocabularyId')

	def set_AsrVocabularyId(self, AsrVocabularyId):  # String
		self.add_query_param('AsrVocabularyId', AsrVocabularyId)
	def get_AsrClassVocabularyId(self): # String
		return self.get_query_params().get('AsrClassVocabularyId')

	def set_AsrClassVocabularyId(self, AsrClassVocabularyId):  # String
		self.add_query_param('AsrClassVocabularyId', AsrClassVocabularyId)
	def get_EntryId(self): # String
		return self.get_query_params().get('EntryId')

	def set_EntryId(self, EntryId):  # String
		self.add_query_param('EntryId', EntryId)
	def get_AsrCustomizationId(self): # String
		return self.get_query_params().get('AsrCustomizationId')

	def set_AsrCustomizationId(self, AsrCustomizationId):  # String
		self.add_query_param('AsrCustomizationId', AsrCustomizationId)
	def get_ConfigLevel(self): # Integer
		return self.get_query_params().get('ConfigLevel')

	def set_ConfigLevel(self, ConfigLevel):  # Integer
		self.add_query_param('ConfigLevel', ConfigLevel)
	def get_AsrAcousticModelId(self): # String
		return self.get_query_params().get('AsrAcousticModelId')

	def set_AsrAcousticModelId(self, AsrAcousticModelId):  # String
		self.add_query_param('AsrAcousticModelId', AsrAcousticModelId)
