from termcolor import cprint
from .base_server import BaseServer


class SpecialstorageCom(BaseServer):
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
