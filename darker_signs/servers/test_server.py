from ..mail import Mail
from ..utils import show_menu


class TestServer:
    def __init__(self, root_path: str, mail: Mail) -> None:
        self.root_path = root_path
        self.mail = mail

    def wingate_proxy(self):
        print("Test Server Web\nWelcome, this is a test server")
        while True:
            options = ["Informations", "Files", "Who we are"]
            selection: str = show_menu(
                options, abort_message="Exit", selection_message="Make a selection"
            )
            print("")
            match selection:
                case "1":
                    print(
                        "Informations\nThis is a very good company doing very good things!"
                    )
                case "2":
                    print("Files")
                case "3":
                    print(
                        "Who we are\nAs said, this is a very good company doing very good things"
                    )
                case "0":
                    print("Connection closed")
                    break
