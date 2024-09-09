from termcolor import cprint
from darker_signs.dns import Dns
from darker_signs.mail import Mail


class GoPhillyMil:
    def __init__(self, root_path: str, mail: Mail, dns: Dns) -> None:
        self.root_path = root_path
        self.mail = mail
        self.dns = dns

    def xftp25(self):
        print()
        cprint("Welcome to XFTP v1.0", "green")
        cprint("Check out xftp.com for more informations")
        print()
        user = 100
        while user == 100:
            command = input("> ")
            match command:
                case "login":
                    user = input("User: ")
                    pw = input("Pass: ")
                    if len(user) >= 36 or len(pw) >= 36:
                        user = 101
                        cprint("Seg fault in process xftp.exe", "red")
                        cprint("Process killed", "red")
                        print("Logged in as user xftp")
                    else:
                        cprint("Wrong User or Password", "red")
                        continue
                case "help":
                    print()
                    print("Available commands:")
                    print("login  help  exit")
                case "exit":
                    cprint("Connection closed", "red")
                    return
                case _:
                    continue
        while user == 101:
            command = input("> ")
            match command:
                case "run":
                    print("Specify an executable, eg. run <program>")
                    continue
                case "run xftp.exe":
                    user = 100
                    continue
                case "run xftp.exe --debug":
                    user = 0
                case "ls":
                    print("xftp.exe  init.conf")
                    continue
                case "help":
                    print("Available commands:")
                    print("run  ls  exit  help")
                    continue
                case "exit":
                    cprint("Connection closed", "red")
                    return
