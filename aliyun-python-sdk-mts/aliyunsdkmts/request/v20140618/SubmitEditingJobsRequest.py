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
from aliyunsdkmts.endpoint import endpoint_data

class SubmitEditingJobsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Mts', '2014-06-18', 'SubmitEditingJobs','mts')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ResourceOwnerId(self): # Long
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self, ResourceOwnerId):  # Long
		self.add_query_param('ResourceOwnerId', ResourceOwnerId)
	def get_OutputLocation(self): # String
		return self.get_query_params().get('OutputLocation')

	def set_OutputLocation(self, OutputLocation):  # String
		self.add_query_param('OutputLocation', OutputLocation)
	def get_EditingInputs(self): # String
		return self.get_query_params().get('EditingInputs')

	def set_EditingInputs(self, EditingInputs):  # String
		self.add_query_param('EditingInputs', EditingInputs)
	def get_EditingJobURL(self): # String
		return self.get_query_params().get('EditingJobURL')

	def set_EditingJobURL(self, EditingJobURL):  # String
		self.add_query_param('EditingJobURL', EditingJobURL)
	def get_EditingJobOssFileUid(self): # Long
		return self.get_query_params().get('EditingJobOssFileUid')

	def set_EditingJobOssFileUid(self, EditingJobOssFileUid):  # Long
		self.add_query_param('EditingJobOssFileUid', EditingJobOssFileUid)
	def get_EditingJobOutputs(self): # String
		return self.get_query_params().get('EditingJobOutputs')

	def set_EditingJobOutputs(self, EditingJobOutputs):  # String
		self.add_query_param('EditingJobOutputs', EditingJobOutputs)
	def get_ResourceOwnerAccount(self): # String
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self, ResourceOwnerAccount):  # String
		self.add_query_param('ResourceOwnerAccount', ResourceOwnerAccount)
	def get_OwnerAccount(self): # String
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self, OwnerAccount):  # String
		self.add_query_param('OwnerAccount', OwnerAccount)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_PipelineId(self): # String
		return self.get_query_params().get('PipelineId')

	def set_PipelineId(self, PipelineId):  # String
		self.add_query_param('PipelineId', PipelineId)
	def get_OutputBucket(self): # String
		return self.get_query_params().get('OutputBucket')

	def set_OutputBucket(self, OutputBucket):  # String
		self.add_query_param('OutputBucket', OutputBucket)
	def get_EditingJobOssFileRoleArn(self): # String
		return self.get_query_params().get('EditingJobOssFileRoleArn')

	def set_EditingJobOssFileRoleArn(self, EditingJobOssFileRoleArn):  # String
		self.add_query_param('EditingJobOssFileRoleArn', EditingJobOssFileRoleArn)
