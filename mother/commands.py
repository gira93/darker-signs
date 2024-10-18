from termcolor import cprint
from system.dns import Dns
from system.mail import Mail
from system.player import Player


class Commands:
    def __init__(self, root_path: str, dns: Dns, player: Player, mail: Mail) -> None:
        self.root_path = root_path
        self.dns = dns
        self.player = player
        self.mail = mail

    def available_commands(self) -> list[str]:
        return ["tunnel"]

    def __tunnel(self, params: list[str]) -> None:
        try:
            gateway_name = params[0]
            server_name = params[1]
            if len(params) == 2:
                port = "80"
            else:
                port = params[2]
            if gateway_name == "" or server_name == "" or port == "":
                raise NameError
        except (IndexError, NameError):
            cprint(
                "HELP: tunnel [gateway ip or name] [server ip or name] [port, (default 80)]",
                "red",
            )
            return
        # gateway = self.dns.find(gateway_name)
        server = self.dns.find(server_name)
        if server and (port in server["port_mapping"].keys()):
            print(
                f"Connecting to {server['name']}:{port} tunnel through {gateway_name}"
            )
            print()
            self.dns.connect(
                server,
                server["port_mapping"][port],
                root_path=self.root_path,
                mail=self.mail,
                player=self.player,
            )
            return
        else:
            cprint("Gateway, Server or port not available", "red")
            return
