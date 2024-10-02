from termcolor import cprint
from system.utils import download_file, show_menu
from .base_server import BaseServer


class Intserv09PipelinkGov(BaseServer):
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
