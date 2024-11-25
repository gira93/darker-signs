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
                            "a corporation surely can get huge gains from this (you heard of ZRIO right?)."
                            "Find information about D1l3mm4, he's credited as the creator of Mother,",
                            "no one knows his/her real identity, but if this person really created Mother,",
                            "that same person must know something.",
                            "Dig deep, and if you find interesting documents, save them locally and I'll take a look",
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
                ),
                "bentekmail_com_2": (
                    RequirementType.FILE_DOWNLOADED,
                    "triad.doc",
                ),
                "hime_bentekcorp.com": (RequirementType.FILE_DOWNLOADED, "triad.arc"),
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
                            "Each one of the Triad's mirror contains a key, changed daily; I need you to access each one and get its current key.",
                            "As you saw, the Triad servers won't allow ftp access, but their master maybe do,",
                            'I would assume they just prepend "master" to the address, like master.karma...',
                            "Get the key from each server and then check back here, as always, I'll take a look",
                        ]
                    ),
                }
            ],
            "exp_needed": 140,
            "credit_reward": 50,
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
                    "attachment": None,
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
            "credit_reward": 50,
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
            "credit_reward": 50,
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

        if [
            "iron001",
            "iron002",
            "iron003",
            "iron004",
            "iron005",
        ] in self.player.completed_missions():
            for server_id in [
                "karma_mother_net",
                "master_karma_mother_net",
                "sutra_mother_net",
                "master_sutra_mother_net",
                "warez_mother_net",
                "master_warez_mother_net",
                "hammerzone_mother_net",
            ]:
                self.player.add_or_update_server(server_id, {"crashed": True})
                progress_bar()
                cprint("Logged out of Mother Network\n", "red")
                cprint(
                    "Cannot enstablish connection to master.mother.net, skipping",
                    "yellow",
                )
