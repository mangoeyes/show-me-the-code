#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-03-01 17:23:01
# @Author  : Huijun Wang (${email})
# @Link    : ${link}
# @Version : $Id$

import os
import requests
from bs4 import BeautifulSoup
'''
show me the code 
Q1
第 0000 题： 将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。 类似于图中效果
'''

# get my profile pic from Linkedin

headers = {
    "method": "GET",
    "scheme": "https",
    "version": "HTTP/1.1",
    "user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36"
}

conn = requests.session()

resp = conn.get("https://www.linkedin.com/in/huijun-wang/", headers=headers)

print(resp.request.headers)
