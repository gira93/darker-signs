class Environment:
    def __init__(self, root_path: str) -> None:
        self.root_path = root_path

    def available_commands(self) -> list[str]:
        return ["newcom"]

    def __newcom(self, params: list[str]) -> None:
        print(params)
        print(self.root_path)
