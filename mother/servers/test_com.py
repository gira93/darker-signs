from .base_server import BaseServer, MailServerConfig, WebServerConfig

SERVER_CONFIG: WebServerConfig = {
    "id": "test_com",
    "name": "Testing Grounds",
    "banner": "Welcome to the Testing Server!",
    "font": "slant",
    "authentication": None,
    "contents": [
        {
            "title": "Test article",
            "content": "Just a test article contents\ncan go in 2 lines also!",
        },
        {
            "title": "Test article numero dos",
            "content": "Just a SECOND test article contents\ncan go in 2 lines also!\nand three!",
        },
    ],
    "writable": False,
    "crashed": False,
    "hack_tool": "nukelord",
    "defense_tool": None,
}

MAIL_SERVER_CONFIG: MailServerConfig = {
    "id": "test_com_mailer",
    "name": "Testing Mailer",
    "banner": "Welcome to the Testing Server Mailer!",
    "font": "doom",
    "authentication": [("franco", "franchi"), ("gino", "gini")],
    "contents": {
        "franco": [
            {
                "from": "gino@pizzi.com",
                "subject": "Hai visto che roba!",
                "content": "Hai visto che roba zio?",
            },
            {
                "from": "paolo@frino.com",
                "subject": "Non sapevo nulla",
                "content": "Giuro che Mother funziona bene\nIo non ne sapevo nulla!",
            },
        ],
        "gino": [
            {
                "from": "fabio@gastani.it",
                "subject": "Ma Paolo Stagna?",
                "content": "Che è successo a Stagna??",
            }
        ],
    },
    "writable": True,
    "crashed": False,
    "hack_tool": "rootbreaker",
    "defense_tool": None,
}


class TestCom(BaseServer):
    def http(self):
        self.web_server(SERVER_CONFIG)

    def mailer(self):
        self.mail_server(MAIL_SERVER_CONFIG)
