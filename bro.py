from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<!DOCTYPE html>
<html>
 <head>
      table
    </head>
    <body>
        <h1 align="center">SUJAL DAS-25013553 </h1>
        <table border="4" align="center" cellpadding="35">
        <tr>
            <th>S.NO</th>
            <th>DEVICE SPECIFICATION</th>
            <th>DESCRIPTION</th>
        </tr>
        <tr>
            <td>1</td>
            <td>Device Name</td>
            <td>SUJAL</td>
        </tr>
        <tr>
            <td>2</td>
            <td>Storage</td>
            <td>477 GB</td>
         </tr>   
        <tr>
            <td>3</td>
            <td>Graphics Card</td>
            <td>128 MB</td>
        </tr>
        <tr>
            <td>4</td>
            <td>Installed Ram</td>
            <td>16 GB</td>
        </tr>
        <tr>
            <td>5</td>
            <td>Processor</td>
            <td>Intel-corei7-13620H</td>
        </tr>
    </table>
    </body>


</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()