from termcolor import cprint
from system.utils import download_file, show_menu
from .base_server import BaseServer


class CrackertoolsCom(BaseServer):
    def cracker80(self):
        cprint("|\\-/|\\-/||\\-/|\\-/||\\-/|\\-/||\\-/|\\-/||\\-/|\\-/|", "green")
        cprint("|\\-/|             CrackerTools.com              |\\-/|", "green")
        cprint("|\\-/| The only place to get the latest and      |\\-/|", "green")
        cprint("|\\-/|             best cracker tools!           |\\-/|", "green")
        cprint("|\\-/|\\-/||\\-/|\\-/||\\-/|\\-/||\\-/|\\-/||\\-/|\\-/|", "green")
        options = ["Downloads", "Exploits", "Donate", "Links"]
        while True:
            selection = show_menu(options)
            match selection:
                case "1":
                    downloads = [
                        "BackDoor v2.0 [offline]",
                        "DoSer v3.1 [ONLINE]",
                        "PasswdCracker Jack v1.0 [offline]",
                        "Encrypt/Decrypt beta v0.3 [offline]",
                    ]
                    file = show_menu(downloads, abort_message="Back to main menu")
                    if file == "2":
                        download_file(f"{self.root_path}/remoteapp", "REMOTEDOSERv3.1")
                        readme1st = [
                            "Don't be an idiot and run remoteapp on your computer.",
                            "Upload and run remoteapp on targets.",
                            "To use DoSer visit doser.com",
                        ]
                        download_file(
                            f"{self.root_path}/readme1st", "\n".join(readme1st), False
                        )
                        cprint("Downloaded remoteapp and readme1st", "green")
                        continue
                    else:
                        continue
                case "2":
                    print()
                    cprint(
                        "For the lastest and greatest explits check out security.com",
                        "blue",
                    )
                    print()
                    input("Press a key")
                    continue
                case "3":
                    print()
                    print(
                        "Please send an email to donate@crackertools.com for details about donating"
                    )
                    print("Thank you")
                    print()
                    input("Press a key")
                    continue
                case "4":
                    print()
                    cprint("Recommended links", "green")
                    print()
                    print("hackme.com - Hack the server challenge!")
                    print("crashme.com - FUN FUN FUN")
                    print()
                    input("Press a key")
                    continue
                case _:
                    cprint("Connection closed", "red")
                    break
