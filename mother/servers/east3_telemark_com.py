from .base_server import BaseServer
from mother.type_defs import FileServerConfig

SERVER_CONFIG: FileServerConfig = {
    "id": "east3_telemark_com",
    "name": "East3",
    "banner": "Eastern Europe Telemark division",
    "font": "speed",
    "authentication": [("admin", "JIT1240892.dmp")],
    "proxy": None,
    "contents": {"admin": []},
    "writable": True,
    "crashed": False,
    "hack_tool": "physicalkey",
    "defense_tool": "backmirror2",
}


class East3TelemarkCom(BaseServer):
    def ftp(self):
        self.file_server(SERVER_CONFIG)
