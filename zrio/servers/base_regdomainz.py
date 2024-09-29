from termcolor import cprint
from system.dns import Dns
from system.mail import Mail


class BaseRegdomainz:
    def __init__(self, root_path: str, mail: Mail, dns: Dns) -> None:
        self.root_path = root_path
        self.mail = mail
        self.dns = dns

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
