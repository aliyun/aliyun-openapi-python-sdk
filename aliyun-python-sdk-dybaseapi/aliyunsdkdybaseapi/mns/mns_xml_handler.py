# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

# coding=utf-8


import xml.dom.minidom
import base64
import string
import types
from aliyunsdkdybaseapi.mns.mns_exception import *
from aliyunsdkdybaseapi.mns.mns_request import *
try:
    import json
except ImportError as e:
    import simplejson as json

XMLNS = "http://mns.aliyuncs.com/doc/v1/"
class EncoderBase:
    @staticmethod
    def insert_if_valid(item_name, item_value, invalid_value, data_dic):
        if item_value != invalid_value:
            data_dic[item_name] = item_value

    @staticmethod
    def list_to_xml(tag_name1, tag_name2, data_list):
        doc = xml.dom.minidom.Document()
        rootNode = doc.createElement(tag_name1)
        rootNode.attributes["xmlns"] = XMLNS
        doc.appendChild(rootNode)
        if data_list:
            for item in data_list:
                keyNode = doc.createElement(tag_name2)
                rootNode.appendChild(keyNode)
                keyNode.appendChild(doc.createTextNode(item))
        else:
            nullNode = doc.createTextNode("")
            rootNode.appendChild(nullNode)
        return doc.toxml("utf-8")

    @staticmethod
    def dic_to_xml(tag_name, data_dic):
        doc = xml.dom.minidom.Document()
        rootNode = doc.createElement(tag_name)
        rootNode.attributes["xmlns"] = XMLNS
        doc.appendChild(rootNode)
        if data_dic:
            for k,v in data_dic.items():
                keyNode = doc.createElement(k)
                if type(v) is types.DictType:
                    for subkey,subv in v.items():
                        subNode = doc.createElement(subkey)
                        subNode.appendChild(doc.createTextNode(subv))
                        keyNode.appendChild(subNode)
                else:
                    keyNode.appendChild(doc.createTextNode(v))
                rootNode.appendChild(keyNode)
        else:
            nullNode = doc.createTextNode("")
            rootNode.appendChild(nullNode)
        return doc.toxml("utf-8")

    @staticmethod
    def listofdic_to_xml(root_tagname, sec_tagname, dataList):
        doc = xml.dom.minidom.Document()
        rootNode = doc.createElement(root_tagname)
        rootNode.attributes["xmlns"] = XMLNS
        doc.appendChild(rootNode)
        if dataList:
            for subData in dataList:
                secNode = doc.createElement(sec_tagname)
                rootNode.appendChild(secNode)
                if not subData:
                    nullNode = doc.createTextNode("")
                    secNode.appendChild(nullNode)
                    continue
                for k,v in subData.items():
                    keyNode = doc.createElement(k)
                    secNode.appendChild(keyNode)
                    keyNode.appendChild(doc.createTextNode(v))
        else:
            nullNode = doc.createTextNode("")
            rootNode.appendChild(nullNode)
        return doc.toxml("utf-8")

class QueueEncoder(EncoderBase):
    @staticmethod
    def encode(data, has_slice = True):
        queue = {}
        EncoderBase.insert_if_valid("VisibilityTimeout", str(data.visibility_timeout), "-1", queue)
        EncoderBase.insert_if_valid("MaximumMessageSize", str(data.maximum_message_size), "-1", queue)
        EncoderBase.insert_if_valid("MessageRetentionPeriod", str(data.message_retention_period), "-1", queue)
        EncoderBase.insert_if_valid("DelaySeconds", str(data.delay_seconds), "-1", queue)
        EncoderBase.insert_if_valid("PollingWaitSeconds", str(data.polling_wait_seconds), "-1", queue)

        logging_enabled = str(data.logging_enabled)
        if str(data.logging_enabled).lower() == "true":
            logging_enabled = "True"
        elif str(data.logging_enabled).lower() == "false":
            logging_enabled = "False"
        EncoderBase.insert_if_valid("LoggingEnabled", logging_enabled, "None", queue)
        return EncoderBase.dic_to_xml("Queue", queue)

class MessageEncoder(EncoderBase):
    @staticmethod
    def encode(data):
        message = {}
        if data.base64encode:
            #base64 only support str
            tmpbody = data.message_body.encode('utf-8') if isinstance(data.message_body, unicode) else data.message_body
            msgbody = base64.b64encode(tmpbody)
        else:
            #xml only support unicode when contains Chinese
            msgbody = data.message_body.decode('utf-8') if isinstance(data.message_body, str) else data.message_body
        EncoderBase.insert_if_valid("MessageBody", msgbody, "", message)
        EncoderBase.insert_if_valid("DelaySeconds", str(data.delay_seconds), "-1", message)
        EncoderBase.insert_if_valid("Priority", str(data.priority), "-1", message)
        return EncoderBase.dic_to_xml("Message", message)

class MessagesEncoder:
    @staticmethod
    def encode(message_list, base64encode):
        msglist = []
        for msg in message_list:
            item = {}
            if base64encode:
                #base64 only support str
                tmpbody = msg.message_body.encode('utf-8') if isinstance(msg.message_body, unicode) else msg.message_body
                msgbody = base64.b64encode(tmpbody)
            else:
                #xml only support unicode when contains Chinese
                msgbody = msg.message_body.decode('utf-8') if isinstance(msg.message_body, str) else msg.message_body
            EncoderBase.insert_if_valid("MessageBody", msgbody, "", item)
            EncoderBase.insert_if_valid("DelaySeconds", str(msg.delay_seconds), "-1", item)
            EncoderBase.insert_if_valid("Priority", str(msg.priority), "-1", item)
            msglist.append(item)
        return EncoderBase.listofdic_to_xml("Messages", "Message", msglist)

class ReceiptHandlesEncoder:
    @staticmethod
    def encode(receipt_handle_list):
        return EncoderBase.list_to_xml("ReceiptHandles", "ReceiptHandle", receipt_handle_list)


#-------------------------------------------------decode-----------------------------------------------------#
class DecoderBase:
    @staticmethod
    def xml_to_nodes(tag_name, xml_data):
        if xml_data == "":
            raise MNSClientNetworkException("RespDataDamaged", "Xml data is \"\"!")

        try:
            dom = xml.dom.minidom.parseString(xml_data)
        except Exception as e:
            raise MNSClientNetworkException("RespDataDamaged", xml_data)

        nodelist = dom.getElementsByTagName(tag_name)
        if not nodelist:
            raise MNSClientNetworkException("RespDataDamaged", "No element with tag name '%s'.\nData:%s" % (tag_name, xml_data))

        return nodelist[0].childNodes

    @staticmethod
    def xml_to_dic(tag_name, xml_data, data_dic, req_id=None):
        try:
            for node in DecoderBase.xml_to_nodes(tag_name, xml_data):
                if node.nodeName != "#text":
                    if node.childNodes != []:
                        data_dic[node.nodeName] = node.firstChild.data
                    else:
                        data_dic[node.nodeName] = ""
        except MNSClientNetworkException as e:
            raise MNSClientNetworkException(e.type, e.message, req_id)

    @staticmethod
    def xml_to_listofdic(root_tagname, sec_tagname, xml_data, data_listofdic, req_id=None):
        try:
            for message in DecoderBase.xml_to_nodes(root_tagname, xml_data):
                if message.nodeName != sec_tagname:
                    continue

                data_dic = {}
                for property in message.childNodes:
                    if property.nodeName != "#text" and property.childNodes != []:
                        data_dic[property.nodeName] = property.firstChild.data
                data_listofdic.append(data_dic)
        except MNSClientNetworkException as e:
            raise MNSClientNetworkException(e.type, e.message, req_id)

class BatchRecvMessageDecoder(DecoderBase):
    @staticmethod
    def decode(xml_data, base64decode, req_id=None):
        data_listofdic = []
        message_list = []
        DecoderBase.xml_to_listofdic("Messages", "Message", xml_data, data_listofdic, req_id)
        try:
            for data_dic in data_listofdic:
                msg = ReceiveMessageResponseEntry()
                if base64decode:
                    msg.message_body = base64.b64decode(data_dic["MessageBody"])
                else:
                    msg.message_body = data_dic["MessageBody"]
                msg.dequeue_count = int(data_dic["DequeueCount"])
                msg.enqueue_time = int(data_dic["EnqueueTime"])
                msg.first_dequeue_time = int(data_dic["FirstDequeueTime"])
                msg.message_id = data_dic["MessageId"]
                msg.message_body_md5 = data_dic["MessageBodyMD5"]
                msg.priority = int(data_dic["Priority"])
                msg.next_visible_time = int(data_dic["NextVisibleTime"])
                msg.receipt_handle = data_dic["ReceiptHandle"]
                message_list.append(msg)
        except Exception as e:
            raise MNSClientNetworkException("RespDataDamaged", xml_data, req_id)
        return message_list

class BatchDeleteMessageDecoder(DecoderBase):
    @staticmethod
    def decodeError(xml_data, req_id=None):
        try:
            return ErrorDecoder.decodeError(xml_data, req_id)
        except Exception as e:
            pass

        data_listofdic = []
        DecoderBase.xml_to_listofdic("Errors", "Error", xml_data, data_listofdic, req_id)
        if len(data_listofdic) == 0:
            raise MNSClientNetworkException("RespDataDamaged", xml_data, req_id)

        key_list = sorted(["ErrorCode", "ErrorMessage", "ReceiptHandle"])
        for data_dic in data_listofdic:
            for key in key_list:
                keys = sorted(data_dic.keys())
                if keys != key_list:
                    raise MNSClientNetworkException("RespDataDamaged", xml_data, req_id)
        return data_listofdic[0]["ErrorCode"], data_listofdic[0]["ErrorMessage"], None, None, data_listofdic

class ErrorDecoder(DecoderBase):
    @staticmethod
    def decodeError(xml_data, req_id=None):
        data_dic = {}
        DecoderBase.xml_to_dic("Error", xml_data, data_dic, req_id)
        key_list = ["Code", "Message", "RequestId", "HostId"]
        for key in key_list:
            if key not in data_dic.keys():
                raise MNSClientNetworkException("RespDataDamaged", xml_data, req_id)
        return data_dic["Code"], data_dic["Message"], data_dic["RequestId"], data_dic["HostId"], None
