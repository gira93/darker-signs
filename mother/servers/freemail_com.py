from .base_server import BaseServer
from mother.type_defs import MailServerConfig

SERVER_CONFIG: MailServerConfig = {
    "id": "freemail_com",
    "name": "FreeMail",
    "banner": "The REAL FREE email service",
    "font": "slant",
    "authentication": [
        ("b1t_drv", "3dd6de25"),
        ("vlad_ensat", "9e655f3b"),
        ("MeaTPloW", "56e18637"),
        ("admin_hamm3r", "0e0c7541"),
        ("lyana", "c7e60456"),
    ],
    "proxy": None,
    "contents": {
        "b1t_drv": [
            {
                "from": "no-one@xyz.net",
                "subject": "You think it will work?",
                "content": "You think the software bait will work?\nLike, really work?",
            }
        ],
        "vlad_ensat": [
            {
                "from": "it@ensatcorp.net",
                "subject": "Temporary server access",
                "content": "Your temporary account has been activated, here's the details:\nUser: vlad_ensat\nPass: ch4ng3m3\nRemember to change the password even if it's a temporary account",
            }
        ],
        "MeaTPloW": [
            {
                "from": "Papav3ro@australian.final.net <athem.final.net>",
                "subject": "The tool",
                "content": "Here's the tool you wanted, just don't run it locally xd",
            },
        ],
        "admin_hamm3r": [
            {
                "from": "lyana@freemail.com",
                "subject": "Do you know MotherOS?",
                "content": "I'm in the search of the most secure OS, some say it's MotherOS, you worked on that didn't you?",
            },
            {
                "from": "internal@telemark.com <hide.sanandreashubs.com>",
                "subject": "Survey",
                "content": "Hello Howard,\nPlease fill in the following feedback survey by the end of the month.\nThank you",
            },
        ],
        "lyana": [
            {
                "from": "admin_hamm3r@telemark.com <hide.sanandreashubs.com>",
                "subject": "Re: Do you know MotherOS?",
                "content": 'You crazy? DO NOT USE MOTHER OS!\nI was a beta tester on the project, there\'s a HUGE backdoor in the system!\nI think I left some documents on my old server "hammerzone.mother.net"',
            }
        ],
    },
    "writable": False,
    "crashed": False,
    "hack_tool": "rootbreaker",
    "defense_tool": None,
}


class FreemailCom(BaseServer):
    def http(self):
        self.mail_server(SERVER_CONFIG)
