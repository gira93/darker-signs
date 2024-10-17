class Commands:
    def __init__(self, root_path: str) -> None:
        self.root_path = root_path

    def available_commands(self) -> list[str]:
        return ["tunnel"]

    def __tunnel(self, _):
        print("tunnel")
