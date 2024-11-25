from .base_server import BaseServer
from mother.type_defs import FileServerConfig

SERVER_CONFIG: FileServerConfig = {
    "id": "hime_bentekcorp_com",
    "name": "Hime",
    "banner": "Jannet Personal Server",
    "font": "slant",
    "authentication": [("jbvie", "0233260801")],
    "proxy": "hideway.bentekcorp.com",
    "contents": {
        "jbvie": [
            (
                "triad.arc",
                "ARC 1fab2fe4bbd34d6ea19fb3c459b7d92e\n587dea70bbfc4ee0a07f2ef8a1c2ef4c\n8803ce3100e64ac2964cc71e1023002a",
            )
        ]
    },
    "writable": False,
    "crashed": False,
    "hack_tool": "wavehacker",
    "defense_tool": "backmirror3",
}


class HimeBentekcorpCom(BaseServer):
    def ftp(self):
        self.file_server(SERVER_CONFIG)
