from HTTPserver import conf

from http.server import BaseHTTPRequestHandler, HTTPServer
from HTTPserver import pathHandler
import Resources.Plugin as plugin
from urllib.parse import urlparse



class HTTPServer_RequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        pathHandler.handler_Path(self)

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        if (self.headers['Content-Type'] == "application/json"):
            query = urlparse(self.path).query
            print(self.path)
            root = (self.path.replace('?'+query,'')).split("/")
            print(root,query)
            if not query:
                res_msg = "The request could not understood dut to invalid syntax"
                res_code = 400
            else:
                #rawJson = self.rfile.read(content_length)
                #plugin.update_resource((root,query), rawJson)
                res_msg = "OK"
                res_code = 200
        else:
            res_code = 415
            res_msg = "Json is the only Content-Type accepted"

        self.send_response(res_code)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(bytes(res_msg, "utf8"))

def run():
    pathHandler.add_Path("/", pathHandler.GET_MainPage)
    pathHandler.add_Path("/sensors.js", pathHandler.GET_DataScript)
    pathHandler.add_Path("/style.css", pathHandler.GET_StyleSheet)
    pathHandler.add_Path("/resources", pathHandler.GET_Resources)

    print('Server start up')
    server_address = (conf.IP, conf.PORT)
    httpd = HTTPServer(server_address, HTTPServer_RequestHandler)
    print(f'Server running at {httpd.server_address}')
    httpd.serve_forever()


run()
