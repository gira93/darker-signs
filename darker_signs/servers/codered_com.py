from time import sleep
from termcolor import cprint
from darker_signs.dns import Dns
from darker_signs.mail import Mail
from darker_signs.utils import download_file, upload_file, show_menu


class CoderedCom:
    def __init__(self, root_path: str, mail: Mail, dns: Dns) -> None:
        self.root_path = root_path
        self.mail = mail
        self.dns = dns

    def code80(self):
        cprint("Welcome to CodeRed.com", "green")
        cprint("Where the hosting is so cheap it's a CodeRED alert", "red")
        options = ["How Cheap?", "Sign up"]
        crashed = False
        remoteapp = False
        while True:
            selection = show_menu(options)
            match selection:
                case "1":
                    cprint("How cheap is hosting at CodeRed?", "red")
                    print()
                    rates = [
                        "Rates are as follows:",
                        "Monthly, $2.99, 500MB, 1GB bandwidth (each month)",
                        "Yearly, $9.99, 2GB, 5GB bandwidth (each month)",
                    ]
                    cprint("\n".join(rates), "green")
                    print()
                    input("Press a key")
                    continue
                case "2":
                    cprint(
                        "To sign up for hosting, send an email to sales@CodeRed.com",
                        "green",
                    )
                    print()
                    input("Press a key")
                    continue
                case "header::location::crashme.com":
                    print()
                    print("Redirecting ...")
                    sleep(2)
                    cprint("System Command Error", "red")
                    sleep(1)
                    cprint("Fatal error in JazzyWeb.exe", "red")
                    cprint("Returning to command prompt", "green")
                    crashed = True
                    break
                case _:
                    cprint("Connection closed", "red")
                    return
        while crashed:
            commands = [
                "ls",
                "run",
                "upload",
                "help",
                "exit",
            ]
            command = input("> ").split()
            com = command[0] if len(command) > 0 else ""
            param = command[1] if len(command) > 1 else ""
            match com:
                case "ls":
                    print()
                    if remoteapp:
                        print("remoteapp")
                    else:
                        print("NO FILES")
                    print()
                    continue
                case "run":
                    if param == "remoteapp" and remoteapp:
                        print("...")
                        sleep(2)
                        cprint("INFECTED", "red")
                        cprint("Connection closed", "red")
                        download_file(f"{self.root_path}/ddos_codered", "", False)
                        break
                    continue
                case "upload":
                    file = upload_file(f"{self.root_path}/{param}")
                    if file and param == "remoteapp":
                        remoteapp = True
                        cprint("File uploaded", "green")
                    else:
                        cprint("File not found in local", "red")
                    continue
                case "help":
                    print("Available commands")
                    print("  ".join(commands))
                    print()
                    continue
                case "exit":
                    cprint("Connection closed", "red")
                    break
                case _:
                    continue
