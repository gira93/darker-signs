from termcolor import cprint
from system.utils import progress_bar
from .base_server import BaseServer
from mother.type_defs import AssignmentServerConfig, RequirementType

SERVER_CONFIG: AssignmentServerConfig = {
    "id": "hide_ironchang_it",
    "name": "1r0nch4ng",
    "banner": "Private Assignments Only!",
    "font": "bell",
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
            "credit_reward": 0,
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
            "title": "The Missing Link",
            "description": "Investigation",
            "emails": [
                {
                    "from": "1r0nch4ng@hide.ironchang.it",
                    "subject": "",
                    "attachment": None,
                    "content": "\n".join(
                        [
                            "I've taken a look at the binary you uploaded... this is huge, there's a big backdoor",
                            "in Mother that makes all computers part of a botnet!",
                            "Who are the people behind Mother and what is the purpose of this?",
                            "a corporation surely can get huge gains from this (you heard of ZRIO right?).",
                            "Find information about D1l3mm4, he's credited as the creator of Mother,",
                            "no one knows his/her real identity, but if this person really created Mother,",
                            "that same person must know something.",
                            "Dig deep, and if you find interesting documents, save them locally and I'll take a look",
                        ]
                    ),
                }
            ],
            "exp_needed": 130,
            "credit_reward": 0,
            "exp_reward": 10,
            "requirements": {
                "bentekmail_com": (
                    RequirementType.FILE_DOWNLOADED,
                    "mother.doc",
                ),
                "hime_bentekcorp_com": (RequirementType.FILE_DOWNLOADED, "triad.arc"),
            },
        },
        {
            "id": "iron003",
            "title": "The keys",
            "description": "Download file from servers",
            "emails": [
                {
                    "from": "1r0nch4ng@hide.ironchang.it",
                    "subject": "",
                    "attachment": None,
                    "content": "\n".join(
                        [
                            "Everything is making sense now! I'm sure that Jacques De Bout is D1l3mm4",
                            "and he works for Bentek, guess who's the major shareholder of Telemark?",
                            "Bentek! The attack was planned, De Bout is Security Manager and worked for both Telemark and Bentek...",
                            'He is the admin of the entire Mother network and planned the fake Telemark "attack"!',
                            "We need to fight back, I analyzed the documents and the archive you found:",
                            "Each one of the Triad's mirror contains a key, changed daily;",
                            "I need you to access each one and get its current key.",
                            "As you saw, the Triad servers won't allow ftp access, but their master maybe do...",
                            "Get the key from each server and then check back here, as always, I'll take a look",
                        ]
                    ),
                }
            ],
            "exp_needed": 140,
            "credit_reward": 0,
            "exp_reward": 30,
            "requirements": {
                "master_karma_mother_net": (
                    RequirementType.FILE_DOWNLOADED,
                    "daily_karma",
                ),
                "master_sutra_mother_net": (
                    RequirementType.FILE_DOWNLOADED,
                    "daily_sutra",
                ),
                "master_warez_mother_net": (
                    RequirementType.FILE_DOWNLOADED,
                    "daily_warez",
                ),
            },
        },
        {
            "id": "iron004",
            "title": "The Triad is done",
            "description": "Crash a server",
            "emails": [
                {
                    "from": "1r0nch4ng@hide.ironchang.it",
                    "subject": "",
                    "attachment": (
                        "JIT66.dmp",
                        "5cf2ca3029ca4dafadf1aa467678ee74e54d9493d71acd509d224d849bdb828ba8861d37",
                    ),
                    "content": "\n".join(
                        [
                            "Analyzing the 3 keys you got I found out they are each part of a unique key!",
                            'By combining them all I got the file "JIT66.dmp"(attached).',
                            "Remember the physical key authentication? this is just a physical key dump!",
                            'It should grant you access to "master.mother.net".',
                            "I'll leave you the onor of entering and crashing it!",
                            "All mother servers should then crash themselves in a couple of hours",
                        ]
                    ),
                }
            ],
            "exp_needed": 180,
            "credit_reward": 0,
            "exp_reward": 20,
            "requirements": {
                "master_mother_net": (
                    RequirementType.SERVER_CRASHED,
                    "",
                ),
            },
        },
        {
            "id": "iron005",
            "title": "One last thing",
            "description": "Upload file to server",
            "emails": [
                {
                    "from": "1r0nch4ng@hide.ironchang.it",
                    "subject": "",
                    "attachment": None,
                    "content": "\n".join(
                        [
                            "There's one last thing to do...",
                            "Remember the archive you downloaded earlier?",
                            "It contains the entire MotherOS source code (backdoor included)",
                            "Upload it to the interpol servers, let's make their lives easier (and Bentek's one worse!)",
                        ]
                    ),
                }
            ],
            "exp_needed": 200,
            "credit_reward": 0,
            "exp_reward": 10,
            "requirements": {
                "interpol_gov_file": (
                    RequirementType.FILE_PRESENT,
                    "guest|triad.arc",
                ),
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

        endgame_check = all(
            x in self.player.completed_missions()
            for x in [
                "iron001",
                "iron002",
                "iron003",
                "iron004",
                "iron005",
            ]
        )
        if endgame_check:
            for server_id in [
                "karma_mother_net",
                "master_karma_mother_net",
                "sutra_mother_net",
                "master_sutra_mother_net",
                "warez_mother_net",
                "master_warez_mother_net",
                "hammerzone_mother_net",
                "hide_ironchang_it",
            ]:
                self.player.add_or_update_server(server_id, {"crashed": True})

            progress_bar()
            cprint("Logged out of Mother Network\n", "red")
            cprint(
                "Cannot enstablish connection to master.mother.net, skipping",
                "yellow",
            )
            progress_bar()
            iron_message = "\n".join(
                [
                    "Can you believe what we were able to achieve?",
                    "The entire Mother Network is down and it won't be back up anytime soon;",
                    "Jacques De Bout is probably being arrested this very moment",
                    "and so is the entire Bentek management (maybe Telemark too!).",
                    "I told you we would meet again in the future!",
                    "What? You didn't recognize me? It's me Jimmy!",
                    "Actually, my real real name is Massimo (or Max), I don't work for anybody",
                    "I'm just an hacker like you, once I was called into the Mother Network I knew",
                    "something was up, but I played along since everyone was so cool.",
                    "Then you showed up, I knew together we would find answers;",
                    "Now the network is free, for real this time.",
                    "Thank you for helping me again!",
                    "See ya my friend!",
                    "",
                    "Massimo",
                ]
            )
            gira_message = "\n".join(
                [
                    "Hello,",
                    "I'm gira93, the developer who wrote this game,",
                    "thank you for playing! I hope you had fun as much as I did coding it.",
                    "",
                    "I want to mention the original creator of the ZRIO campaign, Vectra Media,",
                    "that's where all the first part was taken and adapted.",
                    "",
                    'Some time ago there was an italian hacking game called "Mother - A computer hacking simulation",',
                    "not to be confused with the RPG game xd.",
                    "This game was very influential to me, it was fun, very hollywood style but most importantly, it spoke my language;",
                    'I didn\'t know english that well and playing a game that was similar to "Uplink" but in my language was a blast!',
                    "",
                    'I recently found out that its creator Massimo "v4ldemar" Pinzaglia passed away,',
                    "I wanted to pay respect to him and the original Mother, so I decided to adapt and translate most of the game in English",
                    "the version you played is very similar, story-wise, to the original Mother,",
                    "but gameplay had to be adapted A LOT (and let me be honest, the original is better)",
                    "Hope you enjoyed it and if you know italian, please check out Mother - A computer hacking simulation (on archive.org)",
                    "",
                    "gira93",
                ]
            )
            self.mail.add_message(
                from_user="1r0nch4ng@hide.ironchang.it",
                subject="And so it ends",
                message=iron_message,
            )
            self.mail.add_message(
                from_user="gira93",
                subject="Some credits and a Thank you",
                message=gira_message,
            )
            return
