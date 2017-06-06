#! /usr/bin/env python
# coding: utf-8

from JYAliYun.AliYunObject import ObjectManager
from JYAliYun.Tools import jy_requests
from JYAliYun.Tools import get_params

__author__ = 'meisanggou'


class RAMUserManager(ObjectManager):
    PRODUCT = "RAM"
    address = "https://ram.aliyuncs.com"

    def get_user(self, user_name):
        action = "GetUser"
        http_method = "GET"
        custom_params = dict(Action=action, UserName=user_name)
        print(self.access_key_id)
        params = get_params(self.access_key_id, self.access_key_secret, http_method, custom_params)
        resp = jy_requests.request(http_method, self.address, params=params)
        return resp
