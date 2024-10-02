from termcolor import cprint
from system.utils import show_menu
from .base_server import BaseServer


class SecuredigitalCom(BaseServer):
    def sendmail_22(self):
        cprint("This is a private server. You will be disconnected", "red")
        print()

    def secure_http(self):
        cprint("SECURE DIGITAL :: INTERNET SERVICES", "blue")
        options = [
            "Education",
            "Internet Services",
            "Anonymouse Communications",
            "Administrative Services",
        ]
        while True:
            selection = show_menu(options)
            match selection:
                case "1":
                    print()
                    print("[Education]")
                    print("For over 10 years now, Secure Digital have provided high")
                    print("quality computer hardware and software to schools and other")
                    print("community organisations at a low price.")
                    print()
                    print("If you have a non profit organisation, and would like to")
                    print("see if you are elegible to get technology at the low price,")
                    print("we will soon be accepting applications online. Please")
                    print("check back at our website at a later date.")
                    print()
                    input("Press a key")
                    continue
                case "2":
                    print()
                    print("[Internet Services]")
                    print("Secure Digital provides Dialup Internet access to the local")
                    print(
                        "area for only $10.00 each month. This includes 1GB of bandwidth"
                    )
                    print(
                        "and 8 hours connection sessions. This means you can stay online"
                    )
                    print(
                        "for up to 8 hours before we disconnect you. Reconnections will"
                    )
                    print("take 20 minutes.")
                    print()
                    print(
                        "If you are interested in joining our Dialup Internet program, please"
                    )
                    print("contact us during business hours, on 0912 175 1712")
                    print()
                    input("Press a key")
                    continue
                case "3":
                    print()
                    print("[Anonymous Communications]")
                    print(
                        "Secure Digital believes in the rights of privacy. This means that"
                    )
                    print(
                        "we believe that what you do on the Internet is your business, and"
                    )
                    print(
                        "yours only. We support this by providing public proxy servers to"
                    )
                    print("the community.")
                    print()
                    print(
                        "You do not have to be a member to use one of our proxy servers."
                    )
                    print("They are free for anyone to use.")
                    print()
                    input("Press a key")
                    continue
                case "4":
                    print()
                    cprint("System error - Command not recognized", "red")
                    print()
                    break
                case _:
                    break
