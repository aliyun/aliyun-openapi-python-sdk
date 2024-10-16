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

class QueryHotelsRequest(RoaRequest):

	def __init__(self):
		RoaRequest.__init__(self, 'IQS', '2024-07-12', 'QueryHotels')
		self.set_protocol_type('https')
		self.set_uri_pattern('/amap-function-call-agent/iqs-agent-service/v1/nl/hotels')
		self.set_method('POST')

