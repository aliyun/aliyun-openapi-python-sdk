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

class HuichengetRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'AmpTest', '2020-12-30', 'Huichenget','AmpTest')
		self.set_method('POST')

	def get_Code(self): # String
		return self.get_query_params().get('Code')

	def set_Code(self, Code):  # String
		self.add_query_param('Code', Code)
	def get_Rong(self): # String
		return self.get_query_params().get('Rong')

	def set_Rong(self, Rong):  # String
		self.add_query_param('Rong', Rong)
	def get_Enight(self): # String
		return self.get_query_params().get('Enight')

	def set_Enight(self, Enight):  # String
		self.add_query_param('Enight', Enight)
	def get_Two(self): # String
		return self.get_query_params().get('Two')

	def set_Two(self, Two):  # String
		self.add_query_param('Two', Two)
	def get_Three(self): # String
		return self.get_query_params().get('Three')

	def set_Three(self, Three):  # String
		self.add_query_param('Three', Three)
	def get_Mack(self): # String
		return self.get_query_params().get('Mack')

	def set_Mack(self, Mack):  # String
		self.add_query_param('Mack', Mack)
	def get_Hold(self): # String
		return self.get_query_params().get('Hold')

	def set_Hold(self, Hold):  # String
		self.add_query_param('Hold', Hold)
	def get_Red(self): # String
		return self.get_query_params().get('Red')

	def set_Red(self, Red):  # String
		self.add_query_param('Red', Red)
	def get_Apple(self): # String
		return self.get_query_params().get('Apple')

	def set_Apple(self, Apple):  # String
		self.add_query_param('Apple', Apple)
	def get_Tea(self): # String
		return self.get_query_params().get('Tea')

	def set_Tea(self, Tea):  # String
		self.add_query_param('Tea', Tea)
	def get_East(self): # String
		return self.get_query_params().get('East')

	def set_East(self, East):  # String
		self.add_query_param('East', East)
	def get_White(self): # String
		return self.get_query_params().get('White')

	def set_White(self, White):  # String
		self.add_query_param('White', White)
	def get_Four(self): # String
		return self.get_query_params().get('Four')

	def set_Four(self, Four):  # String
		self.add_query_param('Four', Four)
	def get_Now(self): # String
		return self.get_query_params().get('Now')

	def set_Now(self, Now):  # String
		self.add_query_param('Now', Now)
	def get_Visity(self): # String
		return self.get_query_params().get('Visity')

	def set_Visity(self, Visity):  # String
		self.add_query_param('Visity', Visity)
	def get_Params2(self): # String
		return self.get_query_params().get('Params2')

	def set_Params2(self, Params2):  # String
		self.add_query_param('Params2', Params2)
	def get_Params3(self): # String
		return self.get_query_params().get('Params3')

	def set_Params3(self, Params3):  # String
		self.add_query_param('Params3', Params3)
	def get_Params4(self): # String
		return self.get_query_params().get('Params4')

	def set_Params4(self, Params4):  # String
		self.add_query_param('Params4', Params4)
	def get_Ten(self): # String
		return self.get_query_params().get('Ten')

	def set_Ten(self, Ten):  # String
		self.add_query_param('Ten', Ten)
	def get_Five(self): # String
		return self.get_query_params().get('Five')

	def set_Five(self, Five):  # String
		self.add_query_param('Five', Five)
	def get_Params1(self): # String
		return self.get_query_params().get('Params1')

	def set_Params1(self, Params1):  # String
		self.add_query_param('Params1', Params1)
	def get_Add(self): # String
		return self.get_query_params().get('Add')

	def set_Add(self, Add):  # String
		self.add_query_param('Add', Add)
	def get_News(self): # String
		return self.get_query_params().get('News')

	def set_News(self, News):  # String
		self.add_query_param('News', News)
	def get_New1(self): # String
		return self.get_query_params().get('New1')

	def set_New1(self, New1):  # String
		self.add_query_param('New1', New1)
	def get_Address(self): # String
		return self.get_query_params().get('Address')

	def set_Address(self, Address):  # String
		self.add_query_param('Address', Address)
	def get_Six(self): # String
		return self.get_query_params().get('Six')

	def set_Six(self, Six):  # String
		self.add_query_param('Six', Six)
	def get_NewName(self): # String
		return self.get_query_params().get('NewName')

	def set_NewName(self, NewName):  # String
		self.add_query_param('NewName', NewName)
	def get_List(self): # String
		return self.get_query_params().get('List')

	def set_List(self, List):  # String
		self.add_query_param('List', List)
	def get_Params(self): # String
		return self.get_query_params().get('Params')

	def set_Params(self, Params):  # String
		self.add_query_param('Params', Params)
	def get_Jack(self): # String
		return self.get_query_params().get('Jack')

	def set_Jack(self, Jack):  # String
		self.add_query_param('Jack', Jack)
	def get_Nigh(self): # String
		return self.get_query_params().get('Nigh')

	def set_Nigh(self, Nigh):  # String
		self.add_query_param('Nigh', Nigh)
	def get_Blue(self): # String
		return self.get_query_params().get('Blue')

	def set_Blue(self, Blue):  # String
		self.add_query_param('Blue', Blue)
	def get_Hello(self): # String
		return self.get_query_params().get('Hello')

	def set_Hello(self, Hello):  # String
		self.add_query_param('Hello', Hello)
