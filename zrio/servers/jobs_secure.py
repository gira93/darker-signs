import os
from termcolor import cprint
from system.utils import show_menu
from .base_server import BaseServer


class JobsSecure(BaseServer):
    def jobs_sd_http(self):
        print()
        print("Welcome to jobs.securedigital.com")
        print('Here you can find some "special" jobs.')
        options = ["See job offers"]
        selection = show_menu(options)
        if selection == "1":
            findgame_completed = os.path.isfile(
                f"{self.root_path}/system/findgame_completed"
            )
            if findgame_completed:
                print("No jobs available at this time")
                input("Press a key")
                cprint("Disconnecting", "red")
                return
            second_level = ["Find a game"]
            second_selection = show_menu(second_level)
            if second_selection == "1":
                print()
                print("A mail has been sent with all the details")
                jobs_message = [
                    "Your job is to find a game.",
                    "The game is stored at oldgames.com.",
                    "We don't have any information about the security level.",
                    "Game is DoomBeta, file DooMBeta.bin,",
                    "Once you have it, upload it to ipgames.com",
                ]
                self.mail.add_message(
                    from_user="jobs.securedigital.com",
                    subject="Job",
                    message="\n".join(jobs_message),
                )
                cprint("Disconnecting", "red")
            else:
                return
        else:
            cprint("Disconnecting", "red")
            return
