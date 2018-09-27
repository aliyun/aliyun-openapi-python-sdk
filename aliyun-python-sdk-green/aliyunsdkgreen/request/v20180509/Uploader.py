#coding=utf-8
import oss2
import hashlib
import uuid
import json
import time
import UploadCredentialsRequest
import UploadCredentials
class Uploader:
    def __init__(self, clt):
        self._clt = clt
        self._credentials = None
        self._header = {}

    def _getPrefix(self, fileType):
        if 'image' == fileType:
            return 'images'
        if 'video' == fileType:
            return 'videos'
        return 'images'

# 从获取上传凭证
    def _getCredential(self):
        if self._credentials == None:
            self._credentials = self._getCredentialsFromServer()
        if self._credentials.get_ExpiredTime() < time.time()*1000:
            self._credentials = self._getCredentialsFromServer()
        return self._credentials

# 从服务器端获取上传凭证
    def _getCredentialsFromServer(self):
        request = UploadCredentialsRequest.UploadCredentialsRequest()
        request.set_accept_format('JSON')
        request.set_content(bytearray(json.dumps({}), 'utf-8'))
        for (key, value) in self._header.iteritems():
                request.add_header(key, value)
        response = self._clt.do_action(request)
        result = json.loads(response)
        if 200 == result['code']:
            data = result['data']
            return UploadCredentials.UploadCredentials(data['accessKeyId'],data['accessKeySecret'], data['securityToken'],data['expiredTime'],data['ossEndpoint'],data['uploadBucket'],data['uploadFolder'])
        raise RuntimeError('get upload credential from server fail. requestId:' + str(result['requestId']) + ', code:' + str(result['code']))

# 上传本地文件
    def uploadFile(self, yourLocalFilePath, fileType):
        credentials = self._getCredential();
        if credentials == None:
            raise RuntimeError('can not get upload credentials')
        auth = oss2.StsAuth(self._credentials.get_AccessKeyId(), self._credentials.get_AccessKeySecret(), self._credentials.get_SecurityToken())
        bucket = oss2.Bucket(auth, self._credentials.get_OssEndpoint(), self._credentials.get_UploadBucket())
        objectKey = self._credentials.get_UploadFolder() + '/' + self._getPrefix(fileType) + '/' + hashlib.md5(yourLocalFilePath.encode('utf-8')).hexdigest()
        bucket.put_object_from_file(objectKey , yourLocalFilePath)
        return 'oss://' + self._credentials.get_UploadBucket() + "/" + objectKey

# 上传Bytes
    def uploadBytes(self, bytes, fileType):
        credentials = self._getCredential();
        if credentials == None:
            raise RuntimeError('can not get upload credentials')
        auth = oss2.StsAuth(self._credentials.get_AccessKeyId(), self._credentials.get_AccessKeySecret(),
                            self._credentials.get_SecurityToken())
        bucket = oss2.Bucket(auth, self._credentials.get_OssEndpoint(), self._credentials.get_UploadBucket())
        objectKey = self._credentials.get_UploadFolder() + '/' + self._getPrefix(fileType) + '/' + hashlib.md5(
            str(uuid.uuid1()).encode('utf-8')).hexdigest()
        bucket.put_object(objectKey, bytes)
        return 'oss://' + self._credentials.get_UploadBucket() + '/' + objectKey

    def add_header(self, k, v):
        self._header[k] = v