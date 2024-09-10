from termcolor import cprint
from darker_signs.dns import Dns
from darker_signs.mail import Mail
from darker_signs.utils import show_menu


class DbPostofficeMil:
    def __init__(self, root_path: str, mail: Mail, dns: Dns) -> None:
        self.root_path = root_path
        self.mail = mail
        self.dns = dns

    def fcdb(self):
        cprint("FirstClass Software 1989-2003 fcdb.com", "blue")
        print()
        user = 100
        while user == 100:
            command = input("> ")
            match command:
                case "su fcdb":
                    user = 0
                case "ls" | "su" | "su admin" | "cd" | "run":
                    cprint("System permission error [not authorized]", "red")
                    continue
                case "exit":
                    cprint("Connection closed", "red")
                    break
                case _:
                    continue

        while user == 0:
            command = input("#> ")
            match command:
                case "ls":
                    cprint("EDITDB.EXE  LOGIC.SYS  READDB.EXE  OPTIONS.INI", "blue")
                    continue
                case "run editdb.exe":
                    self.__editdb()
                    continue
                case "run readdb.exe":
                    cprint(
                        "Service is already running, use a client to read db data",
                        "red",
                    )
                    continue
                case "exit":
                    cprint("Connection closed", "red")
                    break
                case _:
                    continue

    def __editdb(self):
        print()
        cprint("------------------------------------", "blue")
        cprint("-     FirstClass DataBase v3.4     -", "blue")
        cprint("------------------------------------", "blue")
        print()
        options = ["Track Package", "Change Package Details"]
        while True:
            selection = show_menu(options)
            match selection:
                case "1":
                    print()
                    cprint("Package tracker", "blue")
                    print()
                    package_no = input("Please enter the package number")
                    if package_no == "883597":
                        cprint("Package found", "green")
                        print("Status: In Warehouse, awaiting pickup")
                        input("Press a key")
                        continue
                    else:
                        cprint("Package not found", "red")
                        continue
                case "2":
                    print()
                    cprint("Package detail changer", "blue")
                    print()
                    package_no = input("Please enter the package number")
                    if package_no == "883597":
                        cprint("Package found", "green")
                        cprint("Details:", "green")
                        print("Destination: **Classified**")
                        print("Postage type: **Priority**")
                        print()
                        dest = input("Enter new destination or leave blank to cancel")
                        match dest.lower():
                            case "26 masen av new york usa":
                                jimmy_message = [
                                    "Package received, thanks.",
                                    "I was correct in being suspicious... ZRIO is all into this!",
                                    "They were (and still are) hiring skillful hackers just to keep them occupied",
                                    "so they can continue their business unnoticed.",
                                    "This environment we are using, while it IS connected to a subnet, it's all fake!",
                                    "Biolabs, nazis, dolphins, all fake; a small but skillfully created playground to keep hackers happy...",
                                    "And it was all written in those classified documents you were able to forward to me.",
                                    "I gave you a safe address outside ZRIO not to raise suspects further, but I think they know something.",
                                    "Inside the envelope there was also a USB drive, it's encrypted though;",
                                    "I don't have the means to decrypt it from where I am, but before leaving I got a list of IPs from a network config I found.",
                                    "I dumped it to the virtual zrio server, zrio.org on port 45. user: zrio, pass: geno91",
                                    "Once you have this file, upload it to the same zrio server as you did before.",
                                    "They are not actively monitoring the users inside the subnet for now.",
                                    "Be safe and thanks for now",
                                ]
                                self.mail.add_message(
                                    from_user="jimmy@personal.com",
                                    subject="This changes everything!",
                                    message="\n".join(jimmy_message),
                                )
                                return
                            case _:
                                continue
                    else:
                        cprint("Package not found", "red")
                        continue
                case _:
                    return
