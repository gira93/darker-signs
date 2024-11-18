from .base_server import BaseServer
from mother.type_defs import MailServerConfig

SERVER_CONFIG: MailServerConfig = {
    "id": "kyotomail_jp",
    "name": "Kyotomail",
    "banner": "Personal Free Email only for japanese users!",
    "font": "standard",
    "authentication": [("mw_lo", "80ae5278")],
    "proxy": None,
    "contents": {
        "mw_lo": [
            {
                "from": "anonymous@telemark.com",
                "subject": "Interesting docs",
                "content": "\n".join(
                    [
                        "Hello Ming",
                        "Attached you'll find the documents you requested.",
                        "Do not share them in any way.",
                        "",
                        "Attached files: admins.doc, high_ranks.doc, new_users.doc",
                    ]
                ),
            },
            {
                "from": "b1t_drv@freemail.com",
                "subject": "The software",
                "content": "\n".join(
                    [
                        "Hey noob,",
                        "Here's the software you wanted",
                        "Have fun and don't get caught!",
                        "",
                        "Attachments: l0tt0_d3str0y3r.exe",
                    ]
                ),
            },
        ]
    },
    "writable": True,
    "crashed": False,
    "hack_tool": "rootbreaker",
    "defense_tool": None,
}


class KyotomailJp(BaseServer):
    def http(self):
        self.mail_server(SERVER_CONFIG)
