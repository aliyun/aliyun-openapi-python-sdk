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

class ConvertOfficeFormatRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'imm', '2017-09-06', 'ConvertOfficeFormat','imm')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_SrcType(self): # String
		return self.get_query_params().get('SrcType')

	def set_SrcType(self, SrcType):  # String
		self.add_query_param('SrcType', SrcType)
	def get_Project(self): # String
		return self.get_query_params().get('Project')

	def set_Project(self, Project):  # String
		self.add_query_param('Project', Project)
	def get_PdfVector(self): # Boolean
		return self.get_query_params().get('PdfVector')

	def set_PdfVector(self, PdfVector):  # Boolean
		self.add_query_param('PdfVector', PdfVector)
	def get_Password(self): # String
		return self.get_query_params().get('Password')

	def set_Password(self, Password):  # String
		self.add_query_param('Password', Password)
	def get_StartPage(self): # Long
		return self.get_query_params().get('StartPage')

	def set_StartPage(self, StartPage):  # Long
		self.add_query_param('StartPage', StartPage)
	def get_FitToPagesWide(self): # Boolean
		return self.get_query_params().get('FitToPagesWide')

	def set_FitToPagesWide(self, FitToPagesWide):  # Boolean
		self.add_query_param('FitToPagesWide', FitToPagesWide)
	def get_TgtFilePrefix(self): # String
		return self.get_query_params().get('TgtFilePrefix')

	def set_TgtFilePrefix(self, TgtFilePrefix):  # String
		self.add_query_param('TgtFilePrefix', TgtFilePrefix)
	def get_ModelId(self): # String
		return self.get_query_params().get('ModelId')

	def set_ModelId(self, ModelId):  # String
		self.add_query_param('ModelId', ModelId)
	def get_MaxSheetRow(self): # Long
		return self.get_query_params().get('MaxSheetRow')

	def set_MaxSheetRow(self, MaxSheetRow):  # Long
		self.add_query_param('MaxSheetRow', MaxSheetRow)
	def get_MaxSheetCount(self): # Long
		return self.get_query_params().get('MaxSheetCount')

	def set_MaxSheetCount(self, MaxSheetCount):  # Long
		self.add_query_param('MaxSheetCount', MaxSheetCount)
	def get_EndPage(self): # Long
		return self.get_query_params().get('EndPage')

	def set_EndPage(self, EndPage):  # Long
		self.add_query_param('EndPage', EndPage)
	def get_TgtFileSuffix(self): # String
		return self.get_query_params().get('TgtFileSuffix')

	def set_TgtFileSuffix(self, TgtFileSuffix):  # String
		self.add_query_param('TgtFileSuffix', TgtFileSuffix)
	def get_SheetOnePage(self): # Boolean
		return self.get_query_params().get('SheetOnePage')

	def set_SheetOnePage(self, SheetOnePage):  # Boolean
		self.add_query_param('SheetOnePage', SheetOnePage)
	def get_MaxSheetCol(self): # Long
		return self.get_query_params().get('MaxSheetCol')

	def set_MaxSheetCol(self, MaxSheetCol):  # Long
		self.add_query_param('MaxSheetCol', MaxSheetCol)
	def get_TgtType(self): # String
		return self.get_query_params().get('TgtType')

	def set_TgtType(self, TgtType):  # String
		self.add_query_param('TgtType', TgtType)
	def get_Hidecomments(self): # Boolean
		return self.get_query_params().get('Hidecomments')

	def set_Hidecomments(self, Hidecomments):  # Boolean
		self.add_query_param('Hidecomments', Hidecomments)
	def get_FitToPagesTall(self): # Boolean
		return self.get_query_params().get('FitToPagesTall')

	def set_FitToPagesTall(self, FitToPagesTall):  # Boolean
		self.add_query_param('FitToPagesTall', FitToPagesTall)
	def get_SrcUri(self): # String
		return self.get_query_params().get('SrcUri')

	def set_SrcUri(self, SrcUri):  # String
		self.add_query_param('SrcUri', SrcUri)
	def get_TgtFilePages(self): # String
		return self.get_query_params().get('TgtFilePages')

	def set_TgtFilePages(self, TgtFilePages):  # String
		self.add_query_param('TgtFilePages', TgtFilePages)
	def get_TgtUri(self): # String
		return self.get_query_params().get('TgtUri')

	def set_TgtUri(self, TgtUri):  # String
		self.add_query_param('TgtUri', TgtUri)
