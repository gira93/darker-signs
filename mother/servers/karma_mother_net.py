from .base_server import BaseServer
from mother.type_defs import AssignmentServerConfig, RequirementType

SERVER_CONFIG: AssignmentServerConfig = {
    "id": "karma_mother_net",
    "name": "Karma",
    "banner": "Mother Karma Assignment Server",
    "font": "doom",
    "authentication": None,
    "proxy": None,
    "contents": [
        {
            "id": "mtr001",
            "title": "The Admission",
            "description": "Remove record from a database server",
            "emails": [
                {
                    "from": "karma@mother.net",
                    "subject": "",
                    "attachment": None,
                    "content": "\n".join(
                        [
                            "S0ftma4rk, a junior member of our community has been recently caught stealing money.",
                            "His file has been sent to interpol.gov public drop server, fortunately they haven't checked it yet;",
                            "your task is simple:",
                            "Get into the public drop server (it shouldn't have any authentication)",
                            "and remove whatever file has something to do with s0ftm4rk",
                        ]
                    ),
                }
            ],
            "exp_needed": 0,
            "credit_reward": 50,
            "exp_reward": 10,
            "requirements": {
                "interpol_gov_file": (
                    RequirementType.FILE_NOT_PRESENT,
                    "guest|s0ftm4rk_temp.doc",
                )
            },
        },
        {
            "id": "mtr002",
            "title": "Unexpected Email",
            "description": "Remove email from a user account",
            "emails": [
                {
                    "from": "karma@mother.net",
                    "subject": "",
                    "attachment": None,
                    "content": "\n".join(
                        [
                            "An employee of the japanese division of Telemark called Ming Woo Lo has come into possession",
                            "of some documents containing informations about community users.",
                            "We need this email removed from his personal account.",
                            "This task is perfect for learning the use of IVoice, you can search chat logs for messages",
                            "containing strings, names etc.",
                            "Go to ivoice.com to check it out",
                        ]
                    ),
                }
            ],
            "exp_needed": 10,
            "credit_reward": 50,
            "exp_reward": 10,
            "requirements": {
                "kyotomail_jp": (
                    RequirementType.EMAIL_NOT_PRESENT,
                    "mw_lo|Interesting docs",
                )
            },
        },
        {
            "id": "mtr003",
            "title": "Network's cancer",
            "description": "Crash a server",
            "emails": [
                {
                    "from": "karma@mother.net",
                    "subject": "",
                    "attachment": None,
                    "content": "\n".join(
                        [
                            "We have received a horrifying news.",
                            "Someone has hacked web.neowa.se server and is using it to spread some very dark content.",
                            "We deactivated the web browser part, but we need you to access the remaining file server and crash it",
                            "Did you know? some misconfigured servers expose system files, if you delete kernel.sys the system will reboot",
                            "and crash itself",
                        ]
                    ),
                }
            ],
            "exp_needed": 20,
            "credit_reward": 50,
            "exp_reward": 10,
            "requirements": {
                "web_neowa_se": (
                    RequirementType.SERVER_CRASHED,
                    "",
                )
            },
        },
        {
            "id": "mtr004",
            "title": "Confidential information",
            "description": "Download file from a corporate server",
            "emails": [
                {
                    "from": "karma@mother.net",
                    "subject": "",
                    "attachment": None,
                    "content": "\n".join(
                        [
                            "After the TelemarkONE incident a lot of corporations are exchanging confidential documents.",
                            'ENSAT is one of those: we traced a file named "unreg728.dat" it seems it\'s been transferred to',
                            "a temporary server managed by ENSAT itself;",
                            "We don't have an IP or a server name though.",
                            "Find the server and download the file, it will be uploaded to us during the review process.",
                        ]
                    ),
                }
            ],
            "exp_needed": 30,
            "credit_reward": 50,
            "exp_reward": 10,
            "requirements": {
                "temp_ensatcorp_net": (
                    RequirementType.FILE_DOWNLOADED,
                    "unreg728.dat",
                )
            },
        },
        {
            "id": "mtr005",
            "title": "The trojan horse",
            "description": "Upload worm to corporate server",
            "emails": [
                {
                    "from": "karma@mother.net",
                    "subject": "",
                    "attachment": ("database.bin", "7dbecf59592e4e2c9880255ad2f10453"),
                    "content": "\n".join(
                        [
                            "Puresun is also starting to exchange documents.",
                            'We need you to upload a special worm to the their server "subcorp.puresun.net"',
                            "this program will track all data sent to other corporations.",
                            "We can't find information about it so we think a clean login isn't possible.",
                            'The worm you need to upload "database.bin" should be already downloaded into your local machine',
                        ]
                    ),
                }
            ],
            "exp_needed": 40,
            "credit_reward": 50,
            "exp_reward": 10,
            "requirements": {
                "subcorp_puresun_net": (
                    RequirementType.FILE_PRESENT,
                    "admin|database.bin",
                )
            },
        },
    ],
    "writable": False,
    "crashed": False,
    "hack_tool": None,
    "defense_tool": None,
}


class KarmaMotherNet(BaseServer):
    def http(self):
        self.assignment_server(SERVER_CONFIG)
