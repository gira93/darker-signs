import os
from termcolor import cprint
from system.dns import Dns
from system.mail import Mail
from system.utils import show_menu


class FbiGov:
    def __init__(self, root_path: str, mail: Mail, dns: Dns) -> None:
        self.root_path = root_path
        self.mail = mail
        self.dns = dns

    def fbi25(self):
        dosed = os.path.isfile(f"{self.root_path}/system/down_fbi.gov")
        if dosed:
            cprint("Connection terminated", "red")
            cprint("Error: remote host unable to load mail", "red")
            cprint("Pleaase email the admin with the above error message", "red")
        else:
            cprint(
                "This is a government server, any attempt to gain illegal access\nwill be punished",
                "blue",
            )
            print()
            input("Username: ")
            input("Password: ")
            cprint("Username/Password Error", "red")
            cprint("Disconnecting", "red")

    def fbi80(self):
        dosed = os.path.isfile(f"{self.root_path}/system/down_fbi.gov")
        if dosed:
            cprint("Connection terminated", "red")
            cprint("Error: remote host unable to load web script", "red")
            cprint("Pleaase email the admin with the above error message", "red")
        else:
            cprint("FBI Public Relations Access Website", "green")
            options = ["FBI 10 Most Wanted", "Your local FBI Office"]
            while True:
                selection = show_menu(options)
                match selection:
                    case "1":
                        cprint("--- FBI 10 Most Wanted ---")
                        top_10 = [
                            "Osma Ben Ledin",
                            "Robert Nilgate",
                            "Joe Filler",
                            "Marco Heli",
                            "Yesu Junkie",
                            "Eric Webb",
                            "Richard Lokie",
                            "Michael Brown",
                            "Stewart Blake",
                        ]
                        print()
                        print("\n".join(top_10))
                        print()
                        input("Press a key")
                        continue
                    case "2":
                        cprint(
                            "To find your local FBI office please consult\na normal phonebook"
                        )
                        print()
                        input("Press a key")
                        continue
                    case _:
                        cprint("Connection closed", "red")
                        break
