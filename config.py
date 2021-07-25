import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or\
        b'\xf2\x95\xa2\xfe\xfcQ\xf44j\xca\xf2t\xa0\x9a<\xf8'
