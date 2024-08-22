from termcolor import cprint
from darker_signs.dns import Dns
from darker_signs.mail import Mail
from darker_signs.utils import download_file, show_menu


class Regd204Regdomainz:
    def __init__(self, root_path: str, mail: Mail, dns: Dns) -> None:
        self.root_path = root_path
        self.mail = mail
        self.dns = dns

    def xnullrg(self):
        print()
        while True:
            print("Null connection")
            command = input("Enter input (type exit to quit)")
            if command == "exit":
                break
            if command == "run filecopy.exe dompass.txt":
                contents = [
                    "[recent-registration-passwords-internal-data-file]",
                    "username:password:ip:hostname",
                    "ndrgrnd:burntcrisp:66.7.82.99:internal-9.ndrgrnd.pipelink.gov",
                ]
                cprint("Downloading dompass.txt...", "green")
                download_file(f"{self.root_path}/dompass.txt", "\n".join(contents))
                break

    def fuzzymail82(self):
        print()
        cprint("Connected to FUZZY Mail", "blue")
        print()
        user = input("Username: ")
        pw = input("Password: ")
        if user == "admin" and pw == "fuzzy":
            cprint("User admin logged in", "green")
            print()
            print("- - - - Welcom Admin - - - -")
            print()
            options = ["Read New Messages", "Read Old Messages"]
            while True:
                selection = show_menu(options)
                match selection:
                    case "1":
                        print()
                        cprint("FROM: Adam Palmer\nSubject: Recent Proposal", "blue")
                        print()
                        print(
                            "I have decided not to go ahead with the\nother domain business. For now I don't"
                        )
                        print(
                            "need it, however I will keep it in mind, maybe\nat a later date perhaps."
                        )
                        print(
                            "Please let me know if you have ant concerns regarding this."
                        )
                        print()
                        print("Regards,\nAdam")
                        print()
                        input("Press a key")
                        continue
                    case "2":
                        print()
                        cprint("FROM: RegDomains Admin\nSubject: Filenames", "blue")
                        print()
                        print("Hello co admin!")
                        print(
                            "Regarding your recent support question, yes it is possible,"
                        )
                        print(
                            "To modify passwords simply open dompass.txt file and make changes as needed."
                        )
                        print()
                        print("Regards\nScott Riley")
                        print()
                        input("Press a key")
                        continue
                    case _:
                        break
        else:
            cprint("Invalid user or password, disconnecting", "red")
