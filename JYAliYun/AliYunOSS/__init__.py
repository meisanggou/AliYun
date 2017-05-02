#! /usr/bin/env python
# coding: utf-8

from time import time
from urllib import quote
from JYAliYun import AliYUN_DOMAIN_NAME
from JYAliYun.AliYunObject import ObjectManager
from JYAliYun.Tools import ali_signature, jy_requests

__author__ = 'meisanggou'


class OSSBucket(ObjectManager):
    def __init__(self, *args, **kwargs):
        kwargs["default_section"] = "OSS"
        super(OSSBucket, self).__init__(*args, **kwargs)
        if self.cfg.get("bucket") is not None:
            self.bucket_name = self.cfg.get('bucket')
        else:
            self.bucket_name = kwargs["bucket_name"]
        self.region = self.cfg.get("region", "beijing")
        self.protocol = self.cfg.get("protocol", "http")
        if self.is_internal is True:
            self.endpoint = "oss-cn-%s-internal.%s" % (self.region, AliYUN_DOMAIN_NAME)
        else:
            self.endpoint = "oss-cn-%s.%s" % (self.region, AliYUN_DOMAIN_NAME)
        self.server_url = "%s.%s" % (self.bucket_name, self.endpoint)

    @staticmethod
    def get_resource(bucket_name, key):
        return "/%s/%s" % (bucket_name, key)

    @staticmethod
    def format_key(key):
        return key.lstrip("/")

    def sing_file_url(self, key, method="GET", expires=60, server_url=None):
        key = OSSBucket.format_key(key)
        sign_url = self.protocol + "://"
        if server_url is not None:
            sign_url += server_url
        else:
            sign_url += self.server_url
        sign_url += "/%s" % quote(key, '')
        expires = "%s" % int(time() + expires)
        resource_string = "/%s/%s" % (self.bucket_name, key)
        signature = ali_signature(self.access_key_secret, method, "", "", expires, "", resource_string)
        sign_url += "?OSSAccessKeyId=%s&Expires=%s&Signature=%s" % (self.access_key_id, expires, quote(signature, ""))
        return sign_url

    def head_object(self, oss_object):
        if not oss_object.startswith("/"):
            oss_object = "/" + oss_object
        oss_resource = "/%s%s" % (self.bucket_name, oss_object)

        url = "http://%s%s" % (self.oss_host, oss_object)
        headers = ali_signature(self._access_id, self._access_secret, "HEAD", oss_resource)
        response = jy_requests.head(url)
        if response.status_code == 200:
            return True, response.headers
        return False, response.status_code
