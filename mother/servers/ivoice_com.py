from .base_server import BaseServer
from mother.type_defs import ChatServerConfig

SERVER_CONFIG: ChatServerConfig = {
    "id": "ivoice_com",
    "name": "IVoice Chat Server",
    "font": "standard",
    "proxy": None,
    "banner": "Welcome to IVoice Community Chat",
    "crashed": False,
    "writable": False,
    "contents": [
        {
            "op": "mw_lo",
            "content": "Hello, I'm Ming Woo Lo from Telemark, I need the famous lotto program everyone talks about",
        },
        {"op": "b1t_drv", "content": "Ming Woo Lo? weren't you japanese?"},
        {
            "op": "mw_lo",
            "content": "Ming Woo Lo is a japanese name but I'm American! do you have the software? can you send it to mw_lo@kyotomail.jp?",
        },
    ],
    "hack_tool": None,
    "defense_tool": None,
    "authentication": None,
}


class IvoiceCom(BaseServer):
    def http(self):
        self.chat_server(SERVER_CONFIG)
