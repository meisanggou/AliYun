#! /usr/bin/env python
# coding: utf-8

from JYAliYun.AliYunAccount import RAMAccount
from JYAliYun.AliYunOSS import OSSObject

__author__ = 'ZhouHeng'

"""
配置文件示例 /data/Web2/conf/oss.conf
[Account]
access_key_id: LTA***u**AqEZ0H6
access_key_secret: 25*TaQ*EQPx*Ck*Jo*gKuspzPk7pzw
internal: false  #  是否为阿里内网

"""

"""
发送 主题消息
"""
conf_dir = "/data/Web2/conf"
oss_account = RAMAccount(conf_dir=conf_dir, conf_name="oss.conf")
oss_man = OSSObject(ram_account=oss_account)
print oss_man.sing_file_url("geneac", "dmsdata/editor/img/20173/zh_test_166_1490249799.png")
