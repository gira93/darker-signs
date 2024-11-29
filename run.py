#!/usr/bin/env python3
import os
import shutil
import json
from termcolor import cprint
from system.cli import Cli


def main():
    local_base_path, campaign_path, campaign_name, show_intro = setup()
    cli = Cli(
        local_base_path=f"{local_base_path}", campaign_name=campaign_name, host="ds.net"
    )
    os.system("cls||clear")
    cprint("//////////////////", "light_blue")
    cprint("// Darker Signs //", "light_blue")
    cprint("//////////////////", "light_blue")
    print()
    if show_intro:
        with open(f"{local_base_path}/rootfs/system/player.json", "r") as f:
            player = json.load(f)
        with open(f"{local_base_path}/rootfs/system/player.json", "w") as f:
            player["show_intro"] = False
            json.dump(player, f, indent="\t")

        with open(f"{campaign_path}/base_rootfs/intro.txt", "r") as f:
            print(f.read())
    cli.run()


def setup() -> tuple[str, str, str, bool]:
    local_base_path = os.path.dirname(os.path.abspath(__file__))
    rootfs = f"{local_base_path}/rootfs"
    first_run = False
    if os.path.isdir(rootfs):
        with open(f"{rootfs}/system/player.json", "r") as f:
            player = json.load(f)
        campaign_name = player["campaign"]
        show_intro = player["show_intro"]
    else:
        show_intro = True
        first_run = True
        campaign_name = "zrio"

    campaign_path = f"{local_base_path}/{campaign_name}"
    if first_run:
        initialize(local_base_path, campaign_path)
    return local_base_path, campaign_path, campaign_name, show_intro


def initialize(local_base_path: str, campaign_path: str) -> None:
    rootfs = f"{local_base_path}/rootfs"
    base = f"{campaign_path}/base_rootfs"
    if not os.path.isdir(base):
        print("INIT ERROR, please redownload the source code")
        exit(1)
    os.chdir(local_base_path)
    os.makedirs("./rootfs/system")
    shutil.copyfile(f"{base}/system/mail.json", f"{rootfs}/system/mail.json")
    shutil.copyfile(f"{base}/system/player.json", f"{rootfs}/system/player.json")
    shutil.copyfile(f"{base}/readme.txt", f"{rootfs}/readme.txt")


if __name__ == "__main__":
    main()
