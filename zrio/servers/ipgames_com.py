from termcolor import cprint
from system.dns import Dns
from system.mail import Mail
from system.utils import download_file, upload_file


class IpgamesCom:
    def __init__(self, root_path: str, mail: Mail, dns: Dns) -> None:
        self.root_path = root_path
        self.mail = mail
        self.dns = dns

    def ipgames_http(self):
        cprint("-.-.-.-.-.-.-.-.-.-.-.-.-.", "red")
        cprint("Welcome to IPGames\nThe only true archive of games!", "green")
        cprint("-.-.-.-.-.-.-.-.-.-.-.-.-.", "red")
        print()
        cprint("Downloads are currently disabled but we accept uploads!", "green")
        answer = input("Do you want to upload a file? (y/n) ")
        if answer.lower() != "y":
            cprint("Disconnecting", "red")
            return
        while True:
            filename = input("Enter a filename to upload (leave blank to exit): ")
            if filename == "":
                cprint("Disconnecting", "red")
                break
            file = upload_file(f"{self.root_path}/{filename}")
            if not file:
                cprint("File does not exists!", "red")
                continue
            if file and filename == "DooMBeta.bin":
                cprint("That's a lost gem!", "green")
                download_file(f"{self.root_path}/system/findgame_completed", "", False)
                jobs_message = [
                    "Good Job",
                    "IPGames told us the job is completed",
                    "Thank you",
                ]
                self.mail.add_message(
                    from_user="jobs.securedigital.com",
                    subject="Good Job",
                    message="\n".join(jobs_message),
                )
                cprint("Disconnecting", "red")
                break
            elif file and filename in [
                "RepairedSword.bin",
                "RacoonPeninsula.bin",
                "EarthQuake.bin",
                "LittlePeople.bin",
            ]:
                cprint("We have it already!\nBut thanks anyway!", "green")
                cprint("Disconnecting", "red")
                break
            elif file:
                cprint("This doesn't interest us! Please only send games", "red")
                cprint("Disconnecting", "red")
                break
