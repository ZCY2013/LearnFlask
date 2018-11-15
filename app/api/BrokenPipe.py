from flask import current_app, make_response
from app.api import api
import  httplib
import time

@api.route("/brokenpipe")
def brokenpipe():
    headers = {"Content-type":"application/json", "Accept":"application/json"}
    http_client = httplib.HTTPConnection(host='localhost', port=8080, timeout=30)
    http_client.request(method="GET", url="/timeout")
    http_client.getresponse()
    http_client.getresponse()


@api.route("/timeout")
def timeout():
    time.sleep(2)
    return "OK"
