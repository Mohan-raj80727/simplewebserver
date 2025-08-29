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