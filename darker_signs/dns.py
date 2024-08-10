import json


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
