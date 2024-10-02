from termcolor import cprint
from .base_server import BaseServer


class CrashmeCom(BaseServer):
    def crash80(self):
        for _ in range(500):
            cprint("CRASHME ", "red", end=None)
        cprint("Seg Fault in http client", "red")
