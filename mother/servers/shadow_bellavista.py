from .base_server import BaseServer


class ShadowBellavista(BaseServer):
    def http(self):
        self.gateway_server()
