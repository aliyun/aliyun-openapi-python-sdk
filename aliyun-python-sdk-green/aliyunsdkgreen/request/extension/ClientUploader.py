#coding=utf-8
import oss2
import uuid
import json
import time
import threading
import sys
from aliyunsdkgreen.request.v20180509 import UploadCredentialsRequest
from aliyunsdkgreen.request.extension import UploadCredentials
from aliyunsdkgreen.request.extension import HttpContentHelper

lock = lock=threading.Lock()
class ClientUploader:

    def __init__(self, clt, filType):
        self._clt = clt
        self._credentials = None
        self._header = {}
        self._fileType = filType

# 从获取上传凭证
    def _getCredential(self):
        if self._credentials == None or self._credentials.get_ExpiredTime() < time.time()*1000:
            lock.acquire()
            try:
                if self._credentials == None or self._credentials.get_ExpiredTime() < time.time()*1000:
                   self._credentials = self._getCredentialsFromServer()
            finally:
                lock.release()
        return self._credentials

# 从服务器端获取上传凭证
    def _getCredentialsFromServer(self):
        request = UploadCredentialsRequest.UploadCredentialsRequest()
        request.set_accept_format('JSON')
        # python2 和python3 这里调用设置不一样
        if sys.version_info[0] == 2:
            for (key, value) in self._header.iteritems():
                request.add_header(key, value)
        if sys.version_info[0] == 3:
            for (key, value) in self._header.items():
                request.add_header(key, value)
        request.set_content(HttpContentHelper.toValue({}))
        response = self._clt.do_action(request)
        result = json.loads(response)
        if 200 == result['code']:
            data = result['data']
            return UploadCredentials.UploadCredentials(data['accessKeyId'],data['accessKeySecret'], data['securityToken'],data['expiredTime'],data['ossEndpoint'],data['uploadBucket'],data['uploadFolder'])
        raise RuntimeError('get upload credential from server fail. requestId:' + str(result['requestId']) + ', code:' + str(result['code']))

# 上传本地文件
    def uploadFile(self, yourLocalFilePath):
        credentials = self._getCredential();
        if credentials == None:
            raise RuntimeError('can not get upload credentials')
        auth = oss2.StsAuth(self._credentials.get_AccessKeyId(), self._credentials.get_AccessKeySecret(), self._credentials.get_SecurityToken())
        bucket = oss2.Bucket(auth, self._credentials.get_OssEndpoint(), self._credentials.get_UploadBucket())
        objectKey = self._credentials.get_UploadFolder() + '/' + self._fileType + '/' + str(uuid.uuid1()) + '.jpg'
        bucket.put_object_from_file(objectKey , yourLocalFilePath)
        return 'oss://' + self._credentials.get_UploadBucket() + "/" + objectKey

# 上传Bytes
    def uploadBytes(self, bytes):
        credentials = self._getCredential();
        if credentials == None:
            raise RuntimeError('can not get upload credentials')
        auth = oss2.StsAuth(self._credentials.get_AccessKeyId(), self._credentials.get_AccessKeySecret(),
                            self._credentials.get_SecurityToken())
        bucket = oss2.Bucket(auth, self._credentials.get_OssEndpoint(), self._credentials.get_UploadBucket())
        objectKey = self._credentials.get_UploadFolder() + '/' + self._fileType + '/' + str(uuid.uuid1()) + '.jpg'
        bucket.put_object(objectKey, bytes)
        return 'oss://' + self._credentials.get_UploadBucket() + '/' + objectKey

    def add_header(self, k, v):
        self._header[k] = v

def getImageClientUploader(clt):
    return ClientUploader(clt, "images");

def getVideoClientUploader(clt):
    return ClientUploader(clt, "videos");

def getVoiceClientUploader(clt):
    return ClientUploader(clt, "voices");

def getFileClientploader(clt):
    return ClientUploader(clt, "files");


