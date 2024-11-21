from .base_server import BaseServer
from mother.type_defs import FileServerConfig

SERVER_CONFIG: FileServerConfig = {
    "id": "master_mother_net",
    "name": "MotheR",
    "banner": "Mother Master Server",
    "font": "doom",
    "authentication": [("D1l3mm4", "JIT66.dmp")],
    "proxy": None,
    "contents": {"D1l3mm4": [("kernel.sys", "e646ee87ee9b4cf7a2b930d6fa1544eb")]},
    "writable": True,
    "crashed": False,
    "hack_tool": "physicalkey",
    "defense_tool": "backmirror3",
}


class MasterMotherNet(BaseServer):
    def ftp(self):
        self.file_server(SERVER_CONFIG)
