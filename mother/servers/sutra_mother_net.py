from .base_server import BaseServer
from mother.type_defs import WebServerConfig

SERVER_CONFIG: WebServerConfig = {
    "id": "sutra_mother_net",
    "name": "Sutra",
    "banner": "Mother Sutra News Server",
    "font": "doom",
    "authentication": None,
    "proxy": None,
    "contents": [
        {
            "title": "Zrio has fallen",
            "content": "\n".join(
                [
                    "The well known Zrio has finally fallen.",
                    "Recently all the server went down in what seemed like a DDoS attack from the inside.",
                    "The FBI server was also targeted and was succesfully taken down,",
                    "there were no official statements from Zrio representatives",
                ]
            ),
        },
        {
            "title": "We are back ONLINE!",
            "content": "\n".join(
                [
                    "We are back!",
                    "Servers were patched up and bought back online.",
                    "All services as of today are up, running and more secure than ever before",
                ]
            ),
        },
        {
            "title": "New version of Rootbreaker released",
            "content": "\n".join(
                [
                    "A new version of Rootbreaker has been released!",
                    "Remember that every version is not backward compatible,",
                    "this is not a marketing strategy,",
                    "each version is capable of cracking different algorithms!",
                ]
            ),
        },
        {
            "title": "The TelemarkONE big attack",
            "content": "\n".join(
                [
                    "Recently, a huge attack from telecomunication company TelemarkONE has been launched.",
                    "As a result, a lot of Mother hacker's identities were exposed to Interpol.",
                    "Some servers went down and some data leaked,",
                    "details on how this happened are still under investigation.",
                    "This is not the end for Mother, WE WILL FIGHT BACK",
                ]
            ),
        },
    ],
    "writable": False,
    "crashed": False,
    "hack_tool": None,
    "defense_tool": None,
}


class SutraMotherNet(BaseServer):
    def http(self):
        self.web_server(SERVER_CONFIG)
