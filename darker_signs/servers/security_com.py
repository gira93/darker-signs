from termcolor import cprint
from darker_signs.dns import Dns
from darker_signs.mail import Mail
from darker_signs.utils import show_menu

VULNS = [
    {
        "title": "FuzzyMail Exploit",
        "desc": 'Some FuzzyMail servers have the default admin pass unchanged.\nThe default username is "admin" and the default pass is "fuzzy"',
    },
    {
        "title": "XNull Exploit",
        "desc": 'By sending a malformed command, malicious users are able to copy files from the\nremote server. For example using\n "run filecopy.exe [FILENAME]"',
    },
    {
        "title": "JazzyWeb",
        "desc": 'It is possible to redirect a browser by entering\n"header::location::<server>"\n(where <server> is the destination) as a menu option',
    },
    {
        "title": "XFTP",
        "desc": "There's a buffer overflow in some versions of Xftp.\nIf the buffer size of username or password is longer than 36\nthe application will crash to a command line",
    },
    {
        "title": "Gunner Telnet",
        "desc": 'A user can run modules without permissions using the "runmodule" command\n example:\n"runmodule uploadandrun()"\nWill allow the user to upload a file and run it automatically',
    },
]


class SecurityCom:
    def __init__(self, root_path: str, mail: Mail, dns: Dns) -> None:
        self.root_path = root_path
        self.mail = mail
        self.dns = dns

    def securecommail(self):
        cprint(
            "Warning - This is a private mail server.\nYou will be automatically disconnected if you are not part of our network",
            "red",
        )
        input("Press a key")
        cprint("Access denied - Connection terminated", "red")

    def securecomhttp(self):
        cprint("Security.com Public Services", "green")
        while True:
            options = [
                "View Recent Vulnerability List",
                "Search Exploit / Vulnerability Archives",
                "Submit Exploit / Vulnerability",
                "About SECURITY.com",
            ]
            selection = show_menu(options, abort_message="Disconnect")
            match selection:
                case "1":
                    self.__recent_vulns()
                    continue
                case "2":
                    cprint(
                        'Search is currently disabled.\nAll exploits were moved to the "recent" list',
                        "red",
                    )
                    input("Press a key")
                    continue
                case "3":
                    print()
                    print(
                        "We appreciate public members submission of security related information."
                    )
                    print(
                        "To make a submission, please send it through email to submit@security.com"
                    )
                    print()
                    input("Press a key")
                    continue
                case "4":
                    print()
                    print(
                        "SECURITY.com provides a public information base for matters relating to"
                    )
                    print(
                        "Internet and Networking Security. We hope this will help system administrators"
                    )
                    print("to keep their system secure from computer hackers.")
                    print()
                    input("Press a key")
                    continue
                case _:
                    break

    def __recent_vulns(self):
        options = list(map(lambda v: v["title"], VULNS))
        while True:
            selection = show_menu(options)
            selection = int(selection)
            if selection == 0:
                break
            vuln = VULNS[selection - 1]
            print()
            cprint(vuln["title"], "blue")
            cprint(vuln["desc"], "blue")
            print()
            input("Press a key")
            continue
