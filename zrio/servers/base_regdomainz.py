from termcolor import cprint
from .base_server import BaseServer


class BaseRegdomainz(BaseServer):
    def xnullrd(self):
        print()
        print("Null connection")
        while True:
            command = input("Enter Input (type exit to cancel)")
            if command == "exit":
                break
            if command != "":
                cprint("Unauthorized user\nDisconnecting", "red")
                print()
                break
