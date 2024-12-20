import os
from time import sleep
from termcolor import cprint
from system.utils import download_file, progress_bar
from .base_server import BaseServer

DDOS_SERVERS = 9
DDOS_HOSTS = ["zrio.org", "fbi.gov"]


class DoserCom(BaseServer):
    def dos80(self):
        cprint("Welcome to DoSer v3.1", "green")
        print()
        selection = input("Connect to infected servers? (y/n) ").lower()
        if selection == "y":
            self.__start_ddos()
        else:
            cprint("Connection closed, bye", "red")
            return

    def __start_ddos(self):
        print()
        cprint("Connecting to servers...", "yellow")
        sleep(2)
        _, _, files = next(os.walk(f"{self.root_path}/system"))
        ddos_files = list(filter(lambda f: f.startswith("ddos_"), files))
        if len(ddos_files) == DDOS_SERVERS:
            progress_bar()
            cprint("Connected to servers", "green")
            cprint("DDoS armed and READY", "green")
            print()
            host = input("Enter host to attack: ")
            if host in DDOS_HOSTS:
                cprint("DDoSing ...", "green")
                progress_bar()
                cprint("Target DDoSed!", "green")
                download_file(f"{self.root_path}/system/down_{host}", "", False)
                zrio_down = os.path.isfile(f"{self.root_path}/system/down_zrio.org")
                fbi_down = os.path.isfile(f"{self.root_path}/system/down_fbi.gov")
                if zrio_down and fbi_down:
                    jimmy_message = [
                        "We did it!, YOU did it!",
                        "Zrio is down, FBI is down too!",
                        "They can get back up in no time if they want.",
                        "I've sent a message to all connected users explaining everything;",
                        "They just need to leave the network and that's it.",
                        "I think it's over for real now, thank you!",
                        "I don't think we'll ever meet in person but you never know...",
                        "It was a pleasure teaming up with you.",
                        "Thanks for everything",
                        "Bye!",
                    ]
                    self.mail.add_message(
                        from_user="jimmy@personal.com",
                        subject="YOU DID IT!",
                        message="\n".join(jimmy_message),
                    )
                    unk_message = [
                        "The plan worked",
                        "You did exactly what we planned",
                        'You really thought that "someone" dumped the zrio chroot like that?',
                        "We did it, we planned all of that, you were supposed to find the code",
                        "get in, know Jimmy and work with him.",
                        "Helping you was one of his assignments;",
                        "Don't be scared of us, we are actually the good guys.",
                        "And I think now is the time for you to enter the real world...",
                        "",
                        "upgrade.mother.net",
                        "---",
                        "The Mother Triad",
                    ]
                    self.mail.add_message(
                        from_user="karma@mother.net",
                        subject="You did good",
                        message="\n".join(unk_message),
                    )
                return
            else:
                cprint("Host Unreachable", "red")
                print()
                return
        else:
            print()
            cprint("Not enough servers for a DDoS attack", "red")
            cprint("Exiting", "red")
            return
