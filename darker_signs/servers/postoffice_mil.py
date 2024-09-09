from termcolor import cprint
from darker_signs.dns import Dns
from darker_signs.mail import Mail
from darker_signs.utils import show_menu


class PostofficeMil:
    def __init__(self, root_path: str, mail: Mail, dns: Dns) -> None:
        self.root_path = root_path
        self.mail = mail
        self.dns = dns

    def post80(self):
        cprint("Welcome to the Military PostOffice Website", "green")
        options = ["About us", "Employment", "Check package status", "Email admin"]
        while True:
            selection = show_menu(options)
            match selection:
                case "1":
                    cprint("What we do:", "blue")
                    print()
                    print(
                        "The Military PostOffice is just like your ordinary postoffice with the major difference being"
                    )
                    print(
                        "that we deliver postage to US armed forces all around the world."
                    )
                    print()
                    cprint("How important is the Military PostOffice?", "blue")
                    print()
                    print(
                        "The Military PostOffice is very important to the workings of the US"
                    )
                    print(
                        "forces. With out us no-one would get any mail, the men on the battle"
                    )
                    print(
                        "field would not be able to communicate with their families back home."
                    )
                    print(
                        "We also do much more then deliver mail, we also control the traffic"
                    )
                    print("of our electronic mail(eMail).")
                    print()
                    input("Press a key")
                    continue
                case "2":
                    print()
                    print(
                        "If you wish to find out about current job offers for the Military PostOffice"
                    )
                    print(
                        "then email jobs@postoffice.mil with your details and we will get back to"
                    )
                    print("you ASAP.")
                    print()
                    input("Press a key")
                    continue
                case "3":
                    cprint("Critical HTTP error: Encryption error 677", "red")
                    cprint("Transfered from: prx.postoffice.mil", "red")
                    cprint("Module getdb()", "red")
                    print()
                    cprint("Please email admin with errors above", "red")
                    print()
                    input("Press a key")
                    continue
                case "4":
                    print("Email bug/error reports to admin@postoffice.mil")
                    print("Please quote all error information")
                    print()
                    input("Press a key")
                    continue
                case _:
                    cprint("Connection closed", "red")
                    break
