from .base_server import BaseServer
from mother.type_defs import (
    CommerceServerConfig,
    MailServerConfig,
    WebServerConfig,
    FileServerConfig,
    DbServerConfig,
)

SERVER_CONFIG: WebServerConfig = {
    "id": "test_com",
    "name": "Testing Grounds",
    "banner": "Welcome to the Testing Server!",
    "font": "slant",
    "authentication": None,
    "proxy": None,
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
    "proxy": None,
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

FILE_SERVER_CONFIG: FileServerConfig = {
    "id": "test_com_filer",
    "name": "File Grounds",
    "banner": "Welcome to the File Server!",
    "font": "slant",
    "authentication": [("gino", "gini"), ("franco", "franchi")],
    "proxy": "hide.bentekcorp.com",
    "contents": {
        "gino": [
            ("readme.txt", "This is a readme\nHave you read it?"),
            ("another.bin", "Another file dotbin"),
        ],
        "franco": [("franco.md", "franco dotmd"), ("kernel.sys", "KERNELSYS")],
    },
    "writable": True,
    "crashed": False,
    "hack_tool": "rootbreaker2",
    "defense_tool": None,
}

DBSERVER_CONFIG: DbServerConfig = {
    "id": "test_com_db",
    "name": "Testing DB!",
    "banner": "Welcome to the Testing DB",
    "font": "doom",
    "authentication": [("secure", "s3cur3")],
    "proxy": None,
    "contents": [
        {
            "title": "s0ftm4rk",
            "content": "Money robbed and shit",
        },
        {
            "title": "La mietitura di TelemarkONE",
            "content": "The big thing",
        },
    ],
    "writable": False,
    "crashed": False,
    "hack_tool": "rootbreaker3",
    "defense_tool": None,
}

COMMERCESERVER_CONFIG: CommerceServerConfig = {
    "id": "test_com_commerce",
    "name": "Testing Commerce",
    "banner": "Welcome to the Test ECommerce",
    "font": "sblood",
    "authentication": None,
    "proxy": None,
    "contents": [
        ("rootbreaker", "Password cracker\nBasic version", 100),
        ("backmirror", "Defensive tool against server with tracing software", 100),
        ("rootbreaker4", "Updated version of the famous password cracker", 200),
    ],
    "writable": False,
    "crashed": False,
    "hack_tool": None,
    "defense_tool": None,
}


class TestCom(BaseServer):
    def http(self):
        self.web_server(SERVER_CONFIG)

    def mailer(self):
        self.mail_server(MAIL_SERVER_CONFIG)

    def ftp(self):
        self.file_server(FILE_SERVER_CONFIG)

    def db(self):
        self.db_server(DBSERVER_CONFIG)

    def commerce(self):
        self.commerce_server(COMMERCESERVER_CONFIG)
