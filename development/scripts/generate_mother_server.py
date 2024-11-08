#!/usr/bin/env python3

import os
import json
import random
import ipaddress
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("host")
args = parser.parse_args()

cwd = os.getcwd()

with open(f"{cwd}/mother/dns.json", "r") as f:
    dns = json.load(f)

host: str = args.host
host_segments: list[str] = host.split(".")
module_name = "_".join(host_segments)
class_name = "".join(segment.capitalize() for segment in host_segments)
config_id = module_name
server_ip = None

while server_ip is None:
    # Generate a random IPv4 address
    ip = ipaddress.IPv4Address(random.randint(0, (1 << 32) - 1))

    if ip.is_global:
        server_ip = str(ip)

print(f"Host: {host}")
print(f"Module name: {module_name}")
print(f"Class name: {class_name}")
print(f"Config ID: {config_id}")
print(f"IP: {server_ip}")
print()
confirm = input("OK to continue?(y/N): ")

if confirm != "y":
    print("Bye")
    exit(0)

class_template = [
    "from .base_server import BaseServer",
    "from mother.type_defs import WebServerConfig",
    "",
    "SERVER_CONFIG: WebServerConfig = {",
    f'  "id": "{config_id}",',
    '  "name": "", "banner": "", "font": "standard", "authentication": None,',
    '  "proxy": None, "contents": [], "writable": False, "crashed": False, "hack_tool": None, "defense_tool": None,',
    "}",
    "",
    "",
    f"class {class_name}(BaseServer):",
    "  def http(self):",
    "    self.web_server(SERVER_CONFIG)",
]

with open(f"{cwd}/mother/servers/{module_name}.py", "w") as f:
    f.write("\n".join(class_template))

dns[host] = {}
dns[host]["alias"] = server_ip
dns[server_ip] = {}
dns[server_ip]["name"] = host
dns[server_ip]["module_name"] = module_name
dns[server_ip]["class_name"] = class_name
dns[server_ip]["port_mapping"] = {}
dns[server_ip]["port_mapping"]["80"] = "http"


with open(f"{cwd}/mother/dns.json", "w") as f:
    json.dump(dns, f, indent="\t")
