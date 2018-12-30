#!/bin/python3

import requests
import pyperclip

d=requests.get("http://temp-mail.org/en/")
string=d.text

prefix='id="mail" onclick="select(this);" data-original-title="Your temporary Email address" class="mail opentip" value="'
suffix='" data-placement="bottom" title="" type="text" readonly>'

startIndex=string.find(prefix) + len(prefix)
secondIndex=string.find(suffix)

email=string[startIndex:secondIndex]

pyperclip.copy(email)
