import json
import importlib


class Dns:
    def __init__(self, dns_file):
        with open(dns_file, "r") as f:
            self.world = json.load(f)

    def find(self, ip_or_name):
        try:
            server = self.world[ip_or_name]

            if server.get("alias"):
                alias = server["alias"]
                server = self.world[alias]

            return server
        except KeyError:
            print("Server unavailable")
            return None

    def connect(self, server, port, root_path=None, mail=None):
        module_name = f".servers.{server['module_name']}"
        module = importlib.import_module(module_name, "darker_signs")
        cls = getattr(module, server["class_name"])
        srv = cls(root_path, mail)
        method = getattr(srv, port, None)
        if method:
            method()
            return True
        else:
            return False
