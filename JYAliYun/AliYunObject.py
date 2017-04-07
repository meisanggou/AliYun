#! /usr/bin/env python
# coding: utf-8

from JYAliYun.AliYunAccount import RAMAccount

__author__ = 'ZhouHeng'


class ObjectManager(object):
    def __init__(self, *args, **kwargs):
        self.server_url = None
        self.access_key_id = ""
        self.access_key_secret = ""
        self.is_internal = False
        self.ram_account = None
        if "ram_account" in kwargs:
            ram_account = kwargs["ram_account"]
            assert isinstance(ram_account, RAMAccount)
            self.ram_account = ram_account
        if len(args) > 0:
            ram_account = args[0]
            if isinstance(ram_account, RAMAccount):
                self.ram_account = ram_account
        if self.ram_account is not None:
            self.ram_account.assign_access_key(self)
            self.is_internal = self.ram_account.is_internal

    def set_server_url(self, server_url):
        self.server_url = server_url

    def set_access_key_id(self, access_key_id):
        self.access_key_id = access_key_id

    def set_access_key_secret(self, access_key_secret):
        self.access_key_secret = access_key_secret

    def set_is_internal(self, is_internal):
        self.is_internal = is_internal

    def assign_access_key(self, obj):
        assert isinstance(obj, ObjectManager)
        obj.set_access_key_secret(self.access_key_secret)
        obj.set_access_key_id(self.access_key_id)
