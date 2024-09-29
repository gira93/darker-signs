from termcolor import cprint
from system.dns import Dns
from system.mail import Mail


class CrashmeCom:
    def __init__(self, root_path: str, mail: Mail, dns: Dns) -> None:
        self.root_path = root_path
        self.mail = mail
        self.dns = dns

    def crash80(self):
        for _ in range(500):
            cprint("CRASHME ", "red", end=None)
        cprint("Seg Fault in http client", "red")
