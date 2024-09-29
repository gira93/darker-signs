from termcolor import cprint
from system.dns import Dns
from system.mail import Mail
from system.utils import show_menu


class MicmastCom:
    def __init__(self, root_path: str, mail: Mail, dns: Dns) -> None:
        self.root_path = root_path
        self.mail = mail
        self.dns = dns

    def webmail(self):
        cprint("Micmast Webserver", "yellow")
        print()
        logged = False
        while True:
            command = input(":> ")
            match command:
                case "help":
                    print("Avaialble commands:")
                    print("login, exit")
                    print()
                case "login":
                    user = input("Username: ")
                    pw = input("Password: ")
                    if user == "root" and pw == "root":
                        logged = True
                        cprint("Logged in as root", "green")
                        print()
                        break
                    else:
                        cprint("Wrong username or password\nDisconnecting", "red")
                        return
                case "exit":
                    return
        while logged:
            options = [
                "Confirmation Mail Required",
                "Confirmation received. Access Granted",
            ]
            print("Welcome, you have 2 mail(s)")
            print("-----------------------------------------")
            selection = show_menu(options)
            print("-----------------------------------------")
            match selection:
                case "1":
                    print()
                    print("Confirmation required to access the secret network.")
                    print("Click on the link below!")
                    print("specialstorage.com")
                    print()
                    input("Press a key")
                    continue
                case "2":
                    print()
                    print("Account approved")
                    print("Username: micmast")
                    print("Password: urgettingsomewhere")
                    print()
                    input("Press a key")
                    continue
                case _:
                    logged = False
                    return

    def website(self):
        cprint("This is my personal homepage\nCurrently empty!", "yellow")
        print()
        input("Press a key")
