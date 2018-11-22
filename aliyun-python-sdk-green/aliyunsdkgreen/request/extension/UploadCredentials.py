class UploadCredentials:
    def __init__(self, accessKeyId,
                 accessKeySecret,
                 securityToken,
                 expiredTime,
                 ossEndpoint,
                 uploadBucket,
                 uploadFolder
                 ):
        self._accessKeyId = accessKeyId
        self._accessKeySecret = accessKeySecret
        self._securityToken = securityToken
        self._expiredTime = expiredTime
        self._ossEndpoint = ossEndpoint;
        self._uploadBucket = uploadBucket;
        self._uploadFolder = uploadFolder;

    def get_AccessKeyId(self):
        return self._accessKeyId

    def set_AccessKeyId(self, accessKeyId):
         self._accessKeyId = accessKeyId

    def get_AccessKeySecret(self):
        return self._accessKeySecret

    def set_AccessKeySecret(self, accessKeySecret):
         self._accessKeySecret = accessKeySecret

    def get_SecurityToken(self):
        return self._securityToken

    def set_SecurityToken(self, securityToken):
         self._securityToken = securityToken

    def get_ExpiredTime(self):
        return self._expiredTime

    def set_ExpiredTime(self, expiredTime):
         self._expiredTime = expiredTime

    def get_OssEndpoint(self):
        return self._ossEndpoint

    def set_OssEndpoint(self, ossEndpoint):
         self._ossEndpoint = ossEndpoint

    def get_UploadBucket(self):
        return self._uploadBucket

    def set_UploadBucket(self, uploadBucket):
         self._uploadBucket = uploadBucket

    def get_UploadFolder(self):
        return self._uploadFolder

    def set_UploadFolder(self, uploadFolder):
         self._uploadFolder = uploadFolder