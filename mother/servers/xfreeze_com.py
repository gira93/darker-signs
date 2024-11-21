from .base_server import BaseServer
from mother.type_defs import WebServerConfig

SERVER_CONFIG: WebServerConfig = {
    "id": "xfreeze_com",
    "name": "XFREEZE",
    "banner": "XFreeze, one and only",
    "font": "sblood",
    "authentication": None,
    "proxy": None,
    "contents": [
        {"title": "Who we are?", "content": "Just the most skillful hacker team ever"},
        {
            "title": "Members",
            "content": "You think we write the names of our members here in plain sight?",
        },
        {"title": "Can I join?", "content": "If you're worthy we will call you"},
        {
            "title": "Benefits",
            "content": "Every member gets a personal server in our subnet [user].xfreeze.com\nnot publicly available and with basically infinite power",
        },
    ],
    "writable": False,
    "crashed": False,
    "hack_tool": None,
    "defense_tool": None,
}


class XfreezeCom(BaseServer):
    def http(self):
        self.web_server(SERVER_CONFIG)

