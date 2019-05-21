import json

from flask import current_app, make_response, request
from app.api import api
import httplib
import time

from app.models.A import A


@api.route('test_thread_safe', methods=['POST'])
def thread_safe_test():
    xml_data = request.get_json(force=True)
    current_app.logger.debug("xml_data:{}".format(xml_data))
    json_data = json.loads(xml_data)
    a = A(json_data)
    current_app.logger.info(a)
    return 'success'

