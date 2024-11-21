from .base_server import BaseServer
from mother.type_defs import FileServerConfig

SERVER_CONFIG: FileServerConfig = {
    "id": "main1_meccate_ch",
    "name": "MeccA",
    "banner": "Mecca Technologies Mainframe",
    "font": "doom",
    "authentication": [("admin", "6013879631")],
    "proxy": "shadow.bellavista",
    "contents": {
        "admin": [
            (
                "main.cfg",
                "Main config file\nListen: 36.0.191.36\nPort: 21\nACL: vrls\nACL_Config: vrls.conf",
            ),
            (
                "vrls.conf",
                "# Config override for VRLS\nallow_password: no\nadditional_security: proxy,trace_master_3",
            ),
        ]
    },
    "writable": True,
    "crashed": False,
    "hack_tool": "wavehacker",
    "defense_tool": "backmirror3",
}


class Main1MeccateCh(BaseServer):
    def ftp(self):
        self.file_server(SERVER_CONFIG)
