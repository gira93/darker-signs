from termcolor import cprint
from darker_signs.dns import Dns
from darker_signs.mail import Mail
from darker_signs.utils import download_file, show_menu


class Intserv09PipelinkGov:
    def __init__(self, root_path: str, mail: Mail, dns: Dns) -> None:
        self.root_path = root_path
        self.mail = mail
        self.dns = dns

    def sharedaccespl(self):
        cprint("This is a private server", "red")
        cprint("Error accessing auth file", "red")
        cprint("File Database", "blue")
        options = ["8m.enc (broken)", "9m.enc (broken)", "10m.enc"]
        while True:
            selection = show_menu(options)
            if selection != "3":
                cprint("Connection closed", "red")
                break
            if selection == "3":
                print("Downloading 10m.enc")
                download_file(
                    f"{self.root_path}/10m.enc",
                    contents="SJHDKMSGKAGMSKVGASMAGVNSFVZJK",
                )
                cprint("Download complete", "green")
                break
