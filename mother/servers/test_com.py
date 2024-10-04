from .base_server import BaseServer, Files

SERVER_NAME: str = "test.com"
BANNER: str = "Welcome to the best file server ever!"
FILES: Files = [("file1", ""), ("file2", ""), ("file3", "")]


class TestCom(BaseServer):
    def http(self):
        server_config = {"server_name": SERVER_NAME, "files": FILES, "banner": BANNER}
        self.file_server(**server_config)
