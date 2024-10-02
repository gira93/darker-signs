from termcolor import cprint
from system.utils import download_file, show_menu
from .base_server import BaseServer


class BiolabsNet(BaseServer):
    def biolabsnethttp(self):
        cprint("Index file not found", "red")
        cprint("--------------------", "red")
        print("FILENAME | SIZE")
        print("[.]")
        print("[..]")
        print("network.info | 1 KB")
        print()

    def xnullb(self):
        while True:
            command = input('Enter Input ("exit" to quit): ')
            if command == "exit":
                break
            if command == "run filecopy.exe network.info":
                print("Downloading network.info...")
                contents = [
                    "NETWORKING INFORMATION FOR BIOLABS",
                    "BIOLABS.COM",
                    "BIOLABS.NET",
                    "BIOLABS.ORG",
                    "RESEARCH.BIOLABS.NET",
                ]
                download_file(f"{self.root_path}/network.info", "\n".join(contents))
                cprint("network.info download complete", "green")
                break

    def biomail(self):
        cprint("Connected to BIOLABS Mail", "green")
        user = input("Enter Username: ")
        pw = input("Enter Password: ")
        if user == "research" and pw == "dolphin":
            cprint("User logged in", "green")
            print("Mailbox:")
            options = [
                "get extra income conditions apply .aff",
                "Re: Dolphin Project Update",
                "AD: Are YOU Paying More than you should on Insurance?",
            ]
            mail_options = [
                "Forward this Email to someone or somewhere",
                "Back to the mail menu",
            ]
            while True:
                selection = show_menu(options)
                match selection:
                    case "1":
                        print()
                        cprint("get extra income conditions apply .aff", "blue")
                        print("This is your chance to open a free online business.")
                        print("Just answer a few over the phone questions and you")
                        print("will be on your way to success.")
                        print()
                        print("Ring (012) 727 7293 when asked say you were")
                        print("referred by mrspammer.")
                        mail_selection = show_menu(mail_options)
                        if mail_selection == "0":
                            break
                        if mail_selection == "1":
                            input("Type a company name to forward to: ")
                            continue
                        else:
                            continue
                    case "2":
                        print()
                        cprint("Re: Dolphin Project Update", "blue")
                        print(
                            "Hi guys... oh my... you have to see this. It's incredible!"
                        )
                        print("We have found the correct link frequency for")
                        print("communication with the dolphins! It's way above the")
                        print("range we expected.")
                        print()
                        print("This is so exciting for me... it really is an amazing")
                        print("breakthrough. I am currently in Arizona attending")
                        print("a meeting with some other researches. Wait until")
                        print("I get back and I will tell you more.")
                        print()
                        print("Frequency: 28.78 GHZ")
                        print("I have found it works best with the bio tuner on a")
                        print("rotating modulation. Don't ask me why yet, but I'm")
                        print("sure we can figure it out when we get back.")
                        print()
                        print("And Dr. Wright... the information you have been")
                        print("waiting for. Remember to keep it private.")
                        print("LATITUDE ENC(S29MS8MS)")
                        print("LONGITUDE ENC(AJ2M2S08S)")
                        print()
                        print("Talk to you all again soon,")
                        print("Adam Carter")
                        mail_selection = show_menu(mail_options)
                        if mail_selection == "0":
                            break
                        if mail_selection == "1":
                            company = input("Type a company name to forward to: ")
                            if company != "zrio":
                                cprint("Unknown company", "red")
                                return
                            zrio_message = "They research on Dolphins then.\nsomething doesn't seems right though;\nthe encrypted part, why put that on a normal email?\nI've decrypted it and found an IP near that location: 66.1.22.2\nit seems unreachable from where I am (maybe firewall blocked)\nkeep searching."
                            self.mail.add_message(
                                from_user="zrio",
                                subject="Re: Email",
                                message=zrio_message,
                            )
                            break
                        else:
                            continue
                    case "3":
                        print()
                        cprint(
                            "AD: Are YOU Paying More than you should on Insurance?",
                            "blue",
                        )
                        print("AXAS Insurance Global")
                        print("Quality personal insurance for you")
                        print("and your family. Find out how just ring")
                        print("(012) 725 2983.")
                        mail_selection = show_menu(mail_options)
                        if mail_selection == "0":
                            break
                        if mail_selection == "1":
                            input("Type a company name to forward to: ")
                            continue
                        else:
                            continue
                    case _:
                        break

        else:
            cprint("User or Password invalid", "red")
            return
