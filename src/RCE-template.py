#!/usr/bin/python
#
# Template for exploiting RCE vulnerabilities 

import os
import sys
import socket
import urllib
import requests

def runRCE(URL, cmd):
  print("RCE is go..")

# Pipe stuff to Burp (or some other proxy)
#  proxies = {
#    'http': 'http://127.0.0.1:8510',
#  }

# TODO: actual request (or a series of requests) needed to exploit the RCE
#  r = requests.post(URL, data=sonni, headers={"content-type": "application/json"})
#  print(r.text)


# USE LIKE: python attackshell.py http://exploitable.server.somewhere
URL = sys.argv[1]
print("URL: " + URL)

data = ''

# 1. loop as long  as the commmand is not "exit"
# 2. all other commands are sent to the remote server for RCE 
while (data != 'exit'):
  try:
    data = raw_input('>> ')
    if (data != 'exit'):
      runRCE(URL, data)
  except EOFError:
    break
