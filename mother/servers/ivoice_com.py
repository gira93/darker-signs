from .base_server import BaseServer
from mother.type_defs import ChatServerConfig

SERVER_CONFIG: ChatServerConfig = {
    "id": "ivoice_com",
    "name": "IVoice",
    "font": "standard",
    "proxy": None,
    "banner": "Welcome to IVoice Community Chat",
    "crashed": False,
    "writable": False,
    "contents": [
        {
            "op": "mw_lo",
            "content": "Hello, I'm Ming Woo Lo, I need the famous lotto program everyone talks about",
        },
        {"op": "b1t_drv", "content": "Ming Woo Lo? weren't you japanese?"},
        {
            "op": "mw_lo",
            "content": "Ming Woo Lo is a japanese name but I'm American! do you have the software? can you send it to mw_lo@kyotomail.jp?",
        },
        {
            "op": "vlad_ensat",
            "content": "Hello, I'm Vlad from ENSAT, I need to drop a file but all the servers are under maintenance",
        },
        {
            "op": "br4m1n0",
            "content": "Hi, ENSAT should have setup temp.ensatcorp.net, you will receive an email to your @freemail account",
        },
        {"op": "1r0nch4ng", "content": "Does anybody know about some Puresun server?"},
        {
            "op": "fr33z3r",
            "content": "I know for sure that Puresun has created a server, it should be subcorp.puresun.net. Don't have any other info",
        },
        {
            "op": "1r0nch4ng",
            "content": "I was able to connect but my current tools don't work. Puresun must have updated security",
        },
        {
            "op": "b1t_drv",
            "content": "You heard about SirBrown? He went to work for fucking FinalNET!",
        },
        {
            "op": "greenguy",
            "content": "SirBrown is just a traitor, voices says he also stolen some Mother documents that's why finalnet hired him!",
        },
        {
            "op": "tinfoiled",
            "content": "I think something's up, D1l3mm4 vanished, then SirBrown goes to work for finalnet...",
        },
        {
            "op": "fr33z3r",
            "content": "Don't you dare talk shit about D1l3mm4! He basically created Mother! Without him, corporations would've spied on this chat also!",
        },
        {
            "op": "tinfoiled",
            "content": "D1l3mm4 might have created Mother, but we don't know of his past, and his future, he vanished!",
        },
        {
            "op": "v4ldemar",
            "content": "Voices says that D1l3mm4 was monitoring the Mother network during the TelemarkONE big attack!",
        },
        {
            "op": "tinfoiled",
            "content": "If D1l3mm4 was there, don't you all think there should be something official? like in an investigation record?",
        },
        {
            "op": "v4ldemar",
            "content": "Maybe D1l3mm4 was using a different nickname at the time, I don't remember seeing his name in the official report",
        },
        {
            "op": "1r0nch4ng",
            "content": "Did anyone hear about Paolo Stagna? he's been fired from Wellmark!",
        },
        {
            "op": "MeaTPloW",
            "content": "Hey Papav3ro, can you send me that tool to my @freemail address?",
        },
        {
            "op": "REnO",
            "content": "I know the admin of web4.telemark.com, he asked me for something some time ago",
        },
        {
            "op": "admin_hamm3r",
            "content": "Hey REnO, do you still have that old game? can you send it to my @freemail address?",
        },
        {
            "op": "tinfoiled",
            "content": "I have seen that new physical key login system in the wild on a couple of server",
        },
        {
            "op": "CutEPastA",
            "content": "How does that work? you need a physical key attached to the system?",
        },
        {
            "op": "tinfoiled",
            "content": "Yes, you need physical access to the system and that physical key attached to it, else you won't be able to authenticate",
        },
        {
            "op": "Born4This",
            "content": "Actually, there is some sort of a side entrance: if for whatever reason the user loses the physical key,\nhe/she can still access the system remotely if a full dump of that key is present in the local system!",
        },
        {
            "op": "j01nt3r",
            "content": "I'm trying to access east3 without success, what's happening?",
        },
        {
            "op": "Ambrozy",
            "content": "east3 is being upgraded, for internal file sharing you can use privteam",
        },
        {"op": "MeaTPloW", "content": "Have you seen the new VRLS system? it's crazy!"},
        {
            "op": "1r0nch4ng",
            "content": "Yep, saw that, VRLS is basically impossible to crack, there's a tool available but it can't be considered cracking",
        },
        {
            "op": "MeaTPloW",
            "content": "You're right, I payed big bucks without reading the description ...",
        },
        {
            "op": "FaRa0n3",
            "content": "main1.meccate.ch is the most secure server on the network, it's Swiss, what do you expect?",
        },
        {
            "op": "Born4This",
            "content": "Mecca is Swiss? that's why main1.meccate.ch uses shadow.bellavista as a proxy!",
        },
        {
            "op": "MAc5",
            "content": "I know the admin, we worked together as writers at the now defunct archives.gs long ago,\nI was there when he was setting up main1.meccate.ch\nlet me tell you, he's very good",
        },
        {"op": "j01nt3r", "content": "I have found out that n3v3r_MIND is a girl!"},
        {
            "op": "1r0nch4ng",
            "content": "What's so special about it? n3v3r_MIND is basically the boss of xfreeze",
        },
        {
            "op": "j01nt3r",
            "content": "n3v3r heard of xfreeze xd",
        },
        {
            "op": "1r0nch4ng",
            "content": "That's because you weren't here when Zrio NET was up... xfreeze were called THC in Zrio NET\nNow they have a server here, xfreeze.com I think",
        },
        {"op": "v4ldemar", "content": "jbvie don't you have a personal server?"},
        {
            "op": "jbvie",
            "content": "Yes I have, my fiance configured it for me, it doesn't start with jbvie xd\nit's hime.bentekcorp.com, I also have that VRLS thing :)",
        },
    ],
    "hack_tool": None,
    "defense_tool": None,
    "authentication": None,
}


class IvoiceCom(BaseServer):
    def http(self):
        self.chat_server(SERVER_CONFIG)
