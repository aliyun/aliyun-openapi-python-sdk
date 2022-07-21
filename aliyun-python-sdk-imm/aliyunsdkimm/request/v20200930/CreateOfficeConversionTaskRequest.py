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
from aliyunsdkimm.endpoint import endpoint_data
import json

class CreateOfficeConversionTaskRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'imm', '2020-09-30', 'CreateOfficeConversionTask','imm')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_SheetCount(self): # Long
		return self.get_query_params().get('SheetCount')

	def set_SheetCount(self, SheetCount):  # Long
		self.add_query_param('SheetCount', SheetCount)
	def get_LongText(self): # Boolean
		return self.get_query_params().get('LongText')

	def set_LongText(self, LongText):  # Boolean
		self.add_query_param('LongText', LongText)
	def get_TargetType(self): # String
		return self.get_query_params().get('TargetType')

	def set_TargetType(self, TargetType):  # String
		self.add_query_param('TargetType', TargetType)
	def get_ShowComments(self): # Boolean
		return self.get_query_params().get('ShowComments')

	def set_ShowComments(self, ShowComments):  # Boolean
		self.add_query_param('ShowComments', ShowComments)
	def get_TrimPolicy(self): # Struct
		return self.get_query_params().get('TrimPolicy')

	def set_TrimPolicy(self, TrimPolicy):  # Struct
		self.add_query_param("TrimPolicy", json.dumps(TrimPolicy))
	def get_MaxSheetColumn(self): # Long
		return self.get_query_params().get('MaxSheetColumn')

	def set_MaxSheetColumn(self, MaxSheetColumn):  # Long
		self.add_query_param('MaxSheetColumn', MaxSheetColumn)
	def get_FirstPage(self): # Boolean
		return self.get_query_params().get('FirstPage')

	def set_FirstPage(self, FirstPage):  # Boolean
		self.add_query_param('FirstPage', FirstPage)
	def get_PaperHorizontal(self): # Boolean
		return self.get_query_params().get('PaperHorizontal')

	def set_PaperHorizontal(self, PaperHorizontal):  # Boolean
		self.add_query_param('PaperHorizontal', PaperHorizontal)
	def get_UserData(self): # String
		return self.get_query_params().get('UserData')

	def set_UserData(self, UserData):  # String
		self.add_query_param('UserData', UserData)
	def get_ScalePercentage(self): # Long
		return self.get_query_params().get('ScalePercentage')

	def set_ScalePercentage(self, ScalePercentage):  # Long
		self.add_query_param('ScalePercentage', ScalePercentage)
	def get_Password(self): # String
		return self.get_query_params().get('Password')

	def set_Password(self, Password):  # String
		self.add_query_param('Password', Password)
	def get_StartPage(self): # Long
		return self.get_query_params().get('StartPage')

	def set_StartPage(self, StartPage):  # Long
		self.add_query_param('StartPage', StartPage)
	def get_Pages(self): # String
		return self.get_query_params().get('Pages')

	def set_Pages(self, Pages):  # String
		self.add_query_param('Pages', Pages)
	def get_TargetURIPrefix(self): # String
		return self.get_query_params().get('TargetURIPrefix')

	def set_TargetURIPrefix(self, TargetURIPrefix):  # String
		self.add_query_param('TargetURIPrefix', TargetURIPrefix)
	def get_NotifyEndpoint(self): # String
		return self.get_query_params().get('NotifyEndpoint')

	def set_NotifyEndpoint(self, NotifyEndpoint):  # String
		self.add_query_param('NotifyEndpoint', NotifyEndpoint)
	def get_TargetURI(self): # String
		return self.get_query_params().get('TargetURI')

	def set_TargetURI(self, TargetURI):  # String
		self.add_query_param('TargetURI', TargetURI)
	def get_SourceType(self): # String
		return self.get_query_params().get('SourceType')

	def set_SourceType(self, SourceType):  # String
		self.add_query_param('SourceType', SourceType)
	def get_PaperSize(self): # String
		return self.get_query_params().get('PaperSize')

	def set_PaperSize(self, PaperSize):  # String
		self.add_query_param('PaperSize', PaperSize)
	def get_ImageDPI(self): # Long
		return self.get_query_params().get('ImageDPI')

	def set_ImageDPI(self, ImageDPI):  # Long
		self.add_query_param('ImageDPI', ImageDPI)
	def get_ProjectName(self): # String
		return self.get_query_params().get('ProjectName')

	def set_ProjectName(self, ProjectName):  # String
		self.add_query_param('ProjectName', ProjectName)
	def get_NotifyTopicName(self): # String
		return self.get_query_params().get('NotifyTopicName')

	def set_NotifyTopicName(self, NotifyTopicName):  # String
		self.add_query_param('NotifyTopicName', NotifyTopicName)
	def get_FitToHeight(self): # Boolean
		return self.get_query_params().get('FitToHeight')

	def set_FitToHeight(self, FitToHeight):  # Boolean
		self.add_query_param('FitToHeight', FitToHeight)
	def get_LongPicture(self): # Boolean
		return self.get_query_params().get('LongPicture')

	def set_LongPicture(self, LongPicture):  # Boolean
		self.add_query_param('LongPicture', LongPicture)
	def get_MaxSheetRow(self): # Long
		return self.get_query_params().get('MaxSheetRow')

	def set_MaxSheetRow(self, MaxSheetRow):  # Long
		self.add_query_param('MaxSheetRow', MaxSheetRow)
	def get_EndPage(self): # Long
		return self.get_query_params().get('EndPage')

	def set_EndPage(self, EndPage):  # Long
		self.add_query_param('EndPage', EndPage)
	def get_CredentialConfig(self): # Struct
		return self.get_query_params().get('CredentialConfig')

	def set_CredentialConfig(self, CredentialConfig):  # Struct
		self.add_query_param("CredentialConfig", json.dumps(CredentialConfig))
	def get_FitToWidth(self): # Boolean
		return self.get_query_params().get('FitToWidth')

	def set_FitToWidth(self, FitToWidth):  # Boolean
		self.add_query_param('FitToWidth', FitToWidth)
	def get_Quality(self): # Long
		return self.get_query_params().get('Quality')

	def set_Quality(self, Quality):  # Long
		self.add_query_param('Quality', Quality)
	def get_Tags(self): # Map
		return self.get_query_params().get('Tags')

	def set_Tags(self, Tags):  # Map
		self.add_query_param("Tags", json.dumps(Tags))
	def get_SourceURI(self): # String
		return self.get_query_params().get('SourceURI')

	def set_SourceURI(self, SourceURI):  # String
		self.add_query_param('SourceURI', SourceURI)
	def get_SheetIndex(self): # Long
		return self.get_query_params().get('SheetIndex')

	def set_SheetIndex(self, SheetIndex):  # Long
		self.add_query_param('SheetIndex', SheetIndex)
	def get_HoldLineFeed(self): # Boolean
		return self.get_query_params().get('HoldLineFeed')

	def set_HoldLineFeed(self, HoldLineFeed):  # Boolean
		self.add_query_param('HoldLineFeed', HoldLineFeed)
