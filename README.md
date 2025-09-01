# EX01 Developing a Simple Webserver
## Date:29/08/25
## REG NO:212224100036
## Developed by :Mohanraj.s

## AIM:
To develop a simple webserver to serve html pages and display the list of protocols in TCP/IP Protocol Suite.

## DESIGN STEPS:
### Step 1: 
HTML content creation.

### Step 2:
Design of webserver workflow.

### Step 3:
Implementation using Python code.

### Step 4:
Import the necessary modules.

### Step 5:
Define a custom request handler.

### Step 6:
Start an HTTP server on a specific port.

### Step 7:
Run the Python script to serve web pages.

### Step 8:
Serve the HTML pages.

### Step 9:
Start the server script and check for errors.

### Step 10:
Open a browser and navigate to http://127.0.0.1:8000 (or the assigned port).

## PROGRAM:
~~~
from http.server import HTTPServer, BaseHTTPRequestHandler

content = '''
<html>
    <head>
        <body bgcolor="orange">
            <h1 align="center" >PROTOCOL</h1>
            <table border="10" align="center" cellpadding="10" bgcolor="white">
                <tr bgcolor="yellow">
                    <th>S.No</th>
                    <th>Name of the Layer</th>
                    <th>Name of the protocol</th>
                </tr>
                <tr>
                    <td>1</td>
                    <td>Application Layer</td>
                    <td>HTTP,FTP,DNS,Telnet,SSII</td>
                </tr>
                <tr>
                    <td>2</td>
                    <td>Transpot Layer</td>
                    <td>IPV4/IPV6</td>
                </tr>
                <tr>
                    <td>3</td>
                    <td>Network Layer</td>
                    <td>Ethernet</td>
                </tr>
                <tr>
                    <td>3</td>
                    <td>Link Layer</td>
                    <td>TCP & UDP</td>
                </tr>
            </table>
        </body>
    </head>
</html>
'''

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Get request received...")
        self.send_response(200) 
        self.send_header("content-type", "text/html")       
        self.end_headers()
        self.wfile.write(content.encode())

print("This is my webserver") 
server_address =('',8000)
httpd = HTTPServer(server_address,MyServer)
httpd.serve_forever()
~~~


## OUTPUT:
<img width="1745" height="472" alt="Screenshot 2025-08-29 092225" src="https://github.com/user-attachments/assets/24a8f9cc-fa95-4821-a74b-49d634df29bd" />


## RESULT:
The program for implementing simple webserver is executed successfully.
