from termcolor import cprint
from system.dns import Dns
from system.mail import Mail


class NewputeCom:
    def __init__(self, root_path: str, mail: Mail, dns: Dns) -> None:
        self.root_path = root_path
        self.mail = mail
        self.dns = dns

    def npbbs(self):
        print()
        cprint("--------------------", "red")
        cprint("HACKED BY THC GROUP", "green")
        cprint("--------------------", "red")
        print()
