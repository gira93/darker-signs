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
                            "An employee of a Japanese company called Ming Woo Lo has come into possession",
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
                            'The worm you need to upload "database.bin" has been automatically downloaded to your local machine',
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
        {
            "id": "mtr006",
            "title": "Teaching a lesson",
            "description": "Delete a file from a server",
            "emails": [
                {
                    "from": "karma@mother.net",
                    "subject": "",
                    "attachment": None,
                    "content": "\n".join(
                        [
                            'We need you to delete the file "final_review.doc" from the server "athem.final.net".',
                            "The server belongs to SirBrown, an ex member of our community;",
                            "He left us to go work for FinalNET, and also brought that document containing confindential information.",
                        ]
                    ),
                }
            ],
            "exp_needed": 50,
            "credit_reward": 50,
            "exp_reward": 10,
            "requirements": {
                "athem_final_net": (
                    RequirementType.FILE_NOT_PRESENT,
                    "sirbrown|final_review.doc",
                )
            },
        },
        {
            "id": "mtr007",
            "title": "Wrongful dismissal",
            "description": "Investigate a case",
            "emails": [
                {
                    "from": "karma@mother.net",
                    "subject": "",
                    "attachment": None,
                    "content": "\n".join(
                        [
                            "1r0nch4ng, a member of our community, has asked for our help;",
                            "Paolo Stagna, a friend of his, has been wrongfully dismissed from Wellmark.",
                            "Investigate and take action if necessary, Stagna is now under arrest",
                            "so find a way to gey him out of custody if he's innocent!",
                        ]
                    ),
                },
                {
                    "from": "tikhomir@interpol.gov",
                    "subject": "You think we didn't notice?",
                    "attachment": None,
                    "content": "\n".join(
                        [
                            "Hello,",
                            "I'm Tikhomir from russian interpol; you did good on your last hack.",
                            "SirBrown was still under surveilance when we noticed someone sneaking in...",
                            "I won't bring you in, don't worry, I think you can actually do some tasks for us.",
                            "check altproject.interpol.ru once in a while for some smaller jobs.",
                        ]
                    ),
                },
            ],
            "exp_needed": 60,
            "credit_reward": 50,
            "exp_reward": 10,
            "requirements": {
                "interpol_gov_file": (
                    RequirementType.FILE_PRESENT,
                    "guest|hr_report.doc",
                )
            },
        },
        {
            "id": "mtr008",
            "title": "Suspicious partnership",
            "description": "Steal a file",
            "emails": [
                {
                    "from": "karma@mother.net",
                    "subject": "",
                    "attachment": None,
                    "content": "\n".join(
                        [
                            "Thanks to a sypworm uploaded to a Puresun server, we learned of suspicious money movements on behalf of FinalNET.",
                            "It appears that the U.S. company is secretly funding IT adjustment operations for FinalNET's Australian division.",
                            'Some community members have previously traced the name of a file ("transfer.log") received on the "australian.final.net" server;',
                            'It appears to have been transferred by one "Papav3ro."',
                            "Your task is to steal this file.",
                        ]
                    ),
                }
            ],
            "exp_needed": 70,
            "credit_reward": 50,
            "exp_reward": 10,
            "requirements": {
                "australian_final_net": (
                    RequirementType.FILE_DOWNLOADED,
                    "transfer.log",
                )
            },
        },
        {
            "id": "mtr009",
            "title": "Operation Crossfire",
            "description": "Crash a server",
            "emails": [
                {
                    "from": "karma@mother.net",
                    "subject": "",
                    "attachment": None,
                    "content": "\n".join(
                        [
                            "User 1r0nchan4g directly asked for you for this task.",
                            "He needs you to crash the web4.telemark.com server, once this task is completed,",
                            "he will take advantage of the down moment to infiltrate the Telemark network.",
                        ]
                    ),
                }  # TODO - Email from 1r0nch4ng
            ],
            "exp_needed": 80,
            "credit_reward": 50,
            "exp_reward": 10,
            "requirements": {
                "web4_telemark_com": (
                    RequirementType.SERVER_CRASHED,
                    "",
                )
            },
        },
        {
            "id": "mtr010",
            "title": "The installer",
            "description": "Upload spyware on a server",
            "emails": [
                {
                    "from": "karma@mother.net",
                    "subject": "",
                    "attachment": ("setupdb.bin", "faf901d8a56f46a387165fea742cc0ef"),
                    "content": "\n".join(
                        [
                            "These days Telemark seems to be the most active corporation.",
                            "We know they will be performing a massive software upgrade soon,",
                            "we need to make the most of the situation, this is where you come in:",
                            'enter the "east3.telemark.com" server and upload the "setupdb.bin" file (attached),',
                            "during the update this malicious file will be automatically executed",
                            "and we will be able to track Telemark's operations.",
                            "It sounds easy but said server is protected by a physical key login system;",
                            "you won't be able to crack it using conventional methods, we trust your skill.",
                        ]
                    ),
                }
            ],
            "exp_needed": 100,
            "credit_reward": 50,
            "exp_reward": 10,
            "requirements": {
                "east3_telemark_com": (
                    RequirementType.FILE_PRESENT,
                    "admin|setupdb.bin",
                )
            },
        },
        {
            "id": "mtr011",
            "title": "Operation Big Brother",
            "description": "Upload spyware on a server",
            "emails": [
                {
                    "from": "karma@mother.net",
                    "subject": "",
                    "attachment": ("system.bin", "ce4c31a189124f498ba8e3bc1dc2bd28"),
                    "content": "\n".join(
                        [
                            "You have to penetrate the Mecca Technologies main1.meccate.ch mainframe and upload the attached system.bin file.",
                            "Don't be fooled by the simplicity of the request, this server is the most secure in the entire network:",
                            "it uses a voice recognition system to authenticate access (VRLS),",
                            "does not accept public connections, and finally has an advanced tracing system.",
                            "We trust in your talent",
                        ]
                    ),
                }
            ],
            "exp_needed": 120,
            "credit_reward": 50,
            "exp_reward": 10,
            "requirements": {
                "main1_meccate_ch": (
                    RequirementType.FILE_PRESENT,
                    "admin|system.bin",
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
