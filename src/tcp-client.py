import socket
import time
hostname, port = '34.243.97.41', 8510

# create an ipv4 (AF_INET) socket object using the tcp protocol (SOCK_STREAM)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((hostname, port))

client.sendall('hola amigos\n');

data = '' 
while (data != '/exit'):
  try:
    data = raw_input('>> ')
    if (data != '/exit'):
      response = client.recv(4096);
      print(response);
  except EOFError:
    break


