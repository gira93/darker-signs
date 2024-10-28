from .base_server import BaseServer
from mother.type_defs import AssignmentServerConfig, RequirementType

SERVER_CONFIG: AssignmentServerConfig = {
    "id": "karma_mother_net",
    "name": "Karma",
    "banner": "Karma Assignment Server",
    "font": "sblood",
    "authentication": None,
    "proxy": None,
    "contents": [
        {
            "id": "mtr001",
            "title": "Testing initial mission",
            "description": "Remove a file from a server",
            "mail_content": "You need to remove the file test.txt from a server",
            "mail_from": "karma@mother.net",
            "exp_needed": 0,
            "credit_reward": 100,
            "exp_reward": 100,
            "requirements": {"test_com_filer": (RequirementType.SERVER_CRASHED, "")},
        }
    ],
    "writable": False,
    "crashed": False,
    "hack_tool": None,
    "defense_tool": None,
}


class KarmaMotherNet(BaseServer):
    def http(self):
        self.assignment_server(SERVER_CONFIG)

