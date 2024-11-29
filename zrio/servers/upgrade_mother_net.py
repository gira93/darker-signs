from termcolor import cprint
from system.utils import progress_bar, reset_rootfs
from .base_server import BaseServer


class UpgradeMotherNet(BaseServer):
    def upgrade(self):
        print()
        cprint("Welcome to the MotherOS upgrade portal\n", "blue")
        print(
            "\n".join(
                [
                    "This website will download and run the upgrade package",
                    "all current data will be lost and the system will be shutdown",
                ]
            )
        )
        print()
        response = input("Continue with the upgrade? (y/N): ")
        if response == "y":
            print()
            cprint("Downloading package...", "green")
            progress_bar()
            cprint("Extracting package...", "green")
            progress_bar(100, 0.03)
            cprint("Applying update...", "green")
            progress_bar()
            self.player.reset()
            self.player.update_campaign("mother")
            self.mail.reset()
            reset_rootfs(self.root_path)
            cprint("Upgrade DONE", "green")
            cprint("The system will shutdown NOW", "yellow")
            cprint("Please restart the system manually", "blue")
            exit(0)
        else:
            cprint("Upgrade aborted! Disconnecting", "red")
