# coding=utf-8

import re
import os
import logging

def detect(request):
    user_agent = request.headers['User-Agent']
    result = {}
    result['ua'] = user_agent
    if (re.search('iPod|iPhone|Android|Opera Mini|BlackBerry|webOS|UCWEB', user_agent)):
        result['ios'] = True
    else:
        result['ios'] = False
    return result