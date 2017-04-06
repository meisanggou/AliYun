#! /usr/bin/env python
# coding: utf-8

from JYAliYun.AliYunAccount import RAMAccount
from JYAliYun.AliYunMNS.AliMNSServer import MNSServerManager

__author__ = 'ZhouHeng'

"""
配置文件示例 /data/Web2/conf/mns.conf
[Account]
access_key_id: LTAIjqu3vAqEZ0H6
access_key_secret: 25QTaQVEQPxMCkjJolgKuspzPk7pzw

[MNS]
account_id: 1530531001163833
region: beijing
internal: false
"""

"""
发送 主题消息
"""
conf_dir = "/data/Web2/conf"
mns_account = RAMAccount(conf_dir=conf_dir, conf_name="mns.conf")
mns_server = MNSServerManager(mns_account, conf_dir=conf_dir)

topic_name = "JYWaring"
mns_topic = mns_server.get_topic(topic_name)
message_body = "This is An Example Of Publish Message"
message_tag = "TEST"
mns_topic.publish_message(message_body, message_tag)
