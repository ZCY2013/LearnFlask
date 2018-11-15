# -*- coding: utf-8 -*-
# @Info: Entry

import os
from datetime import datetime

from app import create_app
from flask_script import Manager, Server
import sys
#
# reload(sys)
# sys.setdefaultencoding('utf-8')

app = create_app('default')

manager = Manager(app)
manager.add_command('runserver', Server(host='0.0.0.0', port=8080))


def make_shell_context():
    return dict(app=app)


@app.route('/')
def hello():
    app.logger.info("Hello World")
    project_name = "Learn Flask Project"
    return '<br>Hello ! </br> <br>' + project_name + '</br> <br>HERE ! </br>' + str(datetime.now())


if __name__ == '__main__':
    project_name = "Learn Flask Proj"
    app.logger.info('## [Main][Service] ' + project_name + '[START]###')
    port = 8080
    manager.run()