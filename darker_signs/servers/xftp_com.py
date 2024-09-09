from termcolor import cprint
from darker_signs.dns import Dns
from darker_signs.mail import Mail
from darker_signs.utils import show_menu


class XftpCom:
    def __init__(self, root_path: str, mail: Mail, dns: Dns) -> None:
        self.root_path = root_path
        self.mail = mail
        self.dns = dns

    def xftp80(self):
        print()
        cprint("Thank you for visiting XFTP's official website", "blue")
        print()
        options = ["What is XFTP", "Bugs", "Donations", "Contact us"]
        while True:
            selection = show_menu(options)
            match selection:
                case "1":
                    print()
                    cprint("What is XFTP?", "green")
                    print()
                    print(
                        "XFTP is an open source FTP server service. It is free for all to download"
                    )
                    print(
                        "and edit in anyway they see fit. Features in XFTP include multiple user"
                    )
                    print("accounts, permissions, auto-update and more.")
                    print()
                    input("Press a key")
                    continue
                case "2":
                    print()
                    cprint("Bug reports", "green")
                    print()
                    print("-------------------------------------------------------")
                    print("Buffer Over Flow in Login Command")
                    print("-------------------------------------------------------")
                    print("Affected versions: 1.x")
                    print("Priority: Extreme")
                    print("-------------------------------------------------------")
                    print(
                        "There is a buffer over flow in the login command for XFTP v1.x command"
                    )
                    print(
                        "that could give command prompt access as user xftp. xftp user only has"
                    )
                    print("read write access to the xftp root directory.")
                    print(
                        "If a string more then 36 characters long is entered as the username OR"
                    )
                    print(
                        "password XFTP will crash and throw you into the command prompt."
                    )
                    print("-------------------------------------------------------")
                    print("Fix: Apply patch to server")
                    print("-------------------------------------------------------")
                    print()
                    print("-------------------------------------------------------")
                    print("Default Admin Access Using debug Mode")
                    print("-------------------------------------------------------")
                    print("Affected versions: 1.x")
                    print("Priority: Urgent")
                    print("-------------------------------------------------------")
                    print(
                        "If an attacker gained access to the xftp executable file they could gain admin rights"
                    )
                    print(
                        'in XFTP. By running the server in debuug mode with the "--debug" flag, an attacker could run XFTP'
                    )
                    print(
                        "with admin rights on connect. The default for debug mode is off."
                    )
                    print("-------------------------------------------------------")
                    print("Fix: Apply patch to server")
                    print("-------------------------------------------------------")
                    print()
                    input("Press a key")
                    continue
                case "3":
                    print()
                    cprint("Donations", "green")
                    print()
                    print("Thank you for your interest in supporting the XFTP project.")
                    print(
                        "Please send an email to donations@xftp.com for info about donating to the project."
                    )
                    print()
                    input("Press a key")
                    continue
                case "4":
                    print()
                    cprint("Contact us", "green")
                    print()
                    print(
                        "For any additional information please send emails to info@xftp.com"
                    )
                    print()
                    input("Press a key")
                    continue
                case _:
                    cprint("Connection closed", "red")
                    break
