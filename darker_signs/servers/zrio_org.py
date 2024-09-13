from getpass import getuser
from termcolor import cprint
from darker_signs.dns import Dns
from darker_signs.mail import Mail
from darker_signs.utils import download_file, upload_file


class ZrioOrg:
    def __init__(self, root_path: str, mail: Mail, dns: Dns) -> None:
        self.root_path = root_path
        self.mail = mail
        self.dns = dns

    def zrio_filetransfer(self):
        cprint("Connected to ZRIO File Transfer", "green")
        confirm = input("Would you like to upload a file to our server? (y/n): ")
        if confirm != "y":
            cprint("Connection closed by server", "red")
            return
        while True:
            file = input(
                "Enter complete file name or nothing to cancel (Eg: myfile.file): "
            )
            if file == "":
                break
            if upload_file(f"{self.root_path}/{file}"):
                match file:
                    case "8m.enc":
                        message = "This is an automated message\nThanks for the file, it's good to have you on our side.\nUnfortunately, the file you got for us is encrypted.\nAre you able to decrypt it?\n\nYou could try using the tools at decrypt.com...\nWhen asked who to send it to, type in ZRIO.\n\nHope to hear from you again."
                        self.mail.add_message(
                            from_user="zrio", subject="8m.enc", message=message
                        )
                        break
                    case "cryptsetup.exe":
                        jimmy_message = [
                            "Thanks for the file, I'm running the decryption right now.",
                            "I have bad news: they know about what we are doing!",
                            "They deactivated my account on zrio (but I was able to keep my backdoor open)",
                            "We need to crash this subnet",
                            "There are 2 websites that have a connection with the outside network:",
                            "- fbi.gov",
                            "- zrio.org",
                            "DDoSing both should also crash the respective server in the open web",
                            "Take a look at crackertools.com, they have a tool for that,",
                            "I'll do the same, you should try and have at least 9 servers hacked and ready",
                            "We'll keep in touch",
                        ]
                        self.mail.add_message(
                            from_user="jimmy@personal.com",
                            subject="Not so good",
                            message="\n".join(jimmy_message),
                        )
                        break
                    case _:
                        cprint(
                            "That's not the file we expect, please refrain from sending unwanted files.",
                            "red",
                        )
                        continue
            else:
                cprint("File not found", "red")
                continue

    def xcapro(self):
        user = input("Username: ")
        pw = input("Password: ")
        if user == "zrio" and pw == "geno38":
            self.__geno38_message()
        elif user == "zrio" and pw == "geno91":
            self.__geno91_message()
        else:
            return

    def __geno38_message(self):
        print()
        print("To: Alan Johnson(alanjohnson@fbi.gov)")
        print("Document: 22643")
        print("Encryption: 7")
        print()
        print("We have a problem, two guys from ZRIO knows a bit too much.")
        print(
            "They know about the virtual network, they shouldn't be able to reach us but we need to stay alert."
        )
        print(
            f"One hacker in particular going by the alias of {getuser()} is the most active of the two."
        )
        print(
            "We need this problem handled in the usual way. We cant let anyone know about our projects"
        )
        print("")
        return

    def __geno91_message(self):
        ips = [
            "103.45.32.3",
            "72.32.23.54",
            "194.20.37.51",
            "130.239.47.117",
            "215.170.237.35",
            "193.228.123.186",
            "23.22.213.146",
            "98.90.114.41",
            "159.114.182.232",
            "188.174.32.138",
            "115.113.51.237",
            "71.20.174.218",
            "73.121.96.239",
            "92.183.28.121",
            "71.100.81.138",
            "92.164.16.23",
            "145.217.69.76",
            "28.137.198.15",
            "49.78.59.115",
            "120.106.216.70",
            "51.136.67.87",
            "103.45.33.3",
        ]
        download_file(f"{self.root_path}/ips.txt", "\n".join(ips))
        cprint("File downloaded to ips.txt", "green")
        return
