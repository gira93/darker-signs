from .base_server import BaseServer
from mother.type_defs import FileServerConfig

SERVER_CONFIG: FileServerConfig = {
    "id": "hime_bentekcorp_com",
    "name": "Hime",
    "banner": "Jannet Personal Server",
    "font": "slant",
    "authentication": [("jbvie", "0123456")],
    "proxy": None,
    "contents": {"jbvie": []},
    "writable": False,
    "crashed": False,
    "hack_tool": "rootbreaker3",
    "defense_tool": "backmirror3",
}


class HimeBentekcorpCom(BaseServer):
    def ftp(self):
        self.file_server(SERVER_CONFIG)
