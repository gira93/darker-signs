from .base_server import BaseServer
from mother.type_defs import WebServerConfig

SERVER_CONFIG: WebServerConfig = {
    "id": "wellmark_com",
    "name": "Wellmark",
    "banner": "VoIP made easy",
    "font": "standard",
    "authentication": None,
    "proxy": None,
    "contents": [
        {
            "title": "Who we are?",
            "content": "We are a telecomunication company specialised in VoIP technology.\nWe work for companies both small and big",
        },
        {
            "title": "Products",
            "content": "We offer a variety of products ranging from office phones to full room meet setup.\nContact our sales dept. for more info",
        },
        {
            "title": "Other Services",
            "content": 'We also offer other services:\n- Network setup\n- Sysadmin help\n- Public FTP access (available at "file.wellmark.com")',
        },
    ],
    "writable": False,
    "crashed": False,
    "hack_tool": None,
    "defense_tool": None,
}


class WellmarkCom(BaseServer):
    def http(self):
        self.web_server(SERVER_CONFIG)

