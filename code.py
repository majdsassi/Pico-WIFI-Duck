import socketpool
import wifi
from duck import exe
from adafruit_httpserver import Server, Request, JSONResponse ,POST , Response
"""--------------------------------------------------------------------------------------"""
ssid = "Pico WIFI DUCK"
password = "pico123456"
"""--------------------------------------------------------------------------------------"""
print("Creating access point", ssid)
wifi.radio.stop_station()
wifi.radio.start_ap(ssid, password)
print("Access point created!")
pool = socketpool.SocketPool(wifi.radio)
server = Server(pool, "/static", debug=True)
"""--------------------------------------------------------------------------------------"""
@server.route("/")
def base(request: Request):
    with open("index.html", "r") as file:
        html_content = file.read()
    headers = {"Content-Type": "text/html"}
    return Response(request, html_content, headers=headers)
"""--------------------------------------------------------------------------------------"""
@server.route("/api", POST,append_slash=True)
def api(request: Request):
    if request.method == POST :
        req = request.json()
        payload = req["content"]
        payload = payload.splitlines()
        exe(payload)
        return JSONResponse(request, {"message": "Done"})
server.serve_forever('192.168.4.1', 80)
