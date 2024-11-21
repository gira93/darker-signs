from .base_server import BaseServer
from mother.type_defs import FileServerConfig

SERVER_CONFIG: FileServerConfig = {
    "id": "archives_gs",
    "name": "GameSociety",
    "banner": "File Archive",
    "font": "slant",
    "authentication": [("MAc5", "c4560ed6")],
    "proxy": None,
    "contents": {
        "MAc5": [
            (
                "lineup",
                "\n".join(
                    [
                        "The editorial staff for easy copy n paste into articles:",
                        "- Giovanni Rioni (gi_ri@freemail.com)",
                        "- Franco Tredici (frank_xiii@freemail.com)",
                        "- Manuele Cacciatori (MAc5@freemail.com)",
                        "- Luca Vecchio (lucav@freemail.com)",
                    ]
                ),
            )
        ]
    },
    "writable": False,
    "crashed": False,
    "hack_tool": "rootbreaker2",
    "defense_tool": "backmirror2",
}


class ArchivesGs(BaseServer):
    def ftp(self):
        self.file_server(SERVER_CONFIG)
