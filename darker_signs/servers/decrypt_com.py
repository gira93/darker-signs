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
                        zrio_message = "You did it! We recieved the decryption of the file successfully.\nThank you for your continued efforts.\n...we hope you don't mind doing a bit more work for us.\n\nnow, there is another file we need. 8m.enc was only half of it.\nWe need another file, it is called 9m.enc,\nfrom biolabs.com, we need it decrypted as well.\n\nGood Luck."
                        self.mail.add_message(
                            from_user="security.com",
                            subject="MailingListNews",
                            message=security_message,
                        )
                        self.mail.add_message(
                            from_user="zrio", subject="decryption", message=zrio_message
                        )
                        return
                    case "9m.enc":
                        zrio_message = "I see that have developed a good working relationship.\nThis is the way it should always be.\nSee what else you can find around biolabs...\nPerhaps try biolabs.org, or similar servers.\nThere must be something..."
                        self.mail.add_message(
                            from_user="zrio", subject="Good...", message=zrio_message
                        )
                    case "10m.enc":
                        zrio_message = f"We got the 10m.enc file. It is useless to us.\nCheck for other servers.\n\n\nThere may be something important in this IP range:66.7.1.1 to 66.7.115.255\n\nDig deep, {getuser()}, we are counting on you!"
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
