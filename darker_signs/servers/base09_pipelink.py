from darker_signs.dns import Dns
from darker_signs.mail import Mail


class Base09Pipelink:
    def __init__(self, root_path: str, mail: Mail, dns: Dns) -> None:
        self.root_path = root_path
        self.mail = mail
        self.dns = dns

    def remote_res_29(self):
        pass

    def http_09pipelink(self):
        pass
