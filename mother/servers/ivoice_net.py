from .base_server import BaseServer
from mother.type_defs import ChatServerConfig

SERVER_CONFIG: ChatServerConfig = {
    "id": "ivoice_net",
    "name": "IVoice Chat Server",
    "font": "standard",
    "proxy": None,
    "banner": "Welcome to IVoice Community Chat",
    "crashed": False,
    "writable": False,
    "contents": [
        {"op": "mw_lo", "content": "Messaggio test, ciao sono Ming Wo Lo"},
        {"op": "softm", "content": "Ming Wo Lo? chi è?"},
        {"op": "pstagna", "content": "Oh! non lo sapevo, finalNet"},
    ],
    "hack_tool": None,
    "defense_tool": None,
    "authentication": None,
}


class IvoiceNet(BaseServer):
    def http(self):
        self.chat_server(SERVER_CONFIG)
