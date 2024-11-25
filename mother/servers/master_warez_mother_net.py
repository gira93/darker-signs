from .base_server import BaseServer
from mother.type_defs import FileServerConfig

SERVER_CONFIG: FileServerConfig = {
    "id": "master_warez_mother_net",
    "name": "WareZ",
    "banner": "DhYsRhITmi4 little cozy place",
    "font": "doom",
    "authentication": [("DhYsRhITmi4", "e7f2d1799b05403ab63d")],
    "proxy": "warez.mother.net",
    "contents": {"DhYsRhITmi4": [("daily_warez", "d71acd509d224d849bdb828ba8861d37")]},
    "writable": False,
    "crashed": False,
    "hack_tool": "rootbreaker3",
    "defense_tool": "backmirror3",
}


class MasterWarezMotherNet(BaseServer):
    def ftp(self):
        self.file_server(SERVER_CONFIG)
