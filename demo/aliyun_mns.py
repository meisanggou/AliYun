#! /usr/bin/env python
# coding: utf-8

from JYAliYun.AliYunAccount import RAMAccount
from JYAliYun.AliYunMNS.AliMNSServer import MNSServerManager

__author__ = 'ZhouHeng'

"""
配置文件示例 目录./config
[Account]
access_key_id: LTA***u**AqEZ0H6
access_key_secret: 25*TaQ*EQPx*Ck*Jo*gKuspzPk7pzw
internal: false  #  是否为阿里内网

[MNS]
account_id: 1***53***1163833
region: beijing  #  所属区域
"""

"""
发送 主题消息
"""
conf_dir = "conf"
mns_account = RAMAccount(conf_dir=conf_dir, conf_name="mns.conf")
mns_server = MNSServerManager(ram_account=mns_account, conf_dir=conf_dir)

topic_name = "JYWaring"
mns_topic = mns_server.get_topic(topic_name)
message_body = "This is An Example Of Publish Message\n这是一个发送主题消息示例"
message_tag = "TEST"
mns_topic.publish_message(message_body, message_tag)
