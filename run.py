#!/usr/bin/env python3
import os
from termcolor import cprint
from darker_signs.cli import Cli


def main():
    root_path = os.path.dirname(os.path.abspath(__file__))
    cli = Cli(f"{root_path}")
    os.system("cls||clear")
    cprint("//////////////////", "light_blue")
    cprint("// Darker Signs //", "light_blue")
    cprint("//////////////////", "light_blue")
    print()
    cli.run()


if __name__ == "__main__":
    main()
