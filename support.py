import random
import re


# using at SDV.fea_eng.find_mul_class_col()
def data_struc(s):
    """calculate the data type share of string"""
    l = len(s)
    num = len(re.findall('[0-9]',s))
    alpha = len(re.findall('[a-zA-Z]',s))
    
    return {'Number':num/l,'Alphabet':alpha/l,'Others':(l-num-alpha)/l}



# translate script.
import urllib.request

import urllib.parse

import json

 

def get_data(words):

    data = {}

    data["type"] = "AUTO"

    data["i"] = words

    data["doctype"] = "json"

    data["xmlVersion"] = "1.8"

    data["keyfrom:fanyi"] = "web"

    data["ue"] = "UTF-8"

    data["action"] = "FY_BY_CLICKBUTTON"

    data["typoResult"] = "true"

    data = urllib.parse.urlencode(data).encode('utf-8')

    return data

 

def url_open(url, data):

    req = urllib.request.Request(url, data)

    req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36")

    response = urllib.request.urlopen(req)

    html = response.read()

    html = html.decode("utf-8")

    return html

 

def get_json_data(html):

    result = json.loads(html)

    result = result['translateResult']

    result = result[0][0]['tgt']

    return result


def translate(word):
    
    url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=dict.top"
    
    data = get_data(word)
    
    html = url_open(url, data)
    
    return get_json_data(html)