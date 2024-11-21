from .base_server import BaseServer
from mother.type_defs import FileServerConfig

SERVER_CONFIG: FileServerConfig = {
    "id": "personal_softma_rk",
    "name": "S0ftm4rk",
    "banner": "Personal space, PLEASE STOP HACKING IT!",
    "font": "standard",
    "authentication": [("s0ftm4rk", "379a47baabd2")],
    "proxy": None,
    "contents": {
        "s0ftm4rk": [
            (
                "bank_exchanges.log",
                "\n".join(
                    [
                        "User login: admin",
                        "IP: 21.40.3.31",
                        "Action: Withdrawal",
                        "Amount: 10000 usd",
                        "",
                        "User login: admin",
                        "IP: 21.40.3.31",
                        "Action: Withdrawal",
                        "Amount: 9000 gbp",
                        "",
                        "User login: admin",
                        "IP: 21.40.3.31",
                        "Action: Withdrawal",
                        "Amount: 9000 usd",
                    ]
                ),
            )
        ]
    },
    "writable": False,
    "crashed": False,
    "hack_tool": "rootbreaker",
    "defense_tool": None,
}


class PersonalSoftmaRk(BaseServer):
    def ftp(self):
        self.file_server(SERVER_CONFIG)
