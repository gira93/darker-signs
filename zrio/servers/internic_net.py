from system.utils import show_menu
from .base_server import BaseServer


class InternicNet(BaseServer):
    def http_internic(self):
        print("'_'_'_'_'_'_'_'_'_'_'_'_'_'_'_'_'_'_'_'_'_'_'_'_'_'_'")
        print()
        print("- - -  i n t e r n i c  - - -  s e r v i c e s  - - -")
        print()
        print("'_'_'_'_'_'_'_'_'_'_'_'_'_'_'_'_'_'_'_'_'_'_'_'_'_'_'")
        options = ["Recent Registrations"]
        while True:
            selection = show_menu(options)
            if selection == "1":
                print("'_'_'_'_'_'_'_'_'_'_'_'_'_'_'_'_'_'_'_'_'_'_'_'_'_'_'")
                print()
                print(".  - - - r e c e n t  -  -  -  d o m a i n s - - -  .")
                print()
                print("._._._._._._._._._._._._._._._._._._._._._._._._._._.")
                print()
                print("webcache02.securedigital.com")
                print("micmast.com")
                print("newpute.com")
                print("depressed.net  (Registered with private company REGDOMAINZ)")
                print("securedigital.com")
                print(
                    "internal-9.ndrgrnd.pipelink.gov  (Registered with private company REGDOMAINZ)"
                )
                print("targetmailer.com  (Registered with private company REGDOMAINZ)")
                print("darksigns.com")
                print("jobs.securedigital.com")
                print()
                continue
            else:
                break
