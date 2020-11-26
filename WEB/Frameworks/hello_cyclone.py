"""
Cyclone is a web server framework for Python, that implements the Tornado API as a Twisted protocol.
http://cyclone.io/
"""

import cyclone.web
import sys

from twisted.internet import reactor
from twisted.python import log


class MainHandler(cyclone.web.RequestHandler):
    def get(self):
        self.write("Hello, world")


if __name__ == "__main__":
    application = cyclone.web.Application([(r"/", MainHandler)])

    log.startLogging(sys.stdout)
    reactor.listenTCP(8888, application, interface="127.0.0.1")
    reactor.run()
