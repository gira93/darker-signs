from .base_server import BaseServer
from mother.type_defs import FileServerConfig

SERVER_CONFIG: FileServerConfig = {
    "id": "n3v3r_mind_xfreeze_com",
    "name": "XFreeze",
    "banner": "n3v3r_MIND personal server",
    "font": "sblood",
    "authentication": [("n3v3r_MIND", "e91c842cfce24d23")],
    "proxy": "xfreeze.com",
    "contents": {
        "n3v3r_MIND": [
            ("kernel.sys", "894b801201214f269554b3517caac0c4"),
            ("hotmeat.bin", "5fab63e038584e58b4ac7074dbdf68cc"),
        ]
    },
    "writable": True,
    "crashed": False,
    "hack_tool": "rootbreaker3",
    "defense_tool": "backmirror3",
}


class N3v3r_mindXfreezeCom(BaseServer):
    def ftp(self):
        self.file_server(SERVER_CONFIG)

