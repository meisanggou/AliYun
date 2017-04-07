#! /usr/bin/env python
# coding: utf-8

from JYAliYun.AliYunObject import ObjectManager

__author__ = 'meisanggou'


class OSSObject(ObjectManager):
    def __init__(self, *args, **kwargs):
        super(OSSObject, self).__init__(*args, **kwargs)
