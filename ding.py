#!/bin/python3



import requests
import pyperclip
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

d=requests.get("http://www.yopmail.com/en/email-generator.php")
string=d.text

prefix='onmouseup="this.select();" type="text" value="'
suffix='&#64;yopmail.com"'
mailsuffix="&#64;yopmail.com"

startIndex=string.find(prefix) + len(prefix)
endIndex=string.find(suffix) + len(mailsuffix)

email=string[startIndex:endIndex].replace("&#64;", "@")

print(email)
pyperclip.copy(email)

driver = webdriver.Chrome()
driver.get("http://www.yopmail.com/en/")

inputElement = driver.find_element_by_id("login")
inputElement.send_keys(email)

#Now you can simulate hitting ENTER:
inputElement.send_keys(Keys.ENTER)
#or if it is a form you can submit:
#inputElement.submit()

