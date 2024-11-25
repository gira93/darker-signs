from .base_server import BaseServer
from mother.type_defs import FileServerConfig

SERVER_CONFIG: FileServerConfig = {
    "id": "master_karma_mother_net",
    "name": "KarmA",
    "banner": "abDUCtion domain",
    "font": "doom",
    "authentication": [("abDUCtion", "5ff569da")],
    "proxy": "karma.mother.net",
    "contents": {"abDUCtion": [("daily_karma", "5cf2ca3029ca4dafadf1aa467678ee74")]},
    "writable": False,
    "crashed": False,
    "hack_tool": "rootbreaker3",
    "defense_tool": "backmirror3",
}


class MasterKarmaMotherNet(BaseServer):
    def ftp(self):
        self.file_server(SERVER_CONFIG)
