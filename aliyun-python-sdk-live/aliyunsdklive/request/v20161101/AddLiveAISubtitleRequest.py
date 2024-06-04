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
from aliyunsdklive.endpoint import endpoint_data
import json

class AddLiveAISubtitleRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'live', '2016-11-01', 'AddLiveAISubtitle','live')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_SrcLanguage(self): # String
		return self.get_query_params().get('SrcLanguage')

	def set_SrcLanguage(self, SrcLanguage):  # String
		self.add_query_param('SrcLanguage', SrcLanguage)
	def get_Description(self): # String
		return self.get_query_params().get('Description')

	def set_Description(self, Description):  # String
		self.add_query_param('Description', Description)
	def get_FontName(self): # String
		return self.get_query_params().get('FontName')

	def set_FontName(self, FontName):  # String
		self.add_query_param('FontName', FontName)
	def get_SubtitleName(self): # String
		return self.get_query_params().get('SubtitleName')

	def set_SubtitleName(self, SubtitleName):  # String
		self.add_query_param('SubtitleName', SubtitleName)
	def get_FontSizeNormalized(self): # Float
		return self.get_query_params().get('FontSizeNormalized')

	def set_FontSizeNormalized(self, FontSizeNormalized):  # Float
		self.add_query_param('FontSizeNormalized', FontSizeNormalized)
	def get_FontColor(self): # String
		return self.get_query_params().get('FontColor')

	def set_FontColor(self, FontColor):  # String
		self.add_query_param('FontColor', FontColor)
	def get_ShowSourceLan(self): # Boolean
		return self.get_query_params().get('ShowSourceLan')

	def set_ShowSourceLan(self, ShowSourceLan):  # Boolean
		self.add_query_param('ShowSourceLan', ShowSourceLan)
	def get_PositionNormalized(self): # Array
		return self.get_query_params().get('PositionNormalized')

	def set_PositionNormalized(self, PositionNormalized):  # Array
		self.add_query_param("PositionNormalized", json.dumps(PositionNormalized))
	def get_BorderWidthNormalized(self): # Float
		return self.get_query_params().get('BorderWidthNormalized')

	def set_BorderWidthNormalized(self, BorderWidthNormalized):  # Float
		self.add_query_param('BorderWidthNormalized', BorderWidthNormalized)
	def get_MaxLines(self): # Integer
		return self.get_query_params().get('MaxLines')

	def set_MaxLines(self, MaxLines):  # Integer
		self.add_query_param('MaxLines', MaxLines)
	def get_Height(self): # String
		return self.get_query_params().get('Height')

	def set_Height(self, Height):  # String
		self.add_query_param('Height', Height)
	def get_WordPerLine(self): # Integer
		return self.get_query_params().get('WordPerLine')

	def set_WordPerLine(self, WordPerLine):  # Integer
		self.add_query_param('WordPerLine', WordPerLine)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_BgWidthNormalized(self): # Float
		return self.get_query_params().get('BgWidthNormalized')

	def set_BgWidthNormalized(self, BgWidthNormalized):  # Float
		self.add_query_param('BgWidthNormalized', BgWidthNormalized)
	def get_BgColor(self): # String
		return self.get_query_params().get('BgColor')

	def set_BgColor(self, BgColor):  # String
		self.add_query_param('BgColor', BgColor)
	def get_DstLanguage(self): # String
		return self.get_query_params().get('DstLanguage')

	def set_DstLanguage(self, DstLanguage):  # String
		self.add_query_param('DstLanguage', DstLanguage)
	def get_Width(self): # String
		return self.get_query_params().get('Width')

	def set_Width(self, Width):  # String
		self.add_query_param('Width', Width)
	def get_CopyFrom(self): # String
		return self.get_query_params().get('CopyFrom')

	def set_CopyFrom(self, CopyFrom):  # String
		self.add_query_param('CopyFrom', CopyFrom)
