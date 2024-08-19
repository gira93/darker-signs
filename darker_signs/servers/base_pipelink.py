from termcolor import cprint
from darker_signs.mail import Mail
from darker_signs.dns import Dns


class BasePipelink:
    def __init__(self, root_path: str, mail: Mail, dns: Dns) -> None:
        self.root_path = root_path
        self.mail = mail
        self.dns = dns

    def sharedaccesspl(self):
        cprint("This is a private network", "red")
        cprint("Unauthorized access is forbidden", "red")
        cprint("Connection closed", "red")
        print()
