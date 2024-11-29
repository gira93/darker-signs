from system.mail import Mail
from system.dns import Dns
from system.player import Player


class BaseServer:
    def __init__(self, root_path: str, mail: Mail, dns: Dns, player: Player) -> None:
        self.root_path = root_path
        self.mail = mail
        self.dns = dns
        self.player = player
