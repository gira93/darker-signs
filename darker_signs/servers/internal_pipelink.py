from termcolor import cprint
from getpass import getuser
from darker_signs.dns import Dns
from darker_signs.mail import Mail


class InternalPipelink:
    def __init__(self, root_path: str, mail: Mail, dns: Dns) -> None:
        self.root_path = root_path
        self.mail = mail
        self.dns = dns

    def int9http(self):
        message = f"Newsletter Hi {getuser()},\n\nWe have finished upgrading our database and our website\nis now back up and running.\n\nThank you,\nBarry Simons\nFIND.com President"
        self.mail.add_message(
            from_user="find.com", subject="Newsletter", message=message
        )
        cprint("Access Denied\nConnection Closed", "red")

    def int9secure(self):
        cprint("Access Denied\nConnection Closed", "red")

    def int9priv(self):
        cprint("Access Denied\nConnection Closed", "red")
