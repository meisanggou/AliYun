#! /usr/bin/env python
# coding: utf-8

from JYAliYun.AliYunAccount import RAMAccount
from JYAliYun.AliYunOSS import OSSBucket

__author__ = 'ZhouHeng'

"""
配置文件示例 conf/oss.conf
[Account]
access_key_id: LTA***u**AqEZ0H6
access_key_secret: 25*TaQ*EQPx*Ck*Jo*gKuspzPk7pzw
internal: false  #  是否为阿里内网

[OSS]
bucket: geneac
region: beijing #  不存在时默认为beijing

"""

"""
生成oss文件授权链接
"""
conf_dir = "conf"
oss_account = RAMAccount(conf_dir=conf_dir, conf_name="oss.conf")
bucket_man = OSSBucket(ram_account=oss_account, conf_dir=conf_dir, conf_name="oss.conf")
print bucket_man.sing_file_url("zh_t045/readme.txt")

"""
head oss文件
"""
head_object = "admin/SR16043_L001/C16121640570-YH112-SR16043-WES_S1_L001_R1_001.fastq.gz"
resp = bucket_man.head_object(head_object)
print(resp.status_code)
print(resp.headers)

"""
InitiateMultipartUpload
"""
resp = bucket_man.init_mul_upload("zh_t045/C16121640570-SR16043-WES_S1_L001_R1_001.fastq.gz")
assert resp["status_code"] == 200
# print(resp["data"])
upload_id = resp["data"]["upload_id"]
key = resp["data"]["key"]

"""
UploadPartCopy
"""
# print(upload_id)
# resp = bucket_man.part_copy(upload_id, 1, key, copy_range="0-1024000", source_object=head_object)
# print(resp.text)


"""
Get Bucket (List Object)
"""

resp = bucket_man.list_object(max_keys=100, prefix="admin/MJYLWXZ/", delimiter="/")
assert resp["status_code"] == 200
print resp["data"]["keys"]