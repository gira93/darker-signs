from termcolor import cprint
from system.dns import Dns
from system.mail import Mail


class SpecialstorageCom:
    def __init__(self, root_path: str, mail: Mail, dns: Dns) -> None:
        self.root_path = root_path
        self.mail = mail
        self.dns = dns

    def specialstorage(self):
        print()
        print("Welcome, log in first")
        user = input("User: ")
        pw = input("Password: ")
        if user == "micmast" and pw == "urgettingsomewhere":
            cprint("Logged in successfully", "green")
            print()
            print(
                "This is your public server, upload and download from your private one!"
            )
            print(
                "----------------------------------------------------------------------"
            )
            print()
        cprint("Disconnected", "red")
