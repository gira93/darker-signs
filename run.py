#!/usr/bin/env python3
import os
import shutil
from termcolor import cprint
from system.cli import Cli


def main():
    campaign_name = "zrio"
    root_path = os.path.dirname(os.path.abspath(__file__))
    campaign_path = f"{root_path}/{campaign_name}"
    first_run = initialize(root_path, campaign_name)
    cli = Cli(f"{root_path}", campaign_name, "ds.net")
    os.system("cls||clear")
    cprint("//////////////////", "light_blue")
    cprint("// Darker Signs //", "light_blue")
    cprint("//////////////////", "light_blue")
    print()
    if first_run:
        with open(f"{campaign_path}/base_rootfs/intro.txt", "r") as f:
            print(f.read())
    cli.run()


def initialize(root_path: str, campaign_path: str) -> bool:
    rootfs = f"{root_path}/rootfs"
    if not os.path.isdir(rootfs):
        base = f"{campaign_path}/base_rootfs"
        if not os.path.isdir(base):
            print("INIT ERROR, please redownload the source code")
            exit(1)
        os.chdir(root_path)
        os.makedirs("./rootfs/system")
        shutil.copyfile(f"{base}/system/mail.json", f"{rootfs}/system/mail.json")
        shutil.copyfile(f"{base}/readme.txt", f"{rootfs}/readme.txt")
        return True
    else:
        return False


if __name__ == "__main__":
    main()
