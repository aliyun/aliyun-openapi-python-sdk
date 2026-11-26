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
from aliyunsdkgpdb.endpoint import endpoint_data

class ModifyHadoopDataSourceRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'gpdb', '2016-05-03', 'ModifyHadoopDataSource','GPDB')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_DataSourceType(self): # String
		return self.get_query_params().get('DataSourceType')

	def set_DataSourceType(self, DataSourceType):  # String
		self.add_query_param('DataSourceType', DataSourceType)
	def get_HadoopCreateType(self): # String
		return self.get_query_params().get('HadoopCreateType')

	def set_HadoopCreateType(self, HadoopCreateType):  # String
		self.add_query_param('HadoopCreateType', HadoopCreateType)
	def get_YarnConf(self): # String
		return self.get_query_params().get('YarnConf')

	def set_YarnConf(self, YarnConf):  # String
		self.add_query_param('YarnConf', YarnConf)
	def get_DataSourceDescription(self): # String
		return self.get_query_params().get('DataSourceDescription')

	def set_DataSourceDescription(self, DataSourceDescription):  # String
		self.add_query_param('DataSourceDescription', DataSourceDescription)
	def get_EmrInstanceId(self): # String
		return self.get_query_params().get('EmrInstanceId')

	def set_EmrInstanceId(self, EmrInstanceId):  # String
		self.add_query_param('EmrInstanceId', EmrInstanceId)
	def get_HiveConf(self): # String
		return self.get_query_params().get('HiveConf')

	def set_HiveConf(self, HiveConf):  # String
		self.add_query_param('HiveConf', HiveConf)
	def get_HDFSConf(self): # String
		return self.get_query_params().get('HDFSConf')

	def set_HDFSConf(self, HDFSConf):  # String
		self.add_query_param('HDFSConf', HDFSConf)
	def get_DBInstanceId(self): # String
		return self.get_query_params().get('DBInstanceId')

	def set_DBInstanceId(self, DBInstanceId):  # String
		self.add_query_param('DBInstanceId', DBInstanceId)
	def get_MapReduceConf(self): # String
		return self.get_query_params().get('MapReduceConf')

	def set_MapReduceConf(self, MapReduceConf):  # String
		self.add_query_param('MapReduceConf', MapReduceConf)
	def get_HadoopHostsAddress(self): # String
		return self.get_query_params().get('HadoopHostsAddress')

	def set_HadoopHostsAddress(self, HadoopHostsAddress):  # String
		self.add_query_param('HadoopHostsAddress', HadoopHostsAddress)
	def get_HadoopCoreConf(self): # String
		return self.get_query_params().get('HadoopCoreConf')

	def set_HadoopCoreConf(self, HadoopCoreConf):  # String
		self.add_query_param('HadoopCoreConf', HadoopCoreConf)
	def get_DataSourceId(self): # String
		return self.get_query_params().get('DataSourceId')

	def set_DataSourceId(self, DataSourceId):  # String
		self.add_query_param('DataSourceId', DataSourceId)
