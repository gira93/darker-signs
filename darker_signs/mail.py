import json


class Mail:
    def __init__(self, mailbox):
        self.mailbox_path = mailbox
        with open(mailbox, "r") as f:
            self.mailbox = json.load(f)

    def run(self):
        while True:
            self.__print_mailbox()
            message_id = input("Type message number or 0 to exit: ")
            if message_id == "0":
                self.__save()
                break
            self.__print_message(message_id)

    def add_message(self, *, from_user, subject, message):
        self.mailbox.append(
            {
                "from": from_user,
                "subject": subject,
                "message": message,
                "read": False,
            }
        )
        self.__save()

    def __save(self):
        with open(self.mailbox_path, "w") as f:
            json.dump(self.mailbox, f, indent="\t")

    def __print_mailbox(self):
        for idx, mail in enumerate(self.mailbox):
            status = " " if mail["read"] else "N"
            print(f"{idx + 1} {status}> {mail['from']}:{mail['subject']}")

    def __print_message(self, message_id):
        try:
            idx = int(message_id)
            message = self.mailbox[idx - 1]
            print(f"From: {message['from']}")
            print(f"Subject: {message['subject']}")
            print("")
            print(message["message"])
            input("Press enter to return to menu")
            self.mailbox[idx - 1]["read"] = True
            return True
        except (IndexError, ValueError):
            print("Message not found")
            return False
