from .base_server import BaseServer
from mother.type_defs import FileServerConfig

SERVER_CONFIG: FileServerConfig = {
    "id": "web4_telemark_com",
    "name": "Telemark",
    "banner": "Private temporary server",
    "font": "speed",
    "authentication": [("admin", "8e7d52be")],
    "proxy": "hide.sanandreashubs.com",
    "contents": {"admin": [("kernel.sys", "9b7a749267ae480cb4fc5318d7e4d5d7")]},
    "writable": True,
    "crashed": False,
    "hack_tool": "rootbreaker2",
    "defense_tool": "backmirror2",
}


class Web4TelemarkCom(BaseServer):
    def ftp(self):
        self.file_server(SERVER_CONFIG)
