### Hypertext Transfer Protocol (HTTP)
- socket is a module in python that lets you make network connections and retrieve data over sockets.
- A socket is a two-way connection between two programs. You can both send and receive data over a socket. If you try to read from a socket that has no data, your program will sit and wait until data arrives.
- A protocol is a set of rules that determine who goes first, what to do, and what the responses should be and who sends it next. The rules of communication essentially.
- One example of a protocol is the HTTP protocol.
- To request a document from a web server, you makes a connection to a server on port 80 and then send a request `GET url HTTP/1.0` and then a blank line. The server responds with a status line, a blank line, and the document.
```python
import socket
# Type of socket and prot
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connect to the server
mysock.connect(('url', 80))
# Creates the request
cmd = 'GET url HTTP/1.0\r\n\r\n'.encode()
# Sends the request
mysock.send(cmd)
while True:
    # Receives the data
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    # Decodes the data and prints it
    print(data.decode(), end='')
# Closes the connection
mysock.close()
```
- Using b'' notation, you can store the variable as bytes instead of a string. encode() and b'' are equivalent.
- sendall() is a method that sends all the data in one shot. It is more efficient than sending the data in chunks.
- When you use recv(), you get as many characters as have been recieved up to the number specified in the parenthesis. Results may vary depending on network speed.
- You need to sleep for a bit after you send the request to give the server time to respond.

### Retrieving Data with urllib
- urllib is a simpler way to retrieve data from a web page. It treats the web page as a file and retrieves the data in the same way you would read a file.
```python
import urllib.request

fhand = urllib.request.urlopen('url')
for line in fhand:
    print(line.decode().strip())
```
- urllib consumes the header and only returns the data.
- To read binary files, you should use the read() command to store all the data as a string to parse later.
- read() only works if the data is smaller than the memory of the computer.
- Read in blocks if the data is large. You can give read() a number to read a certain amount of characters.
- The ssl library allows this program to access web sites that strictly use https.

### Parsing HTML with BeautifulSoup
- BeautifulSoup tolerates highly flawed HTML and still parses it.
- BeautifulSoup(url, 'html.parser') parses the url and returns a BeautifulSoup object.
- Giving a tag in the BeautifulSoup object returns a list of all the tags with that name.

### Linux
- There is a curl command that can be used to retrieve data over HTTP or File Transfer (FTP) protocols. Curl stands for copy URL.
- wget is a similar command.

### Glossary
- port: A number that indicates which application you are contacting.
- scrape: Pretend to be a browser and retrieve data from a web server to look through the content.
- socket: A two-way connection between two programs.
- spider: The act of a web search engine retrieving web pages and then all the pages linked to those pages until they have retrieved the entire web to build an index.