from termcolor import cprint
from system.utils import show_menu
from .base_server import BaseServer


class RegdomainzNet(BaseServer):
    def http_regdomainz(self):
        print()
        print("REGDOMAINZ.net")
        print("----------- D o m a i n ---- R e  g i s t r y -----------")
        print("REGDOMAINSREGDOMAINSREGDOMAINSREGDOMAINS")
        print("REGDOMAINSREGDOMAINSREGDOMAINSREGDOMAINS")
        options = ["Registrations", "Maintenance", "Network"]
        print("REGDOMAINSREGDOMAINSREGDOMAINSREGDOMAINS")
        print("REGDOMAINSREGDOMAINSREGDOMAINSREGDOMAINS")
        while True:
            selection = show_menu(options)
            match selection:
                case "1":
                    print()
                    cprint("REGDOMAINZ Domain Registration", "blue")
                    print()
                    print(
                        "REGDOMAINZ currently only accepts domain registrations from Australia"
                    )
                    print(
                        "and the surrounding area including New Zealand, Antarctica and Fiji."
                    )
                    print(
                        "We are offering domains for a limited time price of just $12.95 a year."
                    )
                    print("Please call (03) 9752 6019")
                    print()
                    input("Press a key")
                    continue
                case "2":
                    print()
                    cprint("REGDOMAINZ Domain Maintenance", "blue")
                    print()
                    print("Domain owners, to administer your domain name,")
                    print("you must connect to REGADMIN.net")
                    print()
                    input("Press a key")
                    continue
                case "3":
                    print()
                    cprint("REGDOMAINZ Network", "blue")
                    print()
                    print(
                        "REGDOMAINZ owns a large network which can be used for Internet Services"
                    )
                    print("Our local range includes 90.92.106.1 - 90.92.186.255")
                    print()
                    input("Press a key")
                    continue
                case _:
                    break
