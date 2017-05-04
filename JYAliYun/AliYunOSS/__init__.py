#! /usr/bin/env python
# coding: utf-8

from time import time
from lxml import etree
from urllib import quote
from JYAliYun import AliYUN_DOMAIN_NAME
from JYAliYun.AliYunObject import ObjectManager
from JYAliYun.Tools import ali_signature, jy_requests

__author__ = 'meisanggou'


class OSSBucket(ObjectManager):
    PRODUCT = "OSS"

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
        key = OSSBucket.format_key(key)
        return "/%s/%s" % (bucket_name, key)

    @staticmethod
    def format_key(key):
        return key.lstrip("/")

    def join_url(self, oss_object, server_url=None):
        url = self.protocol + "://"
        if server_url is not None:
            url += server_url
        else:
            url += self.server_url
        url += "/" + self.format_key(oss_object)
        return url

    def sing_file_url(self, key, method="GET", expires=60, server_url=None):
        key = OSSBucket.format_key(key)
        sign_url = self.join_url(quote(key, ''), server_url)
        expires = "%s" % int(time() + expires)
        resource_string = self.get_resource(self.bucket_name, key)
        signature = ali_signature(self.access_key_secret, method, "", "", expires, "", resource_string)
        sign_url += "?OSSAccessKeyId=%s&Expires=%s&Signature=%s" % (self.access_key_id, expires, quote(signature, ""))
        return sign_url

    def head_object(self, oss_object):
        key = OSSBucket.format_key(oss_object)
        url = self.join_url(oss_object)
        headers = self.ali_headers("HEAD", "", "", "", self.get_resource(self.bucket_name, key))
        response = jy_requests.head(url, headers=headers)
        return response

    def init_mul_upload(self, oss_object):
        headers = self.ali_headers("POST", "", "", None, OSSBucket.get_resource(self.bucket_name, oss_object),
                                   sub_resource={"uploads": None})
        url = self.join_url(oss_object) + "?uploads"
        resp = jy_requests.post(url, headers=headers)
        r_d = dict(status_code=resp.status_code, text=resp.text, headers=resp.headers)
        if resp.status_code / 100 != 2:
            return r_d
        res_ele = etree.fromstring(resp.text.encode("utf-8"))
        r_d["data"] = dict(bucket_name=res_ele.find("Bucket").text, key=res_ele.find("Key").text,
                           upload_id=res_ele.find("UploadId").text)
        return r_d

    def part_copy(self, upload_id, part_num, oss_object, copy_range, source_object, source_bucket=None):
        if source_bucket is None:
            source_bucket = self.bucket_name
        copy_source = OSSBucket.get_resource(source_bucket, source_object)
        x_headers = {"x-oss-copy-source": copy_source, "x-oss-copy-source-range": copy_range}
        del x_headers["x-oss-copy-source-range"]
        sub_resource = dict(partNumber=part_num, uploadId=upload_id)
        headers = self.ali_headers("PUT", "", "", x_headers, OSSBucket.get_resource(self.bucket_name, oss_object),
                                   sub_resource=sub_resource)
        url = self.join_url(oss_object)
        print(url)
        print(sub_resource)
        resp = jy_requests.put(url, params=sub_resource, headers=headers)
        return resp
