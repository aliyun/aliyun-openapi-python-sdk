# credentials
class AccessKeyCredentials:
    def __init__(self, access_key_id, access_key_secret):
        self.access_key_id = access_key_id
        self.access_key_secret = access_key_secret


class BearTokenCredentials:
    def __init__(self, bearer_token):
        self.bearer_token = bearer_token


class SecurityCredentials:
    def __init__(self, access_key_id, access_key_secret, token):
        self.access_key_id = access_key_id
        self.access_key_secret = access_key_secret
        self.token = token
