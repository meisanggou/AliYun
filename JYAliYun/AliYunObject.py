#! /usr/bin/env python
# coding: utf-8

import os
import logging
from JYAliYun.Tools import ConfigManager
from JYAliYun.AliYunAccount import RAMAccount

__author__ = 'ZhouHeng'


class ObjectManager(object):
    def __init__(self, *args, **kwargs):
        self.cfg = ConfigManager(**kwargs)
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
            self.ram_account.assign_account_info(self)

        self.env = self.cfg.get("env", "")
        self.logging_dir = self.cfg.get("logging_dir", "")
        self.logging_name = self.cfg.get("logging_name", "")
        # self.run_log = logging.FileHandler(os.path.join(self.logging_dir, self.logging_name))

    def set_server_url(self, server_url):
        self.server_url = server_url

    def set_access_key_id(self, access_key_id):
        self.access_key_id = access_key_id

    def set_access_key_secret(self, access_key_secret):
        self.access_key_secret = access_key_secret

    def set_is_internal(self, is_internal):
        self.is_internal = is_internal

    def set_env(self, env):
        self.env = env

    def log(self, message, level="INFO"):
        pass
