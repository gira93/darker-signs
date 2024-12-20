from time import sleep
from termcolor import cprint
from system.utils import download_file, upload_file
from .base_server import BaseServer


class FtpChrist(BaseServer):
    def christ21(self):
        cprint("Welcome to stLukes.christ.org private ftp server", "green")
        print()
        commands = ["ls", "put", "run", "version", "help", "exit"]
        remoteapp = False
        while True:
            command = input("> ")
            match command:
                case "ls":
                    print()
                    if remoteapp:
                        print("remoteapp")
                    else:
                        print("NO FILES")
                    print()
                    continue
                case "put":
                    file_name = input("Enter file name to upload: ")
                    file = upload_file(f"{self.root_path}/{file_name}")
                    if file:
                        if file_name == "remoteapp":
                            remoteapp = True
                            cprint("File uploaded", "green")
                        else:
                            cprint("File not compatible", "red")
                    else:
                        cprint("File does not exists in local", "red")
                    continue
                case "run":
                    file_name = input("Enter file name to run: ")
                    if file_name == "remoteapp" and remoteapp:
                        cprint("Running remoteapp...", "green")
                        sleep(2)
                        cprint("INFECTED", "red")
                        cprint("Connection closed", "red")
                        download_file(
                            f"{self.root_path}/system/ddos_stlukes", "", False
                        )
                        break
                    else:
                        cprint("File not found or not executable", "red")
                        continue
                case "version":
                    print()
                    print("Version: FTPD v1.0")
                    print("Build: 0.821885")
                    print()
                case "help":
                    print("Available commands:")
                    print("  ".join(commands))
                    continue
                case "exit":
                    cprint("Connection closed", "red")
                    break
                case _:
                    continue
