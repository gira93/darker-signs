import json
import importlib
from .mail import Mail


class Dns:
    def __init__(self, dns_file: str, campaign_name: str) -> None:
        self.campaign_name = campaign_name
        with open(dns_file, "r") as f:
            self.world: dict = json.load(f)

    def find(self, ip_or_name: str) -> dict | None:
        try:
            server = self.world[ip_or_name]

            if server.get("alias"):
                alias = server["alias"]
                server = self.world[alias]

            return server
        except KeyError:
            return None

    def connect(
        self,
        server: dict,
        port: str,
        root_path: str | None = None,
        mail: Mail | None = None,
    ) -> bool:
        # TODO -- Remove once every server has been implemented
        if server["module_name"] == "TODO":
            print("Not implemented")
            return False

        module_name = f".servers.{server['module_name']}"
        module = importlib.import_module(module_name, self.campaign_name)
        cls = getattr(module, server["class_name"])
        srv = cls(root_path, mail, self)
        method = getattr(srv, port, None)
        if method:
            method()
            return True
        else:
            return False
