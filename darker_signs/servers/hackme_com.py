from time import sleep
from termcolor import cprint
from darker_signs.dns import Dns
from darker_signs.mail import Mail
from darker_signs.utils import download_file, show_menu, upload_file


class HackmeCom:
    def __init__(self, root_path: str, mail: Mail, dns: Dns) -> None:
        self.root_path = root_path
        self.mail = mail
        self.dns = dns

    def hack80(self):
        cprint("HackMe.com - That's right, HACKME", "red")
        print()
        options = ["How it works", "Start hacking"]
        while True:
            selection = show_menu(options)
            match selection:
                case "1":
                    print()
                    cprint("How HackMe.com Works", "red")
                    print()
                    instructions = [
                        "The aim of HackMe.com is to hack the website server.",
                        "It's a series of challenges and a little reward at the end.",
                        "Some rules for this:",
                        "- Respect the server and don't damage it in any way",
                        "- No DoS attacks are allowed to be launched from this server",
                        "- No bounces or proxies from this server",
                        "- We will cooperate with the law",
                    ]
                    cprint("\n".join(instructions), "blue")
                    print()
                    input("Press a key")
                    continue
                case "2":
                    break
                case _:
                    cprint("Connection closed", "red")
                    return
        self.__start_hack()

    def __start_hack(self):
        user = "level1"
        commands = [
            "ls",
            "cat",
            "cwd",
            "whoami",
            "run",
            "get",
            "upload",
            "help",
            "exit",
        ]
        ls_level1 = ["hello.exe"]
        ls_level2 = ["xftp.exe"]
        ls_admin = ["links"]
        remoteapp = False
        hello_content = [
            "if pass == 'ijusthackedyou':",
            "  return True",
            "else:",
            "  print('Wrong password!')",
        ]
        links_content = [
            "Here's your prize! Have FUN!",
            "",
            "telnet.pokemonworld.com",
            "telnet.globalsport.com",
            "ftp.willowfootball.org",
            "media.net",
            "ftp.stlukes.christ.org",
            "ftp.blindballet.org",
            "telnet.happyhackers.net",
            "codered.com",
        ]
        print()
        cprint(
            'You will be dropped into a command line as user "level1"\nLook around and good luck!'
        )
        print()
        while True:
            ps1 = "#> " if user == "admin" else "> "
            command = input(ps1).split()
            com = command[0] if len(command) > 0 else ""
            param = command[1] if len(command) > 1 else ""
            match com:
                case "ls":
                    print()
                    if user == "level1":
                        print("  ".join(ls_level1))
                    elif user == "level2":
                        print("  ".join(ls_level2))
                    elif user == "admin":
                        print("  ".join(ls_admin))
                        if remoteapp:
                            print("remoteapp")
                    print()
                    continue
                case "cat":
                    if user == "level1" and param == "hello.exe":
                        print()
                        print("\n".join(hello_content))
                        print()
                    elif user == "admin" and param == "links":
                        print()
                        print("\n".join(links_content))
                        print()
                    else:
                        print("File not found or unreadable")
                        print()
                    continue
                case "cwd":
                    print(f"/home/{user}")
                    continue
                case "whoami":
                    print(user)
                    continue
                case "run":
                    if user == "level1" and param == "hello.exe":
                        pw = input("Enter password: ")
                        if pw == "ijusthackedyou":
                            cprint("Password correct", "green")
                            cprint("Logged in as user level2", "green")
                            user = "level2"
                        else:
                            cprint("Wrong password!", "red")
                    if user == "level2" and param == "xftp.exe":
                        if len(command) >= 3 and command[2] == "--debug":
                            cprint("Running XFTP in debug mode", "green")
                            cprint("You are admin", "green")
                            user = "admin"
                        else:
                            cprint("Restarting xftp\nPlease relogin", "green")
                            cprint("Disconnecting", "red")
                            return
                    if user == "admin" and param == "remoteapp" and remoteapp:
                        print("...")
                        sleep(2)
                        cprint("INFECTED", "red")
                        cprint("Connection closed", "red")
                        download_file(f"{self.root_path}/system/ddos_hackme", "", False)
                        return
                    continue
                case "get":
                    if user == "level1" and param == "hello.exe":
                        download_file(
                            f"{self.root_path}/hello.exe", "\n".join(hello_content)
                        )
                    if user == "admin" and param == "links":
                        download_file(
                            f"{self.root_path}/links", "\n".join(links_content)
                        )
                    continue
                case "upload":
                    if user == "admin":
                        file = upload_file(f"{self.root_path}/{param}")
                        if file and param == "remoteapp":
                            remoteapp = True
                            cprint("File uploaded", "green")
                        else:
                            cprint("File not found in local", "red")
                    else:
                        cprint("You don't have permissions to upload files", "red")
                    continue
                case "help":
                    print("Available commands")
                    print("  ".join(commands))
                    print()
                    continue
                case "exit":
                    cprint("Connection closed", "red")
                    return
                case _:
                    continue
