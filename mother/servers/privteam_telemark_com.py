from .base_server import BaseServer
from mother.type_defs import FileServerConfig

SERVER_CONFIG: FileServerConfig = {
    "id": "privteam_telemark_com",
    "name": "PrivTeam",
    "banner": "Telemark private drop server",
    "font": "speed",
    "authentication": [("admin", "e55fc39b"), ("ambroz", "d0b3c301")],
    "proxy": None,
    "contents": {
        "admin": [
            (
                "access.log",
                "\n".join(
                    [
                        "ambroz -- logged in",
                        "admin -- package upgrade",
                        "admin -- system cleanup",
                        "ambroz -- uploaded file test.txt",
                        "ambroz -- deleted file test.txt",
                        "admin -- activated key dump service",
                        "ambroz -- dumped key to JIT1240892.dmp",
                        "ambroz -- logged out",
                        "admin -- logged out",
                    ]
                ),
            )
        ],
        "ambroz": [("JIT1240892.dmp", "3a233c76addc48968b96d2ced2f03dac")],
    },
    "writable": False,
    "crashed": False,
    "hack_tool": "rootbreaker2",
    "defense_tool": "backmirror2",
}


class PrivteamTelemarkCom(BaseServer):
    def ftp(self):
        self.file_server(SERVER_CONFIG)
