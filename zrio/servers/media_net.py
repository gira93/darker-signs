from time import sleep
from termcolor import cprint
from system.utils import download_file, upload_file
from .base_server import BaseServer


class MediaNet(BaseServer):
    def media23(self):
        cprint("Welcome to media.net telnet server", "green")
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
                                f"{self.root_path}/system/ddos_media", "", False
                            )
                            jimmy_message = [
                                "How's it going?",
                                "I was able to hack 10 servers",
                                "and added them to our little botnet.",
                                "If you get at least 9 we're good to go.",
                                "We need to hurry though, FBI is on our trail;",
                                "There was a message encrypted in the USB drive,",
                                "you can take a look, I've left it in the zrio virtual fs at zrio.org",
                                "port 45, user: zrio, pass: geno38",
                            ]
                            self.mail.add_message(
                                from_user="jimmy@personal.com",
                                subject="How is it going?",
                                message="\n".join(jimmy_message),
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
