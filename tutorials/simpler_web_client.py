import urllib.request

fhand = urllib.request.urlopen("http://127.0.0.1:9000/romeo.txt")
for line in fhand:
    print(line.decode().strip())

# simple sever get request 
# will be accessing the server 
# Access http://localhost:9000
# Get http://127.0.0.1/romeo.txt HTTP/1.0