from .base_server import BaseServer
from mother.type_defs import MailServerConfig

SERVER_CONFIG: MailServerConfig = {
    "id": "freemail_com",
    "name": "FreeMail",
    "banner": "The REAL FREE email service",
    "font": "slant",
    "authentication": [("b1t_drv", "3dd6de25"), ("vlad_ensat", "9e655f3b")],
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
    },
    "writable": False,
    "crashed": False,
    "hack_tool": "rootbreaker",
    "defense_tool": None,
}


class FreemailCom(BaseServer):
    def http(self):
        self.mail_server(SERVER_CONFIG)
