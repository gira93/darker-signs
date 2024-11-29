from .base_server import BaseServer
from mother.type_defs import CommerceServerConfig

SERVER_CONFIG: CommerceServerConfig = {
    "id": "warez_mother_net",
    "name": "Warez",
    "banner": "Mother Warez Software Server",
    "font": "doom",
    "authentication": None,
    "proxy": None,
    "contents": [
        (
            "rootbreaker",
            "Password cracker\nFirst version of the famous password cracker.\nTo use it: type 'rootbreaker' in place of the user password\nYou need to know a valid username first!",
            5,
        ),
        (
            "rootbreaker2",
            "Password cracker\nSecond version of the famous password cracker.\nTo use it: type 'rootbreaker2' in place of the user password\nYou need to know a valid username first!",
            20,
        ),
        (
            "rootbreaker3",
            "Password cracker\nLatest version of the famous password cracker.\nTo use it: type 'rootbreaker3' in place of the user password\nYou need to know a valid username first!",
            50,
        ),
        (
            "wavehacker",
            "Voice authentication cracker\nIt will bridge a real phone call to the voice authentication service on the server.\nYou need to insert a valid phone number in place of the password.\nAlso you need to know a valid username first!",
            70,
        ),
        (
            "backmirror",
            "Trace diversion\nDefensive tool against server with tracing software.",
            15,
        ),
        (
            "backmirror2",
            "Trace diversion\nDefensive tool against server with tracing software, second version.",
            50,
        ),
        (
            "backmirror3",
            "Trace diversion\nDefensive tool against server with tracing software, latest version.",
            70,
        ),
    ],
    "writable": False,
    "crashed": False,
    "hack_tool": None,
    "defense_tool": None,
}


class WarezMotherNet(BaseServer):
    def http(self):
        self.commerce_server(SERVER_CONFIG)
