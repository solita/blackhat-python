s = "$8:2>9#2%2$#>90$#%>90"

# https://stackoverflow.com/questions/3636928/test-if-a-python-string-is-printable
def is_printable(s):
  return not any(repr(ch).startswith("'\\x") or repr(ch).startswith("'\\u") for ch in s)

for i in range(0,255):
  s2 = ""
  for c in s:
    s2 = s2 + chr(i ^ ord(c))
  if (is_printable(s2)):
    print(str(i) + ": " + s2)

