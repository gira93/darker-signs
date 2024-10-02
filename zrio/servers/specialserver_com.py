from termcolor import cprint
from .base_server import BaseServer


class SpecialserverCom(BaseServer):
    def special80(self):
        cprint("You are getting to know things here", "green")
        cprint("-MicMast-", "green")
        cprint("Bye Bye", "red")
