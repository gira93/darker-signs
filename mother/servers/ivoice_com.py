from .base_server import BaseServer
from mother.type_defs import ChatServerConfig

SERVER_CONFIG: ChatServerConfig = {
    "id": "ivoice_com",
    "name": "IVoice Chat Server",
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
            "content": "I think something's up, first D1l3mm4, then SirBrown, finalnet and the other company are hiring the best ones!",
        },
        {
            "op": "fr33z3r",
            "content": "Don't you dare talk shit about D1l3mm4! He basically created Mother! Without him, corporations would've spied on this chat also!",
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
    ],
    "hack_tool": None,
    "defense_tool": None,
    "authentication": None,
}


class IvoiceCom(BaseServer):
    def http(self):
        self.chat_server(SERVER_CONFIG)
