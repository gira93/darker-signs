from .base_server import BaseServer
from mother.type_defs import FileServerConfig

SERVER_CONFIG: FileServerConfig = {
    "id": "bentekmail_com",
    "name": "Bentek",
    "banner": "Bentek private server",
    "font": "short",
    "authentication": [("j.debout", "ab13ac4d")],
    "proxy": "hideway.bentekcorp.com",
    "contents": {
        "j.debout": [
            (
                "triad.doc",
                "\n".join(
                    [
                        "The Triad and his Masters",
                        "karma.mother.net -- mirror of master.karma.mother.net -- abDUCtion",
                        "sutra.mother.net -- mirror of master.sutra.mother.net -- Betruger",
                        "warez.mother.net -- mirror of master.warez.mother.net -- DhYsRhITmi4",
                        "",
                        "Every public server is a mirror of his master",
                        "For added security they connect only once a day, exchanging a security key",
                        "provided by the admin of each server.",
                        "master servers are isolated from public networks and can't communicate between each other.",
                    ]
                ),
            ),
            (
                "mother.doc",
                "\n".join(
                    [
                        "Mother of Network Control",
                        "This project aims to acquire control of the network by creating a big botnet.",
                        "The first step is to develop a free OS, make it accessible and secure.",
                        "Create a community around it, hire hackers.",
                        "ZRIO needs to be taken out of business, they know what we want to do, actually they had the idea first!",
                        "A big event needs to occur so that we can force an update containing a backdoor,",
                        "the community won't ask question if this is for the greater good;"
                        "We'll use that to control all computers in the network and have them be a part of a big botnet.",
                        "We then sell data, identities and documents to big corporations",
                        "A network were we create and control industrial espionage and keep the balance as we like it.",
                    ]
                ),
            ),
        ]
    },
    "writable": False,
    "crashed": False,
    "hack_tool": "rootbreaker3",
    "defense_tool": "backmirror3",
}


class BentekmailCom(BaseServer):
    def ftp(self):
        self.file_server(SERVER_CONFIG)
