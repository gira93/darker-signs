from termcolor import cprint
from .base_server import BaseServer


class PrxPostofficeMil(BaseServer):
    def prx91(self):
        while True:
            command = input("> ")
            if command == "getdb()":
                print()
                print("Server: db.postoffice.mil")
                print("Service: FCDB(FirstClass DataBase)")
                print()
                cprint("Connection closed", "red")
                break
            elif command == "exit":
                cprint("Connection closed", "red")
                break
            else:
                continue
