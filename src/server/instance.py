from flask import Flask
from flask_restplus import Api


class Server:
    def __init__(self, host='0.0.0.0', port=8080, debug=True):
        self.host = host
        self.port = port
        self.debug = debug
        self.app = Flask(__name__)
        self.api = Api(
            self.app,
            version='1.0.0',
            title='Sample Book api',
            description='A simple book API',
            doc='/docs'
        )
    def run(self,):
        self.app.run(
            host=self.host,
            port=self.port,
            debug=self.debug
        )

server = Server()