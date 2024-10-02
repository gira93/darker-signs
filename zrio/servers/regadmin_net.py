from termcolor import cprint
from system.utils import show_menu
from .base_server import BaseServer


class RegadminNet(BaseServer):
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
            while True:
                selection = show_menu(options)
                match selection:
                    case "1":
                        cprint("Account Domains", "blue")
                        print()
                        print("internal-9.ndrgrnd.pipelink.gov : 66.7.82.99")
                        print("base09.pipelink.gov : 66.199.200.203")
                        print()
                        input("Press a key")
                        continue
                    case "2" | "3":
                        print()
                        cprint("Disabled for maintenance", "red")
                        print()
                        input("Press a key")
                        continue
                    case _:
                        cprint("Connection closed", "red")
                        break
        else:
            cprint("Invalid username or password", "red")
