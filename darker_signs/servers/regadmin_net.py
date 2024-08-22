from termcolor import cprint
from darker_signs.dns import Dns
from darker_signs.mail import Mail


class RegadminNet:
    def __init__(self, root_path: str, mail: Mail, dns: Dns) -> None:
        self.root_path = root_path
        self.mail = mail
        self.dns = dns

    def http_regadmin(self):
        cprint("#     #    #   #  # ################### #  #   #    #     #", "green")
        cprint("REGDOMAINZ Domain Administration Server", "green")
        cprint("#     #    #   #  # ################### #  #   #    #     #", "green")
        print()
        user = input("Username: ")
        pw = input("Password: ")
        if user == "ndrgrnd" and pw == "burntcrisp":
            cprint("0X0X0X0X0X0X0X0X0X0X0X0X0X0X0X0X0X0X0X0X0X0X0X0X0X0", "blue")
            print()
            cprint("This server is currently undergoing maintenance.", "yellow")
            cprint("To make major changes to your domain(s), please ring", "yellow")
            cprint("us directly on (+613) 752 6019.", "yellow")
            print()
            cprint("0X0X0X0X0X0X0X0X0X0X0X0X0X0X0X0X0X0X0X0X0X0X0X0X0X0", "blue")
            options = [
                "View Account Domains",
                "Disabled for Maintenance",
                "Disabled for Maintenance",
            ]
            if options == "1":
                cprint("Account Domains", "blue")
                print()
                print("internal-9.ndrgrnd.pipelink.gov : 66.7.82.99")
                print("base09.pipelink.gov : 66.199.200.203")
                print()
                return
            else:
                return
        else:
            cprint("Invalid username or password", "red")
