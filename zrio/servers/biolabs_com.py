from termcolor import cprint
from system.utils import show_menu, download_file
from .base_server import BaseServer


class BiolabsCom(BaseServer):
    def http_biolabs(self):
        cprint("Connected on Port 80 to BIOLABS\nPublic Information Interface", "green")
        print("Biolabs biotechnology research, centered on dolphin intelligence.")
        while True:
            options = ["Our Research", "Dolphin Encounters", "File Database", "Network"]
            selection: str = show_menu(
                options,
                abort_message="Disconnect",
                selection_message="Please select an option",
            )
            print()
            match selection:
                case "1":
                    cprint("Research", "blue")
                    print(
                        "Biolabs focuses most of its efforts on dolphin communication."
                    )
                    print(
                        "We see dolphins in the ocean and can distinguish many of the"
                    )
                    print("individual dolphins by their unique characteristics.")
                    print()
                    print("In our continuing research, we believe we are very close to")
                    print("a breakthrough in this new communication science.")
                    print()
                    input("Press a key")
                case "2":
                    cprint("Dolphin Encounters", "blue")
                    print("The best way to have a dolphin encounter is to spend a week")
                    print(
                        "with us on a group retreat beside the sea. Here you get to really"
                    )
                    print(
                        "learn the ways and guidelines for communicating with dolphins,"
                    )
                    print(
                        "you get to create a pod like community with the other retreaters"
                    )
                    print(
                        "and live right beside the sea on a marine reserve where they"
                    )
                    print("often come to rest and play.")
                    print()
                    print(
                        "The growth in the dolphin communication experience is very powerful."
                    )
                    print()
                    input("Press a key")
                case "3":
                    self.__file_database()
                case "4":
                    cprint("Network", "blue")
                    print(
                        "Restricted to system administrators and biolabs employees only."
                    )
                    print()
                    input("Press a key")
                case _:
                    print("Connection closed")
                    break

    def xnull(self):
        print("Null Connection")
        while True:
            command = input('Enter input ("exit" to quit) ')
            if command == "exit":
                break
            if command == "run filecopy.exe 9m.enc":
                print("Downloading 9m.enc...")
                download_file(
                    f"{self.root_path}/9m.enc", "SUDHMSIHDJAMKAKZYVMKAYVMZVAYAM"
                )
                cprint("Download complete", "green")
                break
        print("Connection closed")

    def __file_database(self) -> None:
        cprint("File Database", "blue")
        print("PUBLIC FILES:")
        print("(none listed)")
        print("PRIVATE FILES:")
        print("1 - 8m.enc")
        while True:
            file_no = input("Enter a file number to download (0 to cancel): ")
            if file_no == "0":
                break
            if file_no == "1":
                print("Downloading 8m.enc...")
                download_file(
                    f"{self.root_path}/8m.enc", "SDKJBSKJDBSKJBHDKJSBHKJDBSKJBDS"
                )
                cprint("Download complete", "green")
                break
