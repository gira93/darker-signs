from .base_server import BaseServer
from mother.type_defs import WebServerConfig

SERVER_CONFIG: WebServerConfig = {
    "id": "privteam_telemark_com",
    "name": "",
    "banner": "",
    "font": "standard",
    "authentication": None,
    "proxy": None,
    "contents": [],
    "writable": False,
    "crashed": False,
    "hack_tool": None,
    "defense_tool": None,
}


class PrivteamTelemarkCom(BaseServer):
    def http(self):
        self.web_server(SERVER_CONFIG)

