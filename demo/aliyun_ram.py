#! /usr/bin/env python
# coding: utf-8

from JYAliYun.AliYunAccount import RAMAccount
from JYAliYun.AliYunRAM import RAMUserManager

__author__ = 'meisanggou'

ram_account = RAMAccount(conf_path="/data/Web2/conf/oss.conf")
user_man = RAMUserManager(ram_account=ram_account)

resp = user_man.create_user("api_test")
print(resp.text)

r_resp = user_man.get_user("api_test")
print(r_resp.text)

r_resp = user_man.delete_user("api_test")
print(r_resp.text)

r_resp = user_man.list_users()
print(r_resp.text)
