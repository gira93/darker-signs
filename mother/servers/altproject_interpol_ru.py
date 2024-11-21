from .base_server import BaseServer
from mother.type_defs import AssignmentServerConfig, RequirementType

SERVER_CONFIG: AssignmentServerConfig = {
    "id": "altproject_interpol_ru",
    "name": "Interpol",
    "banner": "Alt Project Assignment Server",
    "font": "small",
    "authentication": None,
    "proxy": None,
    "contents": [
        {
            "id": "int001",
            "title": "Old acquaintance",
            "description": "Retrieve file from a server",
            "emails": [
                {
                    "from": "altproject@interpol.ru",
                    "subject": "",
                    "attachment": None,
                    "content": "\n".join(
                        [
                            "Do you remember s0ftm4rk? You know the file you removed from Intrapol's public drop?",
                            "I need it back, updated. S0ftm4rk should have it in his personal server at personal.softma.rk",
                        ]
                    ),
                }
            ],
            "exp_needed": 70,
            "credit_reward": 50,
            "exp_reward": 5,
            "requirements": {
                "personal_softma_rk": (
                    RequirementType.FILE_DOWNLOADED,
                    "bank_exchanges.log",
                )
            },
        },
        {
            "id": "int002",
            "title": "Stagna, again",
            "description": "Remove file from a server",
            "emails": [
                {
                    "from": "altproject@interpol.ru",
                    "subject": "",
                    "attachment": None,
                    "content": "\n".join(
                        [
                            "That Paolo Stagna is still under attack, he seems to atract all kind of hackers",
                            'there\'s a malware in his personal server "pstagna.personal.it"',
                            "Find it and remove it."
                            "Usually we don't intervene like that but that malware is bombarding our public drop with files!",
                        ]
                    ),
                }
            ],
            "exp_needed": 75,
            "credit_reward": 50,
            "exp_reward": 5,
            "requirements": {
                "personal_softma_rk": (
                    RequirementType.FILE_NOT_PRESENT,
                    "hotmeat.bin",
                )
            },
        },
        {
            "id": "int003",
            "title": "Vendetta",
            "description": "Crash a server",
            "emails": [
                {
                    "from": "altproject@interpol.ru",
                    "subject": "",
                    "attachment": None,
                    "content": "\n".join(
                        [
                            "We found who uploaded the malware to Stagna's server.",
                            "Someone named n3v3r_MIND from the hacker group xfreeze;",
                            "We need you to find her personal server and just crash it.",
                        ]
                    ),
                }
            ],
            "exp_needed": 170,
            "credit_reward": 50,
            "exp_reward": 10,
            "requirements": {
                "n3v3r_mind_xfreeze_com": (
                    RequirementType.SERVER_CRASHED,
                    "",
                )
            },
        },
    ],
    "writable": False,
    "crashed": False,
    "hack_tool": None,
    "defense_tool": None,
}


class AltprojectInterpolRu(BaseServer):
    def http(self):
        self.assignment_server(SERVER_CONFIG)
