import os
from ipaddress import AddressValueError, IPv4Address
from termcolor import cprint

from darker_signs.utils import progress_bar
from ..mail import Mail
from ..dns import Dns


class ScanCom:
    def __init__(self, root_path: str, mail: Mail, dns: Dns) -> None:
        self.root_path = root_path
        self.mail = mail
        self.dns = dns

    def q(self):
        cprint("//////////////////", "light_red")
        cprint("///// QUAERO /////", "light_red")
        cprint("//////////////////", "light_red")
        print("Ip Scanning tool")
        while True:
            start = input("Enter start IP address: ")
            end = input("Enter end IP address: ")
            try:
                start = IPv4Address(start)
                end = IPv4Address(end)
                if start >= end:
                    raise AddressValueError
            except AddressValueError:
                print("Invalid addresses specified")
                return
            file = input("Save result to file (type a name): ")
            if file == "":
                cprint("No file specified", "red")
                return
            break
        os.system("cls||clear")
        current = start
        print()
        with open(f"{self.root_path}/{file}", "w") as f:
            while current <= end:
                if self.dns.find(str(current)):
                    f.write(f"{current}\n")
                current += 1
            progress_bar(step=0.3)
        print()
        cprint(f"Scan completed to file {file}", "green")
        print("Disconnected by server")
