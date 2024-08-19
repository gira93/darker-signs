from darker_signs.dns import Dns
from darker_signs.mail import Mail


class ResearchBiolabsNet:
    def __init__(self, root_path: str, mail: Mail, dns: Dns) -> None:
        self.root_path = root_path
        self.mail = mail
        self.dns = dns

    def biolabsresearchhttp(self):
        pass
