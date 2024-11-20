from .base_server import BaseServer
from mother.type_defs import FileServerConfig, DbServerConfig

DB_SERVER_CONFIG: DbServerConfig = {
    "id": "interpol_gov_db",
    "name": "Interpol",
    "banner": "Internal Record Database, unauthorized access will be punished",
    "font": "small",
    "authentication": [("admin", "c3e45b49")],
    "proxy": None,
    "contents": [
        {
            "title": "s0ftm4rk",
            "content": "\n".join(
                [
                    "Alleged money stealing scam",
                    "",
                    "The subject in question allegedly stole different amount of money",
                    "in various currencies from bank servers.",
                    "This was achieved with targeted phishing emails sent to account holders;",
                    "the veridicity of said informations has not yet been validated",
                ]
            ),
        },
        {
            "title": "SirBrown",
            "content": "\n".join(
                [
                    "Spyware in corporate server",
                    "",
                    "Wes Browning, aka: SirBrown has been reported by Bentek to have installed a spyware",
                    "into the main FinalNET server;",
                    "the case has been closed by FinalNET itself who didn't want to proceed",
                    "Consider this record deleted.",
                ]
            ),
        },
        {
            "title": "Paolo Stagna",
            "content": "\n".join(
                [
                    "Virus in corporate server",
                    "",
                    "Paolo Stagna was arrested yesterday on suspicion of hacking and installing a virus",
                    "on a Wellmark server, the company he was working with.",
                    "We are working on the case, Stagna does not have an hacking background",
                    "and is not that tech savvy.",
                    "Maybe he was being used by a third party",
                ]
            ),
        },
    ],
    "writable": False,
    "crashed": False,
    "hack_tool": "rootbreaker",
    "defense_tool": None,
}

FILE_SERVER_CONFIG: FileServerConfig = {
    "id": "interpol_gov_file",
    "name": "Public Drop",
    "banner": "Public Drop Server, login as user guest with pass guest",
    "font": "small",
    "authentication": [("guest", "guest")],
    "proxy": None,
    "contents": {
        "guest": [
            (
                "s0ftm4rk_temp.doc",
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
    "writable": True,
    "crashed": False,
    "hack_tool": None,
    "defense_tool": None,
}


class InterpolGov(BaseServer):
    def record_database(self):
        self.db_server(DB_SERVER_CONFIG)

    def public_drop(self):
        self.file_server(FILE_SERVER_CONFIG)
