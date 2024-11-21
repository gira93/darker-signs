from .base_server import BaseServer


class HideSanandreashubsCom(BaseServer):
    def http(self):
        self.gateway_server()
