from .base_server import BaseServer
from mother.type_defs import AssignmentServerConfig, RequirementType

SERVER_CONFIG: AssignmentServerConfig = {
    "id": "hide_ironchang_it",
    "name": "",
    "banner": "",
    "font": "standard",
    "authentication": None,
    "proxy": None,
    "contents": [
        {
            "id": "iron001",
            "title": "Suspects",
            "description": "Investigation",
            "emails": [
                {
                    "from": "1r0nch4ng@hide.ironchang.it",
                    "subject": "",
                    "attachment": None,
                    "content": "\n".join(
                        [
                            "On our latest hack (thanks again, btw) I saw something that caught my attention;",
                            'I was looking through admin emails and saw the name "admin_hamm3r", the only "nickname" in a sea of real names.',
                            "Searching IVoice I found the same information you saw;",
                            "I was going to check his email account but then you crashed the server and we needed to move, fast",
                            "Do some investigation on this guy and if you find useful stuff, save it locally",
                        ]
                    ),
                }
            ],
            "exp_needed": 90,
            "credit_reward": 50,
            "exp_reward": 10,
            "requirements": {
                "hammerzone_mother_net": (
                    RequirementType.FILE_DOWNLOADED,
                    "bdoor_trace.bin",
                )
            },
        },
        {
            "id": "iron002",
            "title": "More Suspects",
            "description": "Investigation",
            "emails": [
                {
                    "from": "1r0nch4ng@hide.ironchang.it",
                    "subject": "",
                    "attachment": (
                        "stuff.txt",
                        "\n".join(
                            [
                                "Don't know if you read about D1l3mm4",
                                "he's credited as the creator of Mother and the network, seen as a master hacker around here,",
                                "some says he was defending the network during the big TelemarkONE attack",
                                "He vanished, no one knows his identity, but I crosschecked all actions of D1l3mm4",
                                "and it seems they are tied to Bentek!"
                                "and who is the major shareholder in Telemark? you guessed it Bentek again,",
                                "if D1l3mm4 works for Bentek, it means we know who's in charge of Mother!",
                                "and that opens up a new point of view on the TelemarkONE attack..."
                                "Keep this to yourself for now",
                            ]
                        ),
                    ),
                    "content": "\n".join(
                        [
                            "Oh my god! This is huge!",
                            "The backdoor you found makes every computer in the Mother network part of a botnet!",
                            'We need to lay low, I have attached the document "stuff.txt", read it, then check in here to complete the task',
                            "I'll get back to you",
                        ]
                    ),
                }
            ],
            "exp_needed": 110,
            "credit_reward": 50,
            "exp_reward": 10,
            "requirements": {
                "hammerzone_mother_net": (
                    RequirementType.FILE_DOWNLOADED,
                    "stuff.txt",
                )
            },
        },
        {
            "id": "iron003",
            "title": "The Missing Link",
            "description": "Investigation",
            "emails": [
                {
                    "from": "1r0nch4ng@hide.ironchang.it",
                    "subject": "",
                    "attachment": None,
                    "content": "\n".join(
                        [
                            "You need to find the missing link between D1l3mm4, Bentek and Telemark).",
                            "All we have now are speculations, there must be something somewhere.",
                            "Investigate, if you find interesting stuff, save it locally,",
                            "I'll take a look when you check in for this task",
                        ]
                    ),
                }
            ],
            "exp_needed": 130,
            "credit_reward": 50,
            "exp_reward": 10,
            "requirements": {
                "bentekmail_com": (
                    RequirementType.FILE_DOWNLOADED,
                    "mother.doc",
                )
            },
        },
    ],
    "writable": False,
    "crashed": False,
    "hack_tool": None,
    "defense_tool": None,
}


class HideIronchangIt(BaseServer):
    def http(self):
        self.assignment_server(SERVER_CONFIG)
