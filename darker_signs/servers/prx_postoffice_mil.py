from termcolor import cprint
from darker_signs.dns import Dns
from darker_signs.mail import Mail


class PrxPostofficeMil:
    def __init__(self, root_path: str, mail: Mail, dns: Dns) -> None:
        self.root_path = root_path
        self.mail = mail
        self.dns = dns

    def prx91(self):
        while True:
            command = input("> ")
            if command == "getdb()":
                print()
                print("Server: db.postoffice.mil")
                print("Service: FCDB(FirstClass DataBase")
                print()
                cprint("Connection closed", "red")
                break
            elif command == "exit":
                cprint("Connection closed", "red")
                break
            else:
                continue
