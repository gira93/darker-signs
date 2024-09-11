from time import sleep
from termcolor import cprint
from darker_signs.dns import Dns
from darker_signs.mail import Mail
from darker_signs.utils import download_file, upload_file


class CoderedCom:
    def __init__(self, root_path: str, mail: Mail, dns: Dns) -> None:
        self.root_path = root_path
        self.mail = mail
        self.dns = dns

    def code80(self):
        cprint("Welcome to CodeRed.com", "green")
        cprint("Where the hosting is so cheap it's a CodeRED alert", "red")
