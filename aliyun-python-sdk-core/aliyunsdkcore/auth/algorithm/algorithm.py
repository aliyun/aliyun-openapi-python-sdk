# coding=utf-8


import hashlib
import hmac

from aliyunsdkcore.compat import ensure_string
from aliyunsdkcore.compat import ensure_bytes
from aliyunsdkcore.compat import b64_encode_bytes


def get_sign_string(source, secret):
    source = ensure_bytes(source)
    secret = ensure_bytes(secret)
    h = hmac.new(secret, source, hashlib.sha1)
    signature = ensure_string(b64_encode_bytes(h.digest()).strip())
    return signature


def get_signer_name():
    return "HMAC-SHA1"


def get_signer_version():
    return "1.0"


def get_signer_type():
    return ""


class ShaHmac1:

    def sign_string(self, source, secret):
        source = ensure_bytes(source)
        secret = ensure_bytes(secret)
        h = hmac.new(secret, source, hashlib.sha1)
        signature = ensure_string(b64_encode_bytes(h.digest()).strip())
        return signature

    @property
    def signer_name(self):
        return "HMAC-SHA1"

    @property
    def signer_version(self):
        return "1.0"

    @property
    def signer_type(self):
        return ""


class ShaHmac256:

    def get_sign_string(self, source, access_secret):
        if platform.system() != "Windows":
            from Crypto.Signature import PKCS1_v1_5
            from Crypto.Hash import SHA256
            from Crypto.PublicKey import RSA

            key = RSA.importKey(b64_decode_bytes(ensure_bytes(access_secret)))
            h = SHA256.new(ensure_bytes(source))
            signer = PKCS1_v1_5.new(key)
            signed_bytes = signer.sign(h)
            signed_base64 = b64_encode_bytes(signed_bytes)
            signature = ensure_string(signed_base64).replace('\n', '')
            return signature
        else:
            message = "auth type [publicKeyId] is disabled in Windows " \
                      "because 'pycrypto' is not supported, we will resolve " \
                      "this soon"
            raise exceptions.ClientException(error_code.SDK_NOT_SUPPORT, message)

    @property
    def signer_name(self):
        return "SHA256withRSA"

    @property
    def signer_version(self):
        return "1.0"

    @property
    def signer_type(self):
        return "PRIVATEKEY"


class BearToken:

    def sign_string(self, source, secret):
        return ""

    @property
    def signer_name(self):
        return ""

    @property
    def get_signer_version(self):
        return "1.0"

    @property
    def get_signer_type(self):
        return "BEARERTOKEN"
