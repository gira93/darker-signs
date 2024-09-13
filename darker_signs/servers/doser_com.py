import os
from time import sleep
from termcolor import cprint
from darker_signs.dns import Dns
from darker_signs.mail import Mail
from darker_signs.utils import progress_bar, show_menu

DDOS_SERVERS = 9


class DoserCom:
    def __init__(self, root_path: str, mail: Mail, dns: Dns) -> None:
        self.root_path = root_path
        self.mail = mail
        self.dns = dns

    def dos80(self):
        cprint("Welcome to DoSer v3.1", "green")
        print()
        selection = input("Connect to infected servers? (y/n) ").lower()
        if selection == "y":
            self.__start_ddos()
        else:
            cprint("Connection closed, bye", "red")
            return

    def __start_ddos(self):
        print()
        cprint("Connecting to servers...", "yellow")
        sleep(2)
        _, _, files = next(os.walk(self.root_path))
        ddos_files = list(filter(lambda f: f.startswith("ddos_"), files))
        if len(ddos_files) == DDOS_SERVERS:
            progress_bar()
            cprint("Connected to servers", "green")
            cprint("DDoS armed and READY", "green")
            print()
        else:
            print()
            cprint("Not enough servers for a DDoS attack", "red")
            cprint("Exiting", "red")
            return
