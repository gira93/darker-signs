import json
from termcolor import cprint


class Mail:
    def __init__(self, mailbox: str) -> None:
        self.mailbox_path = mailbox
        with open(mailbox, "r") as f:
            self.mailbox: list[dict] = json.load(f)

    def run(self) -> None:
        while True:
            print()
            self.__print_mailbox()
            print()
            message_id = input("Type message number or 0 to exit: ")
            if message_id == "0":
                self.__save()
                break
            print()
            self.__print_message(message_id)

    def add_message(self, *, from_user: str, subject: str, message: str) -> bool:
        is_present = next(
            (
                m
                for m in self.mailbox
                if m["from"] == from_user and m["subject"] == subject
            ),
            None,
        )
        if not is_present:
            self.mailbox.append(
                {
                    "from": from_user,
                    "subject": subject,
                    "message": message,
                    "read": False,
                }
            )
            self.__save()
            return True
        return False

    def new_email(self) -> bool:
        return any(not m["read"] for m in self.mailbox)

    def __save(self) -> None:
        with open(self.mailbox_path, "w") as f:
            json.dump(self.mailbox, f, indent="\t")

    def __print_mailbox(self) -> None:
        for idx, mail in enumerate(self.mailbox):
            status = " " if mail["read"] else "N"
            cprint(f"{idx + 1} {status}> {mail['from']}:{mail['subject']}", "blue")

    def __print_message(self, message_id: str) -> bool:
        try:
            idx = int(message_id)
            message = self.mailbox[idx - 1]
            cprint(f"From: {message['from']}", "light_blue")
            cprint(f"Subject: {message['subject']}", "light_blue")
            print()
            cprint(message["message"], "light_blue")
            input("Press enter to return to menu")
            self.mailbox[idx - 1]["read"] = True
            return True
        except (IndexError, ValueError):
            cprint("Message not found", "red")
            return False
