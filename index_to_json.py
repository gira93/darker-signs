#!/usr/bin/env python3
import json

index_file = "./others/index.dsh"
new_index = {}

with open(index_file, "r") as f:
    index = f.readlines()

for item in index:
    entry = item.split("%")[1].rstrip()
    dns = entry.split("#")
    ip = dns[0]
    name = dns[1]
    ports = {}
    with open(f"./others/{ip}.svf") as srv:
        for line in srv:
            if line.startswith("port%"):
                protocol = line.split("%")[1].rstrip()
                port = protocol.split("#")[0]
                method = protocol.split("#")[1]
                ports[port] = method
    new_index[name] = {"alias": ip}
    new_index[ip] = {
        "name": name,
        "module_name": "TODO",
        "class_name": "TODO",
        "port_mapping": ports,
    }

with open("./dns.json", "w") as f:
    json.dump(new_index, f, indent="\t")
