from pwn import *
import argparse
import os
import string

#context.log_level = "debug"
LOCAL_PATH = "./serverperver"

def get_process(is_remote = False):
  if is_remote:
    return remote("127.0.0.1", 8510)
  else:
    return process(LOCAL_PATH)

parser = argparse.ArgumentParser()
parser.add_argument("-r", "--remote", help="Execute on remote server", action="store_true")
args = parser.parse_args()

e = ELF(LOCAL_PATH)

p = get_process(args.remote)

def read_menu(proc):
  s = proc.recvline()
  log.info("> " + s)

# DO the tricks here
read_menu(p)
p.interactive()

s = p.recvline()
log.info("ok " + s)
