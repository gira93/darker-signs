from .base_server import BaseServer
from mother.type_defs import FileServerConfig

SERVER_CONFIG: FileServerConfig = {
    "id": "hammerzone_mother_net",
    "name": "Hammerzone",
    "banner": "admin_hamm3r personal space, get out!",
    "font": "standard",
    "authentication": [("admin_hamm3r", "34fb5051")],
    "proxy": None,
    "contents": {
        "admin_hamm3r": [("bdoor_trace.bin", "BIN 71e96b1d887443d295f89271d474ebac")]
    },
    "writable": False,
    "crashed": False,
    "hack_tool": "rootbreaker2",
    "defense_tool": "backmirror2",
}


class HammerzoneMotherNet(BaseServer):
    def ftp(self):
        self.file_server(SERVER_CONFIG)
