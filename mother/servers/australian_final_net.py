from .base_server import BaseServer
from mother.type_defs import FileServerConfig

SERVER_CONFIG: FileServerConfig = {
    "id": "australian_final_net",
    "name": "FinalNET",
    "banner": "Australian Division, this is a private server",
    "font": "ntgreek",
    "authentication": [("admin", "5d341749"), ("Papav3ro", "a3a2cc70")],
    "proxy": "athem.final.net",
    "contents": {
        "admin": [],
        "Papav3ro": [("transfer.log", "ENC b1d925b373bd4e8691854c033720361b")],
    },
    "writable": False,
    "crashed": False,
    "hack_tool": "rootbreaker2",
    "defense_tool": "backmirror",
}


class AustralianFinalNet(BaseServer):
    def ftp(self):
        self.file_server(SERVER_CONFIG)
