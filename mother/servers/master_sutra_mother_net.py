from .base_server import BaseServer
from mother.type_defs import FileServerConfig

SERVER_CONFIG: FileServerConfig = {
    "id": "master_sutra_mother_net",
    "name": "SutrA",
    "banner": "Betruger lair",
    "font": "doom",
    "authentication": [("Betruger", "e45228f5")],
    "proxy": "sutra.mother.net",
    "contents": {"Betruger": [("daily_part2", "e54d9493")]},
    "writable": False,
    "crashed": False,
    "hack_tool": "rootbreaker3",
    "defense_tool": "backmirror3",
}


class MasterSutraMotherNet(BaseServer):
    def ftp(self):
        self.file_server(SERVER_CONFIG)

