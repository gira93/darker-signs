from .base_server import BaseServer
from mother.type_defs import FileServerConfig

SERVER_CONFIG: FileServerConfig = {
    "id": "subcorp_puresun_net",
    "name": "Puresun",
    "banner": "Puresun Subcorp file server, public access is denied",
    "font": "standard",
    "authentication": [("admin", "bb8995a8")],
    "proxy": None,
    "contents": {"admin": [("db_data.bin", "BIN")]},
    "writable": True,
    "crashed": False,
    "hack_tool": "rootbreaker2",
    "defense_tool": None,
}


class SubcorpPuresunNet(BaseServer):
    def ftp(self):
        self.file_server(SERVER_CONFIG)
