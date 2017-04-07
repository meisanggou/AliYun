#! /usr/bin/env python
# coding: utf-8

import hmac
import hashlib
import base64
import xml.dom.minidom

__author__ = 'ZhouHeng'

XMLNS = "http://www.gene.ac"


class ConvertObject(object):
    encoding = "utf-8"

    @staticmethod
    def decode(s):
        if isinstance(s, str):
            return s.decode(ConvertObject.encoding)
        return s

    @staticmethod
    def encode(s):
        if isinstance(s, unicode):
            return s.encode(ConvertObject.encoding)
        return s

    @staticmethod
    def dict_to_xml(tag_name, dict_data):
        tag_name = ConvertObject.decode(tag_name)
        doc = xml.dom.minidom.Document()
        root_node = doc.createElement(tag_name)
        root_node.setAttribute("xmlns", XMLNS)
        doc.appendChild(root_node)
        assert isinstance(dict_data, dict)
        for k, v in dict_data.items():
            key_node = doc.createElement(k)
            if isinstance(v, dict):
                for sub_k, sub_v in v.items():
                    sub_node = doc.createElement(sub_k)
                    sub_v = ConvertObject.decode(sub_v)
                    sub_node.appendChild(doc.createTextNode(sub_v))
                    key_node.appendChild(sub_node)
            else:
                v = ConvertObject.decode(v)
                key_node.appendChild(doc.createTextNode(v))
            root_node.appendChild(key_node)
        return doc.toxml("utf-8")


def ali_signature(access_key_secret, request_method, content_md5, content_type, request_time, x_headers, resource):
    if content_md5 is None:
        content_md5 = ""
    if content_type is None:
        content_type = ""
    x_headers_s = ""
    if x_headers is not None:
        if type(x_headers) == unicode:
            x_headers_s = x_headers
        elif type(x_headers) == dict:
            for key in sorted(x_headers.keys()):
                x_headers_s += key.lower() + ":" + x_headers[key] + "\n"
    msg = "%s\n%s\n%s\n%s\n%s%s" % (request_method, content_md5, content_type, request_time, x_headers_s, resource)
    h = hmac.new(access_key_secret, msg, hashlib.sha1)
    signature = base64.b64encode(h.digest())
    return signature
