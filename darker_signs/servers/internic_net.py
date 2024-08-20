from darker_signs.dns import Dns
from darker_signs.mail import Mail
from darker_signs.utils import show_menu


class InternicNet:
    def __init__(self, root_path: str, mail: Mail, dns: Dns) -> None:
        self.root_path = root_path
        self.mail = mail
        self.dns = dns

    def http_internic(self):
        print("'_'_'_'_'_'_'_'_'_'_'_'_'_'_'_'_'_'_'_'_'_'_'_'_'_'_'")
        print()
        print("- - -  i n t e r n i c  - - -  s e r v i c e s  - - -")
        print()
        print("'_'_'_'_'_'_'_'_'_'_'_'_'_'_'_'_'_'_'_'_'_'_'_'_'_'_'")
        options = ["Recent Registrations"]
        selection = show_menu(options)
        if selection == "1":
            print("'_'_'_'_'_'_'_'_'_'_'_'_'_'_'_'_'_'_'_'_'_'_'_'_'_'_'")
            print()
            print(".  - - - r e c e n t  -  -  -  d o m a i n s - - -  .")
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