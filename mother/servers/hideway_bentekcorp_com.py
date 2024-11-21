from .base_server import BaseServer


class HidewayBentekcorpCom(BaseServer):
    def http(self):
        self.gateway_server()
