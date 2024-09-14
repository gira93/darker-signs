from getpass import getuser
from termcolor import cprint
from darker_signs.dns import Dns
from darker_signs.mail import Mail
from darker_signs.utils import show_menu, upload_file


class DecryptCom:
    def __init__(self, root_path: str, mail: Mail, dns: Dns) -> None:
        self.root_path = root_path
        self.mail = mail
        self.dns = dns

    def decrypt_http(self):
        cprint("Public File Decryption Server", "green")
        selection = show_menu(["Decrypt a File"])
        if selection != "1":
            return
        file = input(
            "Enter complete file name as it exists, leave empty to quit (Eg: myfile.file): "
        )
        if file == "":
            return
        if upload_file(f"{self.root_path}/{file}"):
            receiver = input("Please specify what organization to send to: ")
            if receiver.lower() == "zrio" or receiver.lower() == "zrio.org":
                match file:
                    case "8m.enc":
                        security_message = "Hello Subscribers!\nThere has been a new bug found in a rare version of the FuzzyMail Server.\nCheck our website for more information\n\nRegards,\nDavid Ashburn\nSECURITY.com"
                        zrio_message = "You did it! We recieved the decryption of the file successfully.\nThank you for your continued efforts.\n\nWe need another file called 9m.enc from biolabs.com, we need it decrypted as well.\n\nGood Luck."
                        jimmy_message = "Who are you?\nYou should't be able to access this network.\nI'm monitoring it for ZRIO, we work together with hackers to keep the world safe.\nSince you were able to enter here, I think you could help us!\nI'll take over the automated mailbox from now on, continue your assignment as requested\nin the other email"
                        self.mail.add_message(
                            from_user="security.com",
                            subject="MailingListNews",
                            message=security_message,
                        )
                        self.mail.add_message(
                            from_user="zrio", subject="decryption", message=zrio_message
                        )
                        self.mail.add_message(
                            from_user="jimmy@zrio",
                            subject="Who are you?",
                            message=jimmy_message,
                        )
                        return
                    case "9m.enc":
                        zrio_message = "File is good, I pieced it together with the other one\nand it's another encrypted string; I'll work on that, in the meantime\nsee what else you can find around biolabs...\nPerhaps try biolabs.org, or similar servers.\nThere must be something..."
                        self.mail.add_message(
                            from_user="zrio", subject="Good...", message=zrio_message
                        )
                    case "10m.enc":
                        zrio_message = f"This doesn't seem to contain anything valuable.\nI was able to decrypt the combined files from before!\n\nThey contain an IP range:66.7.1.1 to 66.7.115.255\n\nTry a scan with scan.com.\nDig deep, {getuser()}, we are getting close!"
                        self.mail.add_message(
                            from_user="zrio", subject="10m.enc", message=zrio_message
                        )
                    case _:
                        cprint("File rejected by receiver, disconnecting", "red")
            else:
                cprint("Organization not found, disconnecting", "red")
        else:
            cprint("File not found", "red")
            return
