from termcolor import cprint
from .base_server import BaseServer


class BasePipelink(BaseServer):
    def sharedaccesspl(self):
        cprint("This is a private network", "red")
        cprint("Unauthorized access is forbidden", "red")
        cprint("Connection closed", "red")
        print()
