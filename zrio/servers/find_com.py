from termcolor import cprint
from system.dns import Dns
from system.mail import Mail
from system.utils import show_menu


class FindCom:
    def __init__(self, root_path: str, mail: Mail, dns: Dns) -> None:
        self.root_path = root_path
        self.mail = mail
        self.dns = dns

    def http_find(self):
        print()
        print("FIND.com")
        print("Internet Resources")
        options = [
            "Jobs on FIND.com",
            "Writing a Review",
            "Domains and Registration",
            "Latest News",
            "Online Services",
        ]
        while True:
            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
            selection = show_menu(options)
            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
            match selection:
                case "1":
                    cprint("FIND.com - Jobs", "blue")
                    print(
                        "Using the Internet to find a new job has come a long way from the"
                    )
                    print(
                        "early sprinkling of email lists and Usenet groups that advertised opening"
                    )
                    print(
                        "to the once-geeky Internet community of the 1980's. Today, web-based"
                    )
                    print(
                        "career sources offer job databases where you can find new jobs and"
                    )
                    print(
                        "apply directly online. Its not just for geeks anymore, either."
                    )
                    print()
                    print("Every employer, from fast-food franchises to government")
                    print("agencies and multinational corporations advertise online. ")
                    print("FIND.com will have more infomation on jobs soon.")
                    print()
                    input("Press a key")
                    continue
                case "2":
                    cprint("FIND.com - Writing", "blue")
                    print("In the introduction, you should...")
                    print()
                    print(
                        "Define or identify the general topic, issue, or area of concern,"
                    )
                    print(
                        "thus providing an appropriate context for reviewing the literature."
                    )
                    print()
                    print(
                        "Point out overall trends in what has been published about the topic;"
                    )
                    print(
                        "or conflicts in theory, methodology, evidence, and conclusions; or"
                    )
                    print(
                        "gaps in research and scholarship; or a single problem or new"
                    )
                    print("perspective of immediate interest.")
                    print()
                    print(
                        "Establish the writer's reason (point of view) for reviewing the"
                    )
                    print(
                        "literature; explain the criteria to be used in analyzing and comparing"
                    )
                    print(
                        "literature and the organization of the review (sequence); and, when"
                    )
                    print(
                        "necessary, state why certain literature is or is not included (scope)."
                    )
                    print()
                    print("Writing the body In the body, you should...")
                    print()
                    print("Group research studies and other types of literature")
                    print(
                        "(reviews, theoretical articles, case studies, etc.) according to common"
                    )
                    print(
                        "denominators such as qualitative versus quantitative approaches,"
                    )
                    print(
                        "conclusions of authors, specific purpose or objective, chronology, etc."
                    )
                    print()
                    print(
                        "Summarize individual studies or articles with as much or as little"
                    )
                    print(
                        "detail as each merits according to its comparative importance in the"
                    )
                    print(
                        "literature, remembering that space (length) denotes significance."
                    )
                    print()
                    print(
                        'Provide the reader with strong "umbrella" sentences at beginnings of'
                    )
                    print(
                        'paragraphs, "signposts" throughout, and brief "so what" summary'
                    )
                    print(
                        "sentences at intermediate points in the review to aid in understanding"
                    )
                    print("comparisons and analyses.")
                    print()
                    print("Writing the conclusion In the conclusion, you should...")
                    print()
                    print(
                        "Summarize major contributions of significant studies and articles"
                    )
                    print(
                        "to the body of knowledge under review, maintaining the focus"
                    )
                    print("established in the introduction.")
                    print()
                    print(
                        'Evaluate the current "state of the art" for the body of knowledge reviewed,'
                    )
                    print(
                        "pointing out major methodological flaws or gaps in research, inconsistencies"
                    )
                    print(
                        "in theory and findings, and areas or issues pertinent to future study."
                    )
                    print()
                    print(
                        "Conclude by providing some insight into the relationship between the"
                    )
                    print(
                        "central topic of the literature review and a larger area of study such"
                    )
                    print("as a discipline, a scientific endeavor, or a profession.")
                    print()
                    input("Press a key")
                    continue
                case "3":
                    cprint("FIND.com - Domains and Registration")
                    print("What is the domain name system?")
                    print()
                    print("The Domain Name System (DNS) helps users to find their way")
                    print(
                        "around the Internet. Every computer on the Internet has a unique"
                    )
                    print(
                        "address - just like a telephone number - which is a rather complicated"
                    )
                    print(
                        'string of numbers. It is called its "IP address" (IP stands for "Internet Protocol").'
                    )
                    print()
                    print(
                        "IP Addresses are hard to remember. The DNS makes using the Internet"
                    )
                    print(
                        'easier by allowing a familiar string of letters (the "domain name") to be'
                    )
                    print(
                        "used instead of the arcane IP address. So instead of typing 207.151.159.3,"
                    )
                    print(
                        'you can type internic.net. It is a "mnemonic" device that makes'
                    )
                    print("addresses easier to remember.")
                    print()
                    input("Press a key")
                    continue
                case "4":
                    cprint("FIND.com - Latest News", "blue")
                    print("Big Bubbles in Bermuda Triangle")
                    print()
                    print(
                        "some scientists think giant gas bubbles in the Bermuda Triangle could"
                    )
                    print(
                        "be what is sucking ships down into the deep. Hollywood special effects artist Phil Beck,"
                    )
                    print(
                        "of Awesome FX, has recreated the phenomenon in order to test this theory. "
                    )
                    print()
                    print("Terminal Zero Releases Dark Signs")
                    print()
                    print(
                        "An Australian based software development company Terminal Zero has recently"
                    )
                    print(
                        "released its groundbreaking new hacking and cracking game - Dark Signs."
                    )
                    print()
                    print("The fish are really big!")
                    print()
                    print(
                        "Scientists researching deep in the pacific have found the largest sea creatures"
                    )
                    print(
                        "known to exist! They know believe that the deeper they go, the larger the life"
                    )
                    print("they will find.")
                    print()
                    input("Press a key")
                    continue
                case "5":
                    cprint("FIND.com - Online Services", "blue")
                    print(
                        "FIND.com offers services including web hosting, database management,"
                    )
                    print("internet access, and much more.")
                    print()
                    print(
                        "FIND.com can also provide online services including security for online businesses, as"
                    )
                    print(
                        "well as provide information and system upgrades, for example the recent bug in"
                    )
                    print(
                        "a version of remote resource servers that allows the user open http access"
                    )
                    print(
                        "if the key code is RRS441 and for more information regarding our services, please"
                    )
                    print("contact us by phone +613 7528288 (Business Hours Only) ")
                    print()
                    input("Press a key")
                    continue
                case _:
                    break
