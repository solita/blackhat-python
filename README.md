This contains material for Black Hat Python workshop at Disobey 2019.

See the [introduction to the workshop](/da_presis.pdf)

The idea is to learn quickly prototyping scripts and tools for hacking. Obviously it's possible to do many things with the existing tools like sqlmap, Hydra, wfuzz etc. but sooner or later there is something that requires some custom programming or a custom tool. Due to time and other constraints these assignments and the content is quite basic, nothing fancy pro level stuff here. My blog post [Black Hat Programming](https://dev.solita.fi/2018/05/02/Black-Hat-Programming.html) explains the basic philosophy.

The material and the workshop was inspired by the [awesome book Black Hat Python](https://nostarch.com/blackhatpython), but the exercise tasks haven't been copied from the book. Get the book if you want to continue on this path.

So, despite the title, "Black hat" does not refer to illegal activities. Do not hack systems without a permission to do so! According to Finnish law, even an attempt to break into a computer system is a criminal offense. I think the law is pretty similar in other countries too.



# Preparations

1. Install Python, version 3 or 2.7 should both do fine. If you are running Linux or Mac OS, you almost certainly already have Python
installed. 

2. Get some kind of text editor. Emacs should do fine. You can use pycharm or some other IDE if you want, of course.


# Python ? 

Yes, Python. The friendly programming language. This is a very very short primer to Python, which you can skip if you know Python already.

Python can do pretty much anything from GUI programs to embedded systems, but we leave out some interesting aspects like OOP, functional programming, test automation, 
lambdas and threads here. Go check them out later - Python is very flexible and can support large software systems. It's not just a scripting language.

Python is an interpreted language (no compiler). ```python skribu.py``` uses the interpreter to run the program from a file. Very easy. If you run "python" on the command line, you get an interpreter. This is very handy for trying out something quickly. ```exit()``` brings you back to the command prompt.

Unusually, in Python, the code indentation defines code blocks so be careful with your copy-paste and spaces. But otherwise, everything is pretty straightforward and logical compared to other
mainstream languages.

```
t = "kekkonen" # t is a variable with a value of string "kekkonen".
```


```
# this is a loop that prints out 0,1,2,3,4 
for i in range(0, 5):
  print(i)
```

semicolon is used to separate for/if and such statements from the code blocks.

```map(f, s)``` calls f for each element in s. Pretty much how it works in any functional language.

if/else works pretty much like you would expect.

```
ìf True:
  print("Yea")
else:
  print("Nay")
```

## Python Strings

Python has all the standard string manipulation functions built-in. Search&Replace, find, join etc. ```split``` is often quite useful:

```
>>> "aattonajanottaa".split("j")
['aattona', 'anottaa']
```

"aattonajanottaa" is a string object and ```split``` is a method in string. The result is a list (vector) which you get if you cut it to pieces for each "j" in the string.

### Strings, UTF-8

UTF-8 and encodings are a bit annoying. Python 2.7 and 3.x behave differently, so be careful about what you are doing if you need to handle special characters in strings.

These all create strings with the character A in it.
```
t = "A"
t = u'A'    # unicode 
t = "\x41"  # hex encoded character
```

```hex```, ```chr```, ```ord```, ```decode``` and [repr](https://docs.python.org/2/library/repr.html) are particularly useful functions for our purposes in Python. Also [pprint](https://docs.python.org/2/library/pprint.html) which is standard stuff in REPL languages.

## Data structures

The most important Python datastructure we need is probably the "dict" (dictionary), which is basically a key -> value map. Works pretty much like a map in other languages, like so:
```
d = dict() # construct a new dictionary object
d['key'] = "makevaluesgreatagain"
# now d['key'] returns the value if we need it.
```

a ```set``` is also useful and works like you would expect from a set. With sets, vectors (arrays) and dicts, you are well covered.

## dependencies

[pip](https://packaging.python.org/tutorials/installing-packages/) is the mechanism for handling dependencies. In a "real" use i would be preferable to use something like [venv](https://docs.python.org/3/library/venv.html) to isolate separate projects from each other to manage version issues with dependencies and the core language versions. We'll skip that now.

## References

* The official Python site has the language reference and API reference for the core: (https://docs.python.org/2/contents.html)
* Standard functions of Python: (https://docs.python.org/2/library/functions.html)
* Python cheatsheet: (https://gto76.github.io/python-cheatsheet/)
* [requests](http://docs.python-requests.org/en/master/) is a nice HTTP library.
* [scapy](https://scapy.net/) is the Swiss army knife for all network hacking stuff in Python. Not necessary for trivial tasks.
* For fuzzing, [Radamsa](https://github.com/aoh/radamsa) is nice. See [Swissfuzz](https://github.com/ouspg/swissfuzz) and [Heartbreaker](https://github.com/lokori/heartbreaker) for Python interfacing.
* [SecLists](https://github.com/danielmiessler/SecLists) contains very useful lists for usernames, parameters and other things. Use them as input for your scripts.
* [rlwrap](https://linux.die.net/man/1/rlwrap) is a nice utility that really enchances your forward shell experience.
* [pwntools](http://docs.pwntools.com/en/stable/index.html) can be handy if you want to manipulate and play with binary executables.

# The tasks

You don't have to complete every task. Not realistic in two hour workshop.
You can choose whatever task you like the most. They are in no particular order.

* Task 1, RCE -> forward shell
* Task 2, LFI
* Task 3, "better strings"
* Task 4, Remote server pwn





# Task 1, RCE -> forward shell

We have found a web server in our penetration test that seems to be vulnerable and allows [remote code execution](https://en.wikipedia.org/wiki/Arbitrary_code_execution), RCE. It's tedious and time consuming to further exploit the server by manually crafting HTTP requests and parsing the responses from the server, so let's write a "shell" with Python that makes it pleasant to access the server.

(Obviously, if you could [get easily a reverse shell](http://pentestmonkey.net/cheat-sheet/shells/reverse-shell-cheat-sheet) from the server this wouldn't be necessary, but it's not always easy. Sometimes it can be pretty impossible even though you clearly have RCE.)

* ```pip install requests```
* Take the [template code](src/RCE-template.py) 
* Modify it to make a "shell" where you can interact with the remote server like you would have actual terminal connection to the server.
* Tidy up the HTML from the output to make it more user-friendly. Either use ```split``` and other string manipulation stuff or use [HTMLParser](https://docs.python.org/2/library/htmlparser.html)

## RCE Proof-of-Concept

```
POST /haveibeenpwned.php HTTP/1.1
Host: 34.243.97.41
Connection: close
Accept-Encoding: gzip, deflate
Accept: */*
User-Agent: python-requests/2.18.4
content-type: application/x-www-form-urlencoded
Content-Length: 38

site=iiro+*.dat+%26%26+pwd+%26%26+ls
```

We get back something like this:

```
<b>Pwnage results for <font color='green'>iiro *.dat && pwd && ls
</font> <br><br><br></b><table><tr><td>iiro@rot.fi</td></tr><br>
<tr><td>/var/www/html</td></tr><br>
<tr><td></td></tr><br>
</table>  </p>    
```

NOTE: 

Use [rlwrap](https://linux.die.net/man/1/rlwrap) to get command history and arrow keys working properly in your "shell". Installed on Mac and Linux by default.
Something like this:
```rlwrap python rce-shell.py http://34.243.97.41/haveibeenpwned.php 1.1.1.1```


# Task 2

Better "strings". 

It might happen that we have a binary, which has some kind of "secret" embedded in it. The trivial case will be revealed by running ```strings``` and maybe 
looking into it with a disassembler/debugger, but there are other nearly-as-trivial cases. Like XOR encryption over the key.

Create a Python program that can read the binary file and tries to locate and decrypt potential "secrets" out of it.

There is an example of a binary file for test material: (./secret.bin)

Something along these pseudocode lines perhaps:
  * slide an index over the file (say, i)
  * for byte sequence f[i]...f[i+n] check if it looks like a string (alphanumeric characters). At least n characters long. (this is what the standard strings does)
  * for byte sequence f[i]...f[i+n] check if it looks like a string if XOR is done with a single byte over it. 

This can be done in O(n) time so even large files can be quickly scanned.

Bonus ideas:
  * for byte sequence f[i]...f[i+n] check if it looks like a string of XOR is done with any of the previously found strings over it
  * recognize base64 and other common encodings (usually easy anyway if you print out the strings)
  * notice if something is clearly somehow encoded data, based on how it differs from code blocks. (Executable headers of course would also identify data segments, but we might not have those)
 
(After these it's no longer O(n) in the worst case, but it's likely still O(n) in almost every actual case.)

This code might be useful as a starting point: [XOR-guesser.py](src/XOR-guesser.py). ^ is the XOR function in Python.


# Task 3 

Brute force [Local File Inclusion](https://www.owasp.org/index.php/Testing_for_Local_File_Inclusion).

Every now and and then one needs to brute force something out of a web server. [dirb](https://tools.kali.org/web-applications/dirb), [dirbuster](https://tools.kali.org/web-applications/dirbuster) and [gobuster](https://github.com/OJ/gobuster) are fine for basic enumeration. [wfuzz](https://github.com/xmendez/wfuzz) is great. [ffuf](https://github.com/ffuf/ffuf) is superb!
[Burp Intruder](https://portswigger.net/burp/documentation/desktop/tools/intruder/using) is often an excellent choice.

But sometimes you need something custom made so let's make a brute forcer. (This can be easily converted into brute forcing logins or other things aside from LFI). The actual list 
of potentially interesting files depends on the target of course and there might be some limitations on directory traversal and some special encodings that need to be done.

Luckily for us, we already have identified a vulnerable endpoint we can try to exploit: (http://34.243.97.41/site.php?op=menu)

It seems that the parameter ```op``` can be exploited. Try this for a PoC: (http://34.243.97.41/site.php?op=../../../../../../etc/passwd)

Now, try to:

* Modify the template program to fetch files from the external server.
* Try to download interesting files from the server. SecLists can give you some ideas. Also, you could identify the operating system and services with [nmap](https://nmap.org/).
* If possible, try to separate "not found" from the "no access rights". Might not be possible.

Bonus ideas:
* Maintain a list of previous attempts and only try new files that haven't been tried already.
* Make a tester that can automatically test all common LFI vulns from a given HTTP parameter. See the awesome [High On Coffee LFI cheat sheet](https://highon.coffee/blog/lfi-cheat-sheet/) to get some ideas for this.

There is some code that might be useful as a starting point: (src/LFI-template.py)
The program actually downloads and writes the remote files to the current directory so careful here.

P.S. If you don't think LFI is dangerous, consider these: (https://www.rcesecurity.com/2017/08/from-lfi-to-rce-via-php-sessions/)


# Task 4

Remote exploit pwn.

There seems to be a chat server running and all you need is some TCP traffic to chat:

```
nc -v 34.243.97.41 8510
found 0 associations
found 1 connections:
     1:	flags=82<CONNECTED,PREFERRED>
     outif en10
     src 10.25.164.4 port 55900
     dst 34.243.97.41 port 8510
     rank info not available
     TCP aux info available

Connection to 34.243.97.41 port 8510 [tcp/*] succeeded!
     ___  ___ _____      _         _   
    | _ \/ _ \_   _|  __| |_  __ _| |_ 
    |   / (_) || |   / _| ' \/ _` |  _|
    |_|_\\___/ |_|   \__|_||_\__,_|\__|
<system> 2.0.218.106 connected
/nick putsi
hola amigos
<putsi> hola amigos
<lokori> hola putsi!
```

Fortunately (or unfortunately, depending on your point of view), this server has some serious bugs in it. It should be possible to exploit it, perhaps even get RCE out of it.

The task:
* Create a Python program that can act as a client to the chat server. There is some code already available: (src/pwn-backend/tcp-client.py)
* Try to crash the server by sending it some payload (classic is 'A' repeated n times).
* Try to make your client automatically reconnect if the server happens to crash.

Bonus:
* This sort of thing benefits from actual fuzzing. Try to integrate Radamsa to this. 


If you are interested, the compiled binary for the chat server is available: (pwn-backend/serverperver) . It may be useful for developing the exploit locally before trying it out on the remote server.

This is a Python workshop so it doesn't really matter if you can succesfully exploit the flaws and execute some shellcode, but the idea is to get a grasp how this might be done over a remote connection.

