#! /usr/bin/env python
# coding: utf-8

from time import time
import base64
import hmac
import hashlib
from urllib import quote
from JYAliYun.AliYunObject import ObjectManager
from JYAliYun.Tools import ali_signature

__author__ = 'meisanggou'


class OSSObject(ObjectManager):
    def sign_url(self, endpoint, bucket_name, key, expires=60):
        url = "http://%s.%s/%s" % (bucket_name, quote(endpoint, ''), quote(key, ''))
        Expires = "%s" % int(time() + expires)
        resource_string = "/%s/%s" % (bucket_name, key)
        signature = ali_signature(self.access_key_secret, "GET", "", "", Expires, "", resource_string)
        url += "?OSSAccessKeyId=%s&Expires=%s&Signature=%s" % (self.access_key_id, Expires, quote(signature, ""))
        return url

    def sing_file_url(self, bucket_name, key, expires=60):
        url = "http://file.gene.ac/%s" % quote(key, '')
        Expires = "%s" % int(time() + expires)
        resource_string = "/%s/%s" % (bucket_name, key)
        signature = ali_signature(self.access_key_secret, "GET", "", "", Expires, "", resource_string)
        url += "?OSSAccessKeyId=%s&Expires=%s&Signature=%s" % (self.access_key_id, Expires, quote(signature, ""))
        return url


class OSSBucket(ObjectManager):
    def __init__(self, bucket_name, *args, **kwargs):
        super(OSSBucket, self).__init__(*args, **kwargs)
        self.bucket_name = bucket_name

    @staticmethod
    def get_resource(bucket_name, key):
        return "/%s/%s" % (bucket_name, key)

    def sing_file_url(self, key, expires=60):
        url = "http://file.gene.ac/%s" % quote(key, '')
        Expires = "%s" % int(time() + expires)
        resource_string = OSSBucket.get_resource(self.bucket_name, key)
        signature = ali_signature(self.access_key_secret, "GET", "", "", Expires, "", resource_string)
        url += "?OSSAccessKeyId=%s&Expires=%s&Signature=%s" % (self.access_key_id, Expires, quote(signature, ""))
        return url
