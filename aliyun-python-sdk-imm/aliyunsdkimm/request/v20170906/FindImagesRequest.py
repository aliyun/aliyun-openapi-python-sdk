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

class FindImagesRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'imm', '2017-09-06', 'FindImages','imm')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_RemarksArrayBIn(self): # String
		return self.get_query_params().get('RemarksArrayBIn')

	def set_RemarksArrayBIn(self, RemarksArrayBIn):  # String
		self.add_query_param('RemarksArrayBIn', RemarksArrayBIn)
	def get_Project(self): # String
		return self.get_query_params().get('Project')

	def set_Project(self, Project):  # String
		self.add_query_param('Project', Project)
	def get_ExternalId(self): # String
		return self.get_query_params().get('ExternalId')

	def set_ExternalId(self, ExternalId):  # String
		self.add_query_param('ExternalId', ExternalId)
	def get_FacesModifyTimeRange(self): # String
		return self.get_query_params().get('FacesModifyTimeRange')

	def set_FacesModifyTimeRange(self, FacesModifyTimeRange):  # String
		self.add_query_param('FacesModifyTimeRange', FacesModifyTimeRange)
	def get_OCRContentsMatch(self): # String
		return self.get_query_params().get('OCRContentsMatch')

	def set_OCRContentsMatch(self, OCRContentsMatch):  # String
		self.add_query_param('OCRContentsMatch', OCRContentsMatch)
	def get_Limit(self): # Integer
		return self.get_query_params().get('Limit')

	def set_Limit(self, Limit):  # Integer
		self.add_query_param('Limit', Limit)
	def get_RemarksDPrefix(self): # String
		return self.get_query_params().get('RemarksDPrefix')

	def set_RemarksDPrefix(self, RemarksDPrefix):  # String
		self.add_query_param('RemarksDPrefix', RemarksDPrefix)
	def get_SourceType(self): # String
		return self.get_query_params().get('SourceType')

	def set_SourceType(self, SourceType):  # String
		self.add_query_param('SourceType', SourceType)
	def get_Order(self): # String
		return self.get_query_params().get('Order')

	def set_Order(self, Order):  # String
		self.add_query_param('Order', Order)
	def get_GroupId(self): # String
		return self.get_query_params().get('GroupId')

	def set_GroupId(self, GroupId):  # String
		self.add_query_param('GroupId', GroupId)
	def get_OrderBy(self): # String
		return self.get_query_params().get('OrderBy')

	def set_OrderBy(self, OrderBy):  # String
		self.add_query_param('OrderBy', OrderBy)
	def get_TagNames(self): # String
		return self.get_query_params().get('TagNames')

	def set_TagNames(self, TagNames):  # String
		self.add_query_param('TagNames', TagNames)
	def get_Marker(self): # String
		return self.get_query_params().get('Marker')

	def set_Marker(self, Marker):  # String
		self.add_query_param('Marker', Marker)
	def get_RemarksCPrefix(self): # String
		return self.get_query_params().get('RemarksCPrefix')

	def set_RemarksCPrefix(self, RemarksCPrefix):  # String
		self.add_query_param('RemarksCPrefix', RemarksCPrefix)
	def get_ModifyTimeRange(self): # String
		return self.get_query_params().get('ModifyTimeRange')

	def set_ModifyTimeRange(self, ModifyTimeRange):  # String
		self.add_query_param('ModifyTimeRange', ModifyTimeRange)
	def get_AddressLineContentsMatch(self): # String
		return self.get_query_params().get('AddressLineContentsMatch')

	def set_AddressLineContentsMatch(self, AddressLineContentsMatch):  # String
		self.add_query_param('AddressLineContentsMatch', AddressLineContentsMatch)
	def get_Gender(self): # String
		return self.get_query_params().get('Gender')

	def set_Gender(self, Gender):  # String
		self.add_query_param('Gender', Gender)
	def get_RemarksArrayAIn(self): # String
		return self.get_query_params().get('RemarksArrayAIn')

	def set_RemarksArrayAIn(self, RemarksArrayAIn):  # String
		self.add_query_param('RemarksArrayAIn', RemarksArrayAIn)
	def get_ImageSizeRange(self): # String
		return self.get_query_params().get('ImageSizeRange')

	def set_ImageSizeRange(self, ImageSizeRange):  # String
		self.add_query_param('ImageSizeRange', ImageSizeRange)
	def get_RemarksBPrefix(self): # String
		return self.get_query_params().get('RemarksBPrefix')

	def set_RemarksBPrefix(self, RemarksBPrefix):  # String
		self.add_query_param('RemarksBPrefix', RemarksBPrefix)
	def get_LocationBoundary(self): # String
		return self.get_query_params().get('LocationBoundary')

	def set_LocationBoundary(self, LocationBoundary):  # String
		self.add_query_param('LocationBoundary', LocationBoundary)
	def get_ImageTimeRange(self): # String
		return self.get_query_params().get('ImageTimeRange')

	def set_ImageTimeRange(self, ImageTimeRange):  # String
		self.add_query_param('ImageTimeRange', ImageTimeRange)
	def get_TagsModifyTimeRange(self): # String
		return self.get_query_params().get('TagsModifyTimeRange')

	def set_TagsModifyTimeRange(self, TagsModifyTimeRange):  # String
		self.add_query_param('TagsModifyTimeRange', TagsModifyTimeRange)
	def get_AgeRange(self): # String
		return self.get_query_params().get('AgeRange')

	def set_AgeRange(self, AgeRange):  # String
		self.add_query_param('AgeRange', AgeRange)
	def get_RemarksAPrefix(self): # String
		return self.get_query_params().get('RemarksAPrefix')

	def set_RemarksAPrefix(self, RemarksAPrefix):  # String
		self.add_query_param('RemarksAPrefix', RemarksAPrefix)
	def get_SourceUriPrefix(self): # String
		return self.get_query_params().get('SourceUriPrefix')

	def set_SourceUriPrefix(self, SourceUriPrefix):  # String
		self.add_query_param('SourceUriPrefix', SourceUriPrefix)
	def get_Emotion(self): # String
		return self.get_query_params().get('Emotion')

	def set_Emotion(self, Emotion):  # String
		self.add_query_param('Emotion', Emotion)
	def get_CreateTimeRange(self): # String
		return self.get_query_params().get('CreateTimeRange')

	def set_CreateTimeRange(self, CreateTimeRange):  # String
		self.add_query_param('CreateTimeRange', CreateTimeRange)
	def get_SetId(self): # String
		return self.get_query_params().get('SetId')

	def set_SetId(self, SetId):  # String
		self.add_query_param('SetId', SetId)
