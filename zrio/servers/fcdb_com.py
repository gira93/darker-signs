from termcolor import cprint
from system.dns import Dns
from system.mail import Mail
from system.utils import show_menu


class FcdbCom:
    def __init__(self, root_path: str, mail: Mail, dns: Dns) -> None:
        self.root_path = root_path
        self.mail = mail
        self.dns = dns

    def fcdb80(self):
        cprint("Welcome to FirstClass DataBase website", "green")
        cprint("FirstClass Software 1989-2003 FCDB.com")
        print()
        options_lv1 = ["About us", "Get FCDB", "FCDB documentation", "Contact us"]
        options_lv2 = ["Commands", "Known Bugs and Problems", "Report Bug"]
        level = 1
        while level == 1:
            selection = show_menu(options_lv1)
            match selection:
                case "1":
                    print()
                    cprint("What is FCDB?", "blue")
                    print()
                    print(
                        "FirstClass DataBase is not your ordinary database. FCDB is a smart database"
                    )
                    print(
                        "with many features that include, remote script execution, auto fix, command"
                    )
                    print(
                        "prompt usage and many many more. FCDB is ideal for small and large"
                    )
                    print(
                        "businesses alike, even the average user can benefit from FCDB."
                    )
                    print("FCDB is your all-round database, accept nothing else.")
                    print()
                    input("Press enter to continue")
                    continue
                case "2":
                    print()
                    cprint("How to purchase FCDB", "blue")
                    print()
                    print(
                        "You can purchase FCDB by emailing sales@fcdb.com all information"
                    )
                    print("will be emailed back to you asap")
                    print()
                    input("Press enter to continue")
                    continue
                case "3":
                    level = 2
                case "4":
                    print()
                    cprint("Contact FCDB Team")
                    print()
                    print(
                        "If you wish to contact the FCDB team then please send emails to info@fcdb.com"
                    )
                    print()
                    input("Press a key")
                    continue
                case _:
                    cprint("Connection closed", "red")
                    break

        while level == 2:
            selection = show_menu(options_lv2)
            match selection:
                case "1":
                    print()
                    cprint("FCDB Commands", "blue")
                    cprint("These commands are to be userd in the FCDB console", "blue")
                    print()
                    print("cd <folder>: Changes current dir")
                    print("ls: List file in the current dir")
                    print("run <filename>: Run the specified file")
                    print("su <user>: Changes to specified user")
                    print("exit: Exits the FCDB console")
                    print()
                    input("Press a key")
                    continue
                case "2":
                    print()
                    cprint("FCDB Known Bugs and Problems", "blue")
                    print()
                    print("Posted by BugTracker2000")
                    print("--------------------------------------------------------")
                    print(
                        "If the sysadmin is stupid and does not take access to command SU out"
                    )
                    print(
                        "a user maybe able to exploit this to gain higher premissions."
                    )
                    print("Fix: Deny access for any user to use this command.")
                    print("--------------------------------------------------------")
                    print()
                    print("Posted by BillyBase")
                    print("--------------------------------------------------------")
                    print(
                        "There is a buffer overflow in the exc( ) module, if a string of more then"
                    )
                    print(
                        "255 chars the user will be thrown into the console as admin user."
                    )
                    print(
                        "Fix: Edit options.ini to deny access to the exc( ) module until patch"
                    )
                    print("is released.")
                    print("--------------------------------------------------------")
                    print()
                    input("Press a key")
                    continue
                case "3":
                    print()
                    cprint("Report FCDB Bug", "blue")
                    print()
                    print("Please email all bug reports to bugs@fcdb.com")
                    print()
                    input("Press a key")
                    continue
                case _:
                    level = 1
