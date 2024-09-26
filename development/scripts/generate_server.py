#!/usr/bin/env python3
import os
import json
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("address")
parser.add_argument("module_name")
parser.add_argument("class_name")
args = parser.parse_args()

cwd = os.getcwd()

with open(f"{cwd}/darker_signs/dns.json", "r") as f:
    dns = json.load(f)

server = dns[args.address]
alias = args.address
if server.get("alias"):
    alias = server["alias"]
    server = dns[alias]

if server["module_name"] != "TODO":
    exit(1)
if server["class_name"] != "TODO":
    exit(1)

module_name = args.module_name
class_name = args.class_name

class_template = [
    "from termcolor import cprint",
    "from darker_signs.dns import Dns",
    "from darker_signs.mail import Mail",
    "",
    "",
    f"class {class_name}:",
    "  def __init__(self, root_path: str, mail: Mail, dns: Dns) -> None:",
    "    self.root_path = root_path",
    "    self.mail = mail",
    "    self.dns = dns",
    "",
]

for port in server["port_mapping"].keys():
    class_template.append(f"  def {server['port_mapping'][port]}(self):")
    class_template.append("    pass")
    class_template.append("")

with open(f"{cwd}/darker_signs/servers/{module_name}.py", "w") as f:
    f.write("\n".join(class_template))

dns[alias]["module_name"] = module_name
dns[alias]["class_name"] = class_name

with open(f"{cwd}/darker_signs/dns.json", "w") as f:
    json.dump(dns, f, indent="\t")
