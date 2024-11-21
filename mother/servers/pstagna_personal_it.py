from .base_server import BaseServer
from mother.type_defs import FileServerConfig

SERVER_CONFIG: FileServerConfig = {
    "id": "pstagna_personal_it",
    "name": "Stagna",
    "banner": "Paolo Stagna personal server",
    "font": "standard",
    "authentication": [("pstagna", "83a1d51c")],
    "proxy": None,
    "contents": {
        "pstagna": [
            ("top_anime.txt", "My Top 10 list Anime\n10 - mmm\n9 - ..."),
            ("hotmeat.bin", "37caf0c0c74a44d096df09d685329967"),
        ]
    },
    "writable": True,
    "crashed": False,
    "hack_tool": "rootbreaker",
    "defense_tool": None,
}


class PstagnaPersonalIt(BaseServer):
    def ftp(self):
        self.file_server(SERVER_CONFIG)
