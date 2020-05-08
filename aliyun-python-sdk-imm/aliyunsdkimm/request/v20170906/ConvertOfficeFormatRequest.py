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

class ConvertOfficeFormatRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'imm', '2017-09-06', 'ConvertOfficeFormat','imm')
		self.set_method('POST')

	def get_SrcType(self):
		return self.get_query_params().get('SrcType')

	def set_SrcType(self,SrcType):
		self.add_query_param('SrcType',SrcType)

	def get_Project(self):
		return self.get_query_params().get('Project')

	def set_Project(self,Project):
		self.add_query_param('Project',Project)

	def get_PdfVector(self):
		return self.get_query_params().get('PdfVector')

	def set_PdfVector(self,PdfVector):
		self.add_query_param('PdfVector',PdfVector)

	def get_Password(self):
		return self.get_query_params().get('Password')

	def set_Password(self,Password):
		self.add_query_param('Password',Password)

	def get_StartPage(self):
		return self.get_query_params().get('StartPage')

	def set_StartPage(self,StartPage):
		self.add_query_param('StartPage',StartPage)

	def get_FitToPagesWide(self):
		return self.get_query_params().get('FitToPagesWide')

	def set_FitToPagesWide(self,FitToPagesWide):
		self.add_query_param('FitToPagesWide',FitToPagesWide)

	def get_TgtFilePrefix(self):
		return self.get_query_params().get('TgtFilePrefix')

	def set_TgtFilePrefix(self,TgtFilePrefix):
		self.add_query_param('TgtFilePrefix',TgtFilePrefix)

	def get_ModelId(self):
		return self.get_query_params().get('ModelId')

	def set_ModelId(self,ModelId):
		self.add_query_param('ModelId',ModelId)

	def get_MaxSheetRow(self):
		return self.get_query_params().get('MaxSheetRow')

	def set_MaxSheetRow(self,MaxSheetRow):
		self.add_query_param('MaxSheetRow',MaxSheetRow)

	def get_MaxSheetCount(self):
		return self.get_query_params().get('MaxSheetCount')

	def set_MaxSheetCount(self,MaxSheetCount):
		self.add_query_param('MaxSheetCount',MaxSheetCount)

	def get_EndPage(self):
		return self.get_query_params().get('EndPage')

	def set_EndPage(self,EndPage):
		self.add_query_param('EndPage',EndPage)

	def get_TgtFileSuffix(self):
		return self.get_query_params().get('TgtFileSuffix')

	def set_TgtFileSuffix(self,TgtFileSuffix):
		self.add_query_param('TgtFileSuffix',TgtFileSuffix)

	def get_SheetOnePage(self):
		return self.get_query_params().get('SheetOnePage')

	def set_SheetOnePage(self,SheetOnePage):
		self.add_query_param('SheetOnePage',SheetOnePage)

	def get_MaxSheetCol(self):
		return self.get_query_params().get('MaxSheetCol')

	def set_MaxSheetCol(self,MaxSheetCol):
		self.add_query_param('MaxSheetCol',MaxSheetCol)

	def get_TgtType(self):
		return self.get_query_params().get('TgtType')

	def set_TgtType(self,TgtType):
		self.add_query_param('TgtType',TgtType)

	def get_Hidecomments(self):
		return self.get_query_params().get('Hidecomments')

	def set_Hidecomments(self,Hidecomments):
		self.add_query_param('Hidecomments',Hidecomments)

	def get_FitToPagesTall(self):
		return self.get_query_params().get('FitToPagesTall')

	def set_FitToPagesTall(self,FitToPagesTall):
		self.add_query_param('FitToPagesTall',FitToPagesTall)

	def get_SrcUri(self):
		return self.get_query_params().get('SrcUri')

	def set_SrcUri(self,SrcUri):
		self.add_query_param('SrcUri',SrcUri)

	def get_TgtFilePages(self):
		return self.get_query_params().get('TgtFilePages')

	def set_TgtFilePages(self,TgtFilePages):
		self.add_query_param('TgtFilePages',TgtFilePages)

	def get_TgtUri(self):
		return self.get_query_params().get('TgtUri')

	def set_TgtUri(self,TgtUri):
		self.add_query_param('TgtUri',TgtUri)