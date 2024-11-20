from .base_server import BaseServer
from mother.type_defs import FileServerConfig

SERVER_CONFIG: FileServerConfig = {
    "id": "file_wellmark_com",
    "name": "Wellmark",
    "banner": "Wellmark file server, guest login active",
    "font": "standard",
    "authentication": [("guest", "guest"), ("admin", "rocco")],
    "proxy": None,
    "contents": {
        "guest": [("temp.doc", "Just a test doc, guest access works"), ("rocco", "")],
        "admin": [
            (
                "hr_report.doc",
                "File is digitally signed: Mauro Roberti\nI have found a way to get rid of Stagna\nI just have to upload this virus and you do the rest.\nMake sure no one read this document",
            )
        ],
    },
    "writable": False,
    "crashed": False,
    "hack_tool": None,
    "defense_tool": "backmirror",
}


class FileWellmarkCom(BaseServer):
    def ftp(self):
        self.file_server(SERVER_CONFIG)
