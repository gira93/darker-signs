from typing import TypedDict
from termcolor import cprint
from system.mail import Mail
from system.dns import Dns
from system.player import Player

Files = list[tuple[str, str]]
ServerEmail = TypedDict("ServerEmail", {"from": str, "subject": str, "message": str})
MailList = list[ServerEmail]


class BaseServer:
    def __init__(self, root_path: str, mail: Mail, dns: Dns, player: Player) -> None:
        self.root_path = root_path
        self.mail = mail
        self.dns = dns
        self.player = player

    def file_server(self, server_name: str, files: Files, banner: str | None = None):
        self.__welcome(server_name, banner)
        print(files)

    def web_server(self, server_name: str, banner: str | None = None):
        self.__welcome(server_name, banner)
        cprint("This website is only available through a web browser", "red")
        print()

    def mail_server(
        self, server_name: str, mail_list: MailList, banner: str | None = None
    ):
        self.__welcome(server_name, banner)
        print(mail_list)

    def chat_server(self, server_name: str, banner: str | None = None):
        self.__welcome(server_name, banner)

    def __welcome(self, server_name: str, banner: str | None = None):
        welcome_message = banner if banner else f"Welcome to {server_name}"
        cprint(welcome_message, "green")
        print()
