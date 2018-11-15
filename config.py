
import logging
import os
from flask import current_app
import base64

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    PROJECT_NAME = 'LEARN FLASK'
    APP_PRJNAM = PROJECT_NAME
    LEVEL = 'DEBUG'

    @staticmethod
    def init_app(app):
        pass


config = {
    'default':Config
}