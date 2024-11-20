from .base_server import BaseServer
from mother.type_defs import FileServerConfig

SERVER_CONFIG: FileServerConfig = {
    "id": "athem_final_net",
    "name": "Athem",
    "banner": "A FinalNET Division",
    "font": "ntgreek",
    "authentication": [("sirbrown", "11abee3f")],
    "proxy": None,
    "contents": {
        "admin": [
            ("notes.txt", "- Check the SirBrown guy entry test\n- Talk to JDB about it")
        ],
        "sirbrown": [
            (
                "entry_test.doc",
                "SirBrown\nResult: Passed\nScore: 90/100\nWelcome to FinalNET",
            ),
            ("final_review.doc", "ENC 1d275f4a2c174b81bf85cc8a403813be"),
        ],
    },
    "writable": True,
    "crashed": False,
    "hack_tool": "rootbreaker2",
    "defense_tool": "backmirror",
}


class AthemFinalNet(BaseServer):
    def ftp(self):
        self.file_server(SERVER_CONFIG)
