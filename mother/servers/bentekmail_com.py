from .base_server import BaseServer
from mother.type_defs import FileServerConfig

SERVER_CONFIG: FileServerConfig = {
    "id": "bentekmail_com",
    "name": "Bentek",
    "banner": "Bentek private server",
    "font": "short",
    "authentication": [("j.debout", "ab13ac494295044f80379871b36")],
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
                        "provided by the admin of each server, this is only valid for the current day.",
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
                        "The first step is to develop a free OS, make it accessible and secure,",
                        "then create a community around it, an hacking community, with the intent to",
                        '"make the web a better place", the userbase will trust the system.',
                        "ZRIO, our competitor, needs to be taken out of business, they had the same idea",
                        "albeit way smaller, they didn't succeed in building a real community around the project.",
                        "When user trust is at max, we need an excuse to install the backdoor;",
                        "a big event needs to occur so that we can force an update containing said backdoor,",
                        "we simulate a big down time, and have all users update MotherOS to keep it running.",
                        "Once the backdoor is installed, all computers in the network will be part of a bigger botnet;",
                        "This way we can control ALL information that passes through unsuspecting hackers,",
                        "forging every document at will and keeping Bentek on top",
                        "",
                        "Notes: I'll use various nicknames to keep privacy at a maximum",
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
