from termcolor import cprint
from darker_signs.dns import Dns
from darker_signs.mail import Mail
from darker_signs.utils import show_menu


class JobsSecure:
    def __init__(self, root_path: str, mail: Mail, dns: Dns) -> None:
        self.root_path = root_path
        self.mail = mail
        self.dns = dns

    def jobs_sd_http(self):
        print()
        print("Welcome to jobs.securedigital.com")
        print('Here you can find some "special" jobs.')
        options = ["See job offers"]
        selection = show_menu(options)
        if selection == "1":
            cprint("No jobs available at this time", "red")
            print()
            input("Press a key")
            cprint("Disconnecting", "red")
            return
            # TODO -- Maybe in the future :)
            # second_level = ["Find a game"]
            # second_selection = show_menu(second_level)
            # if second_selection == "1":
            #     print()
            #     print("A mail has been sent with all the details")
            #     jobs_message = "Your job is to find a game.\nThe game is stored at oldgames.com.\nWe don't have any information about the security level.\nThere is a rumor saying someone else wants the game too.\nBut this rumor has not been confirmed, so you should not have any problems.\nGame Doom8 file game868686.bin\nUpload the file to ipgames.com"
            #     security_message = "Great news:\nSecurity.com launched some days ago his BBS!\nYes you're right, this is a wonderfull thing.\nDon't hesitate to come and see how security holes are found in real time !\nVisit us @ bbs.security.com"
            #     self.mail.add_message(
            #         from_user="jobs.securedigital.com",
            #         subject="Job",
            #         message=jobs_message,
            #     )
            #     self.mail.add_message(
            #         from_user="security.com", subject="BBS", message=security_message
            #     )
            #     cprint("Disconnecting", "red")
            # else:
            #     return
        else:
            cprint("Disconnecting", "red")
            return
