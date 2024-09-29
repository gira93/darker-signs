import os
from time import sleep
from random import randint
from termcolor import cprint
from system.dns import Dns
from system.mail import Mail
from system.utils import download_file, progress_bar, show_menu


class OldgamesCom:
    def __init__(self, root_path: str, mail: Mail, dns: Dns) -> None:
        self.root_path = root_path
        self.mail = mail
        self.dns = dns

    def oldg_ftp(self):
        cprint(
            "XFTP Runtime error\nConfig file is unreadable\nReverting to default", "red"
        )
        cprint("Logged in as guest", "green")
        user = "guest"
        commands = ["run", "ls", "cat", "ps", "kill", "exit", "help"]
        xftp_pid = str(randint(1, 999))
        while True:
            ps1 = "#> " if user == "admin" else "> "
            command = input(ps1).split()
            com = command[0] if len(command) > 0 else ""
            param = command[1] if len(command) > 1 else ""
            match com:
                case "run":
                    if user == "xftp" and param == "xftp.exe":
                        if len(command) >= 3 and command[2] == "--debug":
                            cprint("Running XFTP in debug mode", "green")
                            cprint("You are admin", "green")
                            user = "admin"
                        else:
                            cprint("Restarting XFTP", "green")
                            cprint("Please log out and log back in", "green")
                            cprint("Disconnecting", "red")
                            return
                    continue
                case "ls":
                    if user == "guest":
                        print("NO FILES")
                    if user == "xftp":
                        print("xftp.exe  init.conf")
                    if user == "admin":
                        print("ap_config.conf")
                    continue
                case "cat":
                    if user == "xftp" and param == "init.conf":
                        print()
                        print(
                            "debug=false\nallow_guest=true\nrescue_user=xftp\ndefault_user=guest\nallow_commands=run,ls,cat,ps,kill"
                        )
                        print()
                    if user == "admin" and param == "ap_config.conf":
                        print()
                        print(
                            "# Admin Panel Config\nfailsafe_user=oldg-admin\nfailsafe_pass=oldgrulez\nfailsave_is_admin=false\nbackup_config=true"
                        )
                        print()
                case "ps":
                    if user == "guest":
                        print("Processes:")
                        print(f"{xftp_pid}  xftp.exe")
                    continue
                case "kill":
                    if user == "guest" and param == xftp_pid:
                        cprint("Connection lost", "red")
                        cprint("Reverting to user xftp", "green")
                        cprint("Logged in as user xftp", "green")
                        user = "xftp"
                    continue
                case "exit":
                    cprint("Connection closed", "red")
                    return
                case "help":
                    print()
                    print("Available commands:")
                    print("  ".join(commands))
                    print()

    def oldg_http(self):
        oldg_recovered = os.path.isfile(f"{self.root_path}/system/oldg_recovered")
        if not oldg_recovered:
            print()
            cprint(
                "ERROR!\nCannot read config file or file is damaged\nConnection closed",
                "red",
            )
            return
        cprint("-----------------------------------", "green")
        cprint(
            "Welcome to oldgames.com\nHere you'll find some amazing games\nand also unreleased stuff!",
            "green",
        )
        cprint("-----------------------------------", "green")
        print()
        level = 1
        options = ["Download Games", "Upload a game", "Who we are"]
        lv2_options = [
            "Repaired Sword",
            "The Secrets of Racoon Peninsula",
            "EarthQuake",
            "DooMBeta",
            "City of Little People",
        ]
        while level == 1:
            selection = show_menu(options)
            match selection:
                case "1":
                    level = 2
                    continue
                case "2":
                    print()
                    print(
                        "Uploads are currently disabled.\nWe know you want to contribute so stay tuned!"
                    )
                    print()
                    input("Press a key")
                    continue
                case "3":
                    print()
                    print(
                        "We are the best website for old games, do not trust any other site"
                    )
                    print("especially ipgames ahahahah.")
                    print("Only download legit games from us!")
                    print()
                    input("Press a key")
                    continue
                case _:
                    cprint("Disconnected", "red")
                    break
        while level == 2:
            selection = show_menu(lv2_options)
            match selection:
                case "1":
                    download_file(
                        f"{self.root_path}/RepairedSword.bin",
                        "The broken sword was repaired successfully",
                    )
                    continue
                case "2":
                    download_file(
                        f"{self.root_path}/RacoonPeninsula.bin",
                        "Look!\nA triple headed racoon behind you!",
                    )
                    continue
                case "3":
                    download_file(
                        f"{self.root_path}/EarthQuake.bin",
                        "I need some long nails for this job.\n9 inch long at least",
                    )
                    continue
                case "4":
                    download_file(
                        f"{self.root_path}/DooMBeta.bin", "guitar riffs and demons"
                    )
                    continue
                case "5":
                    download_file(
                        f"{self.root_path}/LittlePeople.bin",
                        "Can't understand a thing they say",
                    )
                    continue
                case _:
                    cprint("Disconnected", "red")
                    break

    def oldg_admin(self):
        oldg_recovered = os.path.isfile(f"{self.root_path}/system/oldg_recovered")
        if not oldg_recovered:
            cprint("Cannot read config file", "red")
            cprint("Failsafe configuration loaded", "green")
            sleep(1)
            print("Please insert failsafe credentials for recovery")
        user = input("User: ")
        pw = input("Password: ")
        if not oldg_recovered and (user == "oldg-admin" and pw == "oldgrulez"):
            print("Recovering config file")
            progress_bar()
            cprint("Successfully recovered config files!", "green")
            download_file(f"{self.root_path}/system/oldg_recovered", "", False)
            cprint("Logging out of failsafe console", "red")
            return
        else:
            cprint("Wrong user and/or password", "red")
            return
