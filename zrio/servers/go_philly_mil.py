from termcolor import cprint
from system.dns import Dns
from system.mail import Mail
from system.utils import download_file


class GoPhillyMil:
    def __init__(self, root_path: str, mail: Mail, dns: Dns) -> None:
        self.root_path = root_path
        self.mail = mail
        self.dns = dns

    def xftp25(self):
        cprint("Welcome to XFTP v1.0", "green")
        cprint("Check out xftp.com for more informations")
        print()
        user = 100
        server_running = True
        while user == 100:
            command = input("> ")
            match command:
                case "login":
                    user = input("User: ")
                    pw = input("Pass: ")
                    if len(user) >= 36 or len(pw) >= 36:
                        user = 101
                        server_running = False
                        cprint("Segmentation fault in process xftp.exe", "red")
                        cprint("Process killed", "red")
                        print("Logged in as user xftp")
                        break
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
                    cprint("XFTP server started, please reconnect", "green")
                    server_running = True
                    continue
                case "run xftp.exe --debug":
                    if not server_running:
                        user = 0
                        break
                    else:
                        cprint("XFTP is already running, please close it first", "red")
                        continue
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
                case _:
                    continue
        while user == 0:
            command = input("#> ")
            match command:
                case "run":
                    print("Specify an executable, eg. run <program>")
                    continue
                case "ls":
                    print("cryptsetup.exe  user.txt  notes.txt")
                    continue
                case "get":
                    print("Specify a filename, eg. get <filename>")
                    continue
                case "get cryptsetup.exe":
                    download_file(f"{self.root_path}/cryptsetup.exe", "CRYPTFNEC")
                    cprint("cryptsetup.exe donloaded", "green")
                    continue
                case "get user.txt":
                    download_file(
                        f"{self.root_path}/user.txt",
                        "guest::/home/guest\nxftp::/home/xftp\nroot::/root",
                    )
                    cprint("user.txt downloaded", "green")
                    continue
                case "get notes.txt":
                    download_file(
                        f"{self.root_path}/notes.txt",
                        "Remember to update XFTP.\nMove crypting software somewhere else.",
                    )
                    cprint("notes.txt downloaded", "green")
                    continue
                case "help":
                    print("Available commands:")
                    print("run  ls  get  exit  help")
                    continue
                case "exit":
                    cprint("Connection closed", "red")
                    return
                case _:
                    continue
