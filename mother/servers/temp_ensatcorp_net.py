from .base_server import BaseServer
from mother.type_defs import FileServerConfig

SERVER_CONFIG: FileServerConfig = {
    "id": "temp_ensatcorp_net",
    "name": "ENSAT",
    "banner": "Temporary File Server, do not use for personal data",
    "font": "slant",
    "authentication": [("vlad_ensat", "ch4ng3m3")],
    "proxy": None,
    "contents": {
        "vlad_ensat": [
            ("unreg727.dat", "JDB ENC 27a11def-0b41-4428-8b0f-347c53810f54"),
            (
                "unreg728.dat",
                "PROPERTY OF TELEMARKONE\nDO NOT REDISTRIBUTE\n ENC 0e6f950b-71fb-4769-8ddc-a296a3c0dbcc",
            ),
            ("unreg730.dat", "AH ENC 941b4ebe-b037-4840-ba61-c040e2f9e6da"),
        ]
    },
    "writable": False,
    "crashed": False,
    "hack_tool": None,
    "defense_tool": None,
}


class TempEnsatcorpNet(BaseServer):
    def ftp(self):
        self.file_server(SERVER_CONFIG)
