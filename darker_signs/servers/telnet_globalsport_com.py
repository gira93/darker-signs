from time import sleep
from termcolor import cprint
from darker_signs.dns import Dns
from darker_signs.mail import Mail
from darker_signs.utils import download_file, upload_file


class TelnetGlobalsportCom:
    def __init__(self, root_path: str, mail: Mail, dns: Dns) -> None:
        self.root_path = root_path
        self.mail = mail
        self.dns = dns

    def global23(self):
        cprint("Welcome to GlobalSport.com telnet server", "green")
        print()
        commands = ["ls", "version", "help", "exit"]
        while True:
            command = input("> ")
            match command:
                case "ls":
                    print("config.ini")
                    continue
                case "runmodule uploadandrun()":
                    file_name = input("Enter name of file to upload: ")
                    if file_name == "":
                        continue
                    file = upload_file(f"{self.root_path}/{file_name}")
                    if file:
                        if file_name == "remoteapp":
                            cprint("Upload complete", "green")
                            cprint("Running remoteapp ...", "green")
                            sleep(2)
                            cprint("INFECTED...", "red")
                            cprint("Connection closed", "red")
                            download_file(
                                f"{self.root_path}/ddos_globalsport", "", False
                            )
                            break
                        else:
                            cprint("File not compatible", "red")
                    else:
                        cprint("File not found", "red")
                case "version":
                    print()
                    print("OS: Gunner v4.5")
                    print("Build: v4.24926432a")
                    print()
                    continue
                case "help":
                    print("Avaliable commands:")
                    print("  ".join(commands))
                    continue
                case "exit":
                    cprint("Connection closed", "red")
                    break
                case _:
                    continue
