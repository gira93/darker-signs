#!/usr/bin/env python3
import os
from darker_signs.cli import Cli


def main():
    root_path = os.path.dirname(os.path.abspath(__file__))
    cli = Cli(f"{root_path}")
    os.system("cls||clear")
    cli.run()


if __name__ == "__main__":
    main()
