from termcolor import cprint
from system.dns import Dns
from system.mail import Mail


class SpecialserverCom:
    def __init__(self, root_path: str, mail: Mail, dns: Dns) -> None:
        self.root_path = root_path
        self.mail = mail
        self.dns = dns

    def special80(self):
        cprint("You are getting to know things here", "green")
        cprint("-MicMast-", "green")
        cprint("Bye Bye", "red")
