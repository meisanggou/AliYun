#! /usr/bin/env python
# coding: utf-8

from JYAliYun.AliYunAccount import RAMAccount
from JYAliYun.AliYunRAM import RAMUserManager

__author__ = 'meisanggou'

ram_account = RAMAccount(conf_path="/data/Web2/conf/oss.conf")
user_man = RAMUserManager(ram_account=ram_account)
r_resp = user_man.get_user("api")
print(r_resp.text)
