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
print bucket_man.sing_file_url("dmsdata/editor/img/20173/zh_test_166_1490249799.png", server_url="file.gene.ac")

"""
head oss文件
"""

resp = bucket_man.head_object("dmsdata/editor/img/20173/zh_test_166_1490249799.png")
print(resp.status_code)
print(resp.headers)
