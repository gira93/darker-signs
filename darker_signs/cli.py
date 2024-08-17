import os
import readline
from getpass import getuser
from termcolor import cprint
from .utils import progress_bar
from .mail import Mail
from .dns import Dns

AVAILABLE_COMMANDS: list[str] = [
    "ls",
    "cd",
    "cat",
    "clear",
    "scan",
    "connect",
    "mail",
    "help",
    "exit",
]


class Cli:
    def __init__(self, root_path: str) -> None:
        rootfs = f"{root_path}/rootfs"
        self.system_path = root_path
        self.root_path = rootfs
        self.real_path = rootfs
        self.current_path = ""
        os.chdir(self.real_path)
        self.mail: Mail = Mail(f"{self.root_path}/system/mail.json")
        self.dns: Dns = Dns(f"{self.system_path}/darker_signs/dns.json")

    def run(self) -> None:
        while True:
            typed_command = input(f"{getuser()}@ds.net [{self.current_path}]: ")
            command = typed_command.split(" ")[0]
            params = typed_command.split(" ")[1:]
            if command in AVAILABLE_COMMANDS:
                method = getattr(self, f"_{self.__class__.__name__}__{command}", None)
                if method:
                    method(params)
                else:
                    cprint("Command implementation not found", "red")
            elif command == "":
                continue
            else:
                cprint(
                    'Command not found, type "help" to view available commands', "red"
                )

    def __ls(self, _) -> bool:
        _, dirs, files = next(os.walk(self.real_path))
        cprint(" ".join(map(lambda dir: f"[{dir}]", dirs)), "light_blue")
        print(" ".join(files))
        return True

    def __cd(self, params: list[str]) -> bool:
        try:
            folder = params[0]
            if folder == "":
                raise NameError
            if not os.path.isdir(f"{self.real_path}/{folder}"):
                raise NameError
        except (IndexError, NameError) as _:
            cprint("No folder specified", "red")
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

    def __cat(self, params: list[str]) -> bool:
        try:
            file = params[0]
            if file == "":
                raise NameError
            if not os.path.isfile(f"{self.real_path}/{file}"):
                raise NameError
        except (IndexError, NameError):
            cprint("No file specified", "red")
            return False

        with open(f"{self.real_path}/{file}", "r") as f:
            print()
            cprint(f.read(), "light_blue")
            print()
        return True

    def __clear(self, _) -> None:
        os.system("cls||clear")

    def __scan(self, params: list[str]) -> bool:
        try:
            server_name = params[0]
            if server_name == "":
                raise NameError
        except (IndexError, NameError):
            cprint("No server name or IP address specified", "red")
            return False

        server = self.dns.find(server_name)
        if server:
            print(f"Scanning {server['name']}...")
            progress_bar(100, 0.05)
            print(f"Ports open for {server['name']}:")
            print()
            for port in server["port_mapping"].keys():
                cprint(f"{port} -> [{server['port_mapping'][port]}]", "light_blue")
            print()
            return True
        else:
            return False

    def __connect(self, params: list[str]) -> bool:
        try:
            server_name = params[0]
            if len(params) == 1:
                port = "80"
            else:
                port = params[1]
            if server_name == "" or port == "":
                raise NameError
        except (IndexError, NameError):
            cprint("HELP: connect [server ip or name] [port]", "red")
            return False
        server = self.dns.find(server_name)
        if server and port in server["port_mapping"].keys():
            print(f"Connecting to {server['name']}:{port}")
            print()
            self.dns.connect(
                server,
                server["port_mapping"][port],
                root_path=self.root_path,
                mail=self.mail,
            )
            return True
        else:
            return False

    def __mail(self, _) -> None:
        self.mail.run()

    def __help(self, _) -> None:
        print("Available commands:")
        print(" ".join(AVAILABLE_COMMANDS))

    def __exit(self, _) -> None:
        print("Bye Bye!")
        exit(0)
