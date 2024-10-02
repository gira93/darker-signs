from termcolor import cprint
from getpass import getuser
from .base_server import BaseServer


class InternalPipelink(BaseServer):
    def int9http(self):
        message = f"Hi {getuser()},\n\nWe have finished upgrading our database and our website\nis now back up and running.\n\nThank you,\nBarry Simons\nFIND.com President"
        self.mail.add_message(
            from_user="find.com", subject="Newsletter", message=message
        )
        cprint("Access Denied\nConnection Closed", "red")

    def int9secure(self):
        cprint("Access Denied\nConnection Closed", "red")

    def int9priv(self):
        cprint("Access Denied\nConnection Closed", "red")
