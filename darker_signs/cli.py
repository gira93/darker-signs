import os
from getpass import getuser

AVAILABLE_COMMANDS = ["ls", "cd", "cat", "scan", "connect", "mail", "help", "exit"]


class Cli:
    def __init__(self, root_path):
        self.root_path = root_path
        self.real_path = root_path
        self.current_path = ""
        os.chdir(self.real_path)

    def run(self):
        while True:
            typed_command = input(f"{getuser()}@ds.net [{self.current_path}]: ")
            command = typed_command.split(" ")[0]
            params = typed_command.split(" ")[1:]
            if command in AVAILABLE_COMMANDS:
                method = getattr(self, f"_{self.__class__.__name__}__{command}", None)
                if method:
                    method(params)
                else:
                    print("Command implementation not found")
            elif command == "":
                continue
            else:
                print('Command not found, type "help" to view available commands')

    def __ls(self, _):
        _, dirs, files = next(os.walk(self.real_path))
        print(" ".join(map(lambda dir: f"[{dir}]", dirs)))
        print(" ".join(files))
        return True

    def __cd(self, params):
        try:
            folder = params[0]
            if folder == "":
                raise NameError
            if not os.path.isdir(f"{self.real_path}/{folder}"):
                raise NameError
        except (IndexError, NameError) as _:
            print("No folder specified")
            return False

        if folder == ".." and self.current_path == "":
            return False

        os.chdir(f"{self.real_path}/{folder}")
        self.real_path = os.getcwd()
        if self.real_path == self.root_path:
            self.current_path = ""
        else:
            self.current_path = folder
        return True

    def __cat(self, params):
        try:
            file = params[0]
            if file == "":
                raise NameError
            if not os.path.isfile(f"{self.real_path}/{file}"):
                raise NameError
        except (IndexError, NameError):
            print("No file specified")
            return False

        with open(f"{self.real_path}/{file}", "r") as f:
            print(f.read())
        return True

    def __help(self, _):
        print("Available commands:")
        print(" ".join(AVAILABLE_COMMANDS))

    def __exit(self, _):
        exit(0)
