from termcolor import cprint
from system.utils import show_menu
from .base_server import BaseServer


class ResearchBiolabsNet(BaseServer):
    def biolabsresearchhttp(self):
        cprint("Biolabs Private Dolphin Research Server", "green")
        cprint("Password required for username: research", "yellow")
        pw = input("Enter password: ")
        if pw != "dolphin":
            cprint("Wrong Password, connection closed", "red")
            return
        options = [
            "View shared file: dolphin_partial_019.dat",
            "View shared file: dolphin_partial_020.dat",
        ]
        while True:
            selection = show_menu(options)
            match selection:
                case "1":
                    print()
                    cprint("View shared file: dolphin_partial_019.dat", "blue")
                    print(
                        "Bottle-nosed dolphins dominate many marine acts because of their"
                    )
                    print(
                        "intelligence and researchers believe much of the dolphin's brain is"
                    )
                    print('used for communication or "echolocation".')
                    print()
                    print(
                        "While it is not known if dolphins have a formal language, they do"
                    )
                    print(
                        "communicate with a signature whistle to identify themselves."
                    )
                    print()
                    print("Unlike humans, dolphins lack vocal cords, but they do use a")
                    print("complicated system of whistles, squeaks, moans, trills and")
                    print("clicks produced by sphincter muscles within the blow hole.")
                    input("Press a key")
                    continue
                case "2":
                    print()
                    cprint("View shared file: dolphin_partial_020.dat", "blue")
                    print("Using echolocation, or sonar, dolphins send out frequencies")
                    print("by clicking. The clicking sounds bounce off objects and the")
                    print("returning sound waves are picked up by the dolphin's")
                    print("bulbous forehead and lower jaw and interpreted as to")
                    print("distance, size and shape of object.")
                    print(
                        "This sound system is particularly useful at night or in murky"
                    )
                    print("waters such as the Delaware Bay as it allows the dolphin to")
                    print("navigate even if visibility is poor.")
                    print()
                    print(
                        "Dolphins have produced sound frequencies from 0.25 to 200 kHz,"
                    )
                    print(
                        "using the higher frequencies for echolocation and the lower frequencies"
                    )
                    print("for communication and orientation.")
                    input("Press a key")
                case _:
                    return
