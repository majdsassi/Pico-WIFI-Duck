import socketpool
import wifi
from adafruit_httpserver import Server, Request, Response
from duck import exe
from urllib import url_decode

ssid = "Pico WIFI DUCK"
password = "pico123456"

print("Creating access point", ssid)
wifi.radio.stop_station()
wifi.radio.start_ap(ssid, password)
print("Access point created!")

pool = socketpool.SocketPool(wifi.radio)
server = Server(pool, "/static", debug=True)


@server.route("/")
def base(request: Request):
    """
    Serve an HTML file as the response.
    """
    with open("index.html", "r") as file:
        html_content = file.read()
    headers = {"Content-Type": "text/html"}
    return Response(request, html_content, headers=headers)


@server.route("/decode", methods=["POST"])
def decode(request: Request):
    """
    Handle decoding request and print the decoded string.
    """
    content_start = request.body.find(b"content=") + len("content=")
    content_end = request.body.find(b"&", content_start)
    file_content = request.body[content_start:content_end].decode()
    #decoded_string = file_content.replace('%0D%0A', '\r\n').replace('+', ' ').replace("%0D%0","\n").replace("%27","'").replace("%2F","/").replace("%3A",":")
    decoded_string = url_decode(file_content).replace("+"," ")
    print(decoded_string)
    a = decoded_string.splitlines()
    print(a)
    exe(a)
    return Response(request, "Command Started.")


server.serve_forever('192.168.4.1', 80)
