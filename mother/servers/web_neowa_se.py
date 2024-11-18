from .base_server import BaseServer
from mother.type_defs import FileServerConfig

SERVER_CONFIG: FileServerConfig = {
    "id": "web_neowa_se",
    "name": "Neowase",
    "banner": "This server is only accessible with a web browser",
    "font": "sblood",
    "authentication": [("admin", "ab751b4a")],
    "proxy": None,
    "contents": {"admin": [("kernel.sys", "c2c113ec-0fe7-4247-8ce3-bd6597dd893b")]},
    "writable": True,
    "crashed": False,
    "hack_tool": "rootbreaker",
    "defense_tool": None,
}


class WebNeowaSe(BaseServer):
    def ftp(self):
        self.file_server(SERVER_CONFIG)
