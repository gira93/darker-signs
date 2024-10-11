from .base_server import BaseServer, WebServerConfig

SERVER_CONFIG: WebServerConfig = {
    "id": "test_com",
    "banner": "Welcome to the Testing Server!",
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


class TestCom(BaseServer):
    def http(self):
        self.web_server(SERVER_CONFIG)
