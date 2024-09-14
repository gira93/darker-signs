from termcolor import cprint
from darker_signs.dns import Dns
from darker_signs.mail import Mail


class SpecialserverCom:
    def __init__(self, root_path: str, mail: Mail, dns: Dns) -> None:
        self.root_path = root_path
        self.mail = mail
        self.dns = dns

    def special80(self):
        cprint("You are getting to know things here", "green")
        cprint("-MicMast-", "green")
        cprint("Bye Bye", "red")
