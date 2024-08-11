import os
import readline
from getpass import getuser
from .utils import progress_bar
from .mail import Mail
from .dns import Dns

AVAILABLE_COMMANDS = ["ls", "cd", "cat", "scan", "connect", "mail", "help", "exit"]


class Cli:
    def __init__(self, root_path):
        rootfs = f"{root_path}/rootfs"
        self.system_path = root_path
        self.root_path = rootfs
        self.real_path = rootfs
        self.current_path = ""
        os.chdir(self.real_path)
        self.mail = Mail(f"{self.root_path}/system/mail.json")
        self.dns = Dns(f"{self.system_path}/darker_signs/dns.json")

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

    def __scan(self, params):
        try:
            server_name = params[0]
            if server_name == "":
                raise NameError
        except (IndexError, NameError):
            print("No server name or IP address specified")
            return False

        server = self.dns.find(server_name)
        if server:
            print(f"Scanning {server['name']}...")
            progress_bar(100, 0.05)
            print(f"Ports open for {server['name']}:")
            for port in server["port_mapping"].keys():
                print(f"{port} -> {server['port_mapping'][port]}")
            return True
        else:
            return False

    def __connect(self, params):
        try:
            server_name = params[0]
            if len(params) == 1:
                port = "80"
            else:
                port = params[1]
            if server_name == "" or port == "":
                raise NameError
        except (IndexError, NameError):
            print("HELP: connect [server ip or name] [port]")
            return False
        server = self.dns.find(server_name)
        if server and port in server["port_mapping"].keys():
            print(f"Connecting to {server['name']}:{port}")
            self.dns.connect(
                server,
                server["port_mapping"][port],
                root_path=self.root_path,
                mail=self.mail,
            )
            return True
        else:
            return False

    def __mail(self, _):
        self.mail.run()

    def __help(self, _):
        print("Available commands:")
        print(" ".join(AVAILABLE_COMMANDS))

    def __exit(self, _):
        exit(0)
