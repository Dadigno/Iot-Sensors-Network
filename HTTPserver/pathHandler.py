import  Resources.Plugin as plugin
pathList = []



def handler_Path(req):
    if not ([t[1](req) for t in pathList if t[0] == req.path]):
        req.send_response(404)
        req.end_headers()

def add_Path(path, func):
    pathList.append((path, func))

def GET_MainPage(req):
    s = open("../WebPages/index.html")
    res_body = s.read()
    req.send_response(200)
    req.send_header('Content-type', 'text/html')
    req.end_headers()
    resp_msg = res_body
    req.wfile.write(bytes(resp_msg, "utf8"))

def GET_DataScript(req):
    s = open("../WebPages/sensors.js")
    res_body = s.read()
    req.send_response(200)
    req.send_header('Content-type', 'application/javascript')
    req.end_headers()
    resp_msg = res_body
    req.wfile.write(bytes(resp_msg, "utf8"))

def GET_StyleSheet(req):
    s = open("../WebPages/style.css")
    res_body = s.read()
    req.send_response(200)
    req.send_header('Content-type', 'text/css')
    req.end_headers()
    resp_msg = res_body
    req.wfile.write(bytes(resp_msg, "utf8"))


def  GET_Resources(req):
    req.send_response(200)
    req.send_header('Content-type', 'application/json')
    req.end_headers()
    resp_msg = plugin.read_resources()
    req.wfile.write(bytes(resp_msg, "utf8"))


