from flask import current_app, make_response
from app.api import api
import httplib
import time


@api.route("/brokenpipe")
def brokenpipe():
    current_app.logger.info("broken pip in")
    headers = {"Content-type":"application/json", "Accept":"application/json"}
    http_client = httplib.HTTPConnection(host='localhost', port=8080, timeout=30)
    http_client.request(method="GET", url="/LEARN_FLASK/normal")
    response = http_client.getresponse()
    print(response)
    # http_client.request(method="GET", url="/LEARN_FLASK/timeout")
    # res = http_client.getresponse()
    # print(res)

    return "SUCCESS"


@api.route("/timeout")
def timeout():
    time.sleep(2)
    return "OK"


@api.route("/normal")
def normal():
    return "NORMAL RESPONSE"
