import readline
from termcolor import cprint
from pyfiglet import Figlet
from system.mail import Mail
from system.dns import Dns
from system.player import Player
from system.utils import download_file, progress_bar, show_menu, upload_file
from mother.type_defs import (
    Assignment,
    AssignmentRequirement,
    AssignmentServerConfig,
    ChatMessage,
    RequirementType,
    ServerConfig,
    ShopItem,
    WebServerConfig,
    FileServerConfig,
    MailServerConfig,
    ChatServerConfig,
    DbServerConfig,
    CommerceServerConfig,
    DbEntry,
    Email,
)


class BaseServer:
    def __init__(self, root_path: str, mail: Mail, dns: Dns, player: Player) -> None:
        self.root_path = root_path
        self.mail = mail
        self.dns = dns
        self.player = player

    def file_server(self, server_config: FileServerConfig) -> None:
        if server_config["proxy"]:
            connection_command = readline.get_history_item(
                readline.get_current_history_length()
            ).split(" ")
            if (
                len(connection_command) >= 3
                and connection_command[0] == "tunnel"
                and connection_command[1] == server_config["proxy"]
            ):
                print()
                cprint(f'Connected through {server_config["proxy"]}\n', "green")
            else:
                print()
                cprint("Public connections are disabled!\n", "red")
                return

        base_commands = ["cat", "ls", "download", "help", "exit"]
        write_only_commands = ["rm", "upload"]

        id, config = self.__load_config(server_config)
        if config["crashed"]:
            print()
            cprint("Server Unavailable", "red")
            print()
            return

        available_commands = (
            base_commands + write_only_commands if config["writable"] else base_commands
        )
        _, defense_tool = self.__initialize_tools(server_config)
        if server_config["defense_tool"] and not defense_tool:
            return

        self.__welcome(config["banner"], config["name"], config["font"])

        account = self.__authenticate(config)
        if not account:
            cprint("Disconnecting", "red")
            return

        files: dict[str, str] = dict(config["contents"][account])
        while True:
            filenames: list[str] = list(files.keys())
            command = input(f"{account} > ").split()
            com = command[0] if len(command) > 0 else ""
            param = command[1] if len(command) > 1 else ""
            if com in available_commands:
                match com:
                    case "cat":
                        if param in filenames:
                            print()
                            cprint(files[param], "blue")
                            print()
                        else:
                            cprint("File not found\n", "red")
                        continue
                    case "ls":
                        print()
                        cprint("  ".join(filenames), "blue")
                        print()
                        continue
                    case "download":
                        if param in filenames:
                            print()
                            cprint(f"Downloading {param}...", "green")
                            download_file(f"{self.root_path}/{param}", files[param])
                            print()
                        else:
                            cprint("File not found\n", "red")
                        continue
                    case "rm":
                        if param in filenames:
                            print()
                            cprint(f"{param} removed\n", "red")
                            files.pop(param, None)
                            if param == "kernel.sys":
                                config["crashed"] = True
                                print()
                                cprint("Kernel changed", "yellow")
                                cprint("Rebooting", "yellow")
                                progress_bar()
                                cprint("KERNEL MISSING", "red")
                                cprint("Connection closed by remote host", "red")
                                break
                        else:
                            cprint("File not found", "red")
                        continue
                    case "upload":
                        uploaded_file = upload_file(f"{self.root_path}/{param}")
                        print()
                        if uploaded_file:
                            cprint(f"{param} uploaded\n", "green")
                            files[param] = ""
                        else:
                            cprint("File not found in local machine\n", "red")
                        continue
                    case "help":
                        print("Available commands:")
                        print(" ".join(available_commands))
                        print()
                        continue
                    case "exit":
                        # if "connection.log" in filenames:
                        #     print()
                        #     cprint("Connection log file traced", "red")
                        #     print()
                        cprint("Disconnecting\n", "red")
                        break
            elif com == "":
                continue
            else:
                cprint("Command not found\n", "red")
                continue

        config["contents"][account] = list(files.items())
        self.player.add_or_update_server(id, config)

    def web_server(self, server_config: WebServerConfig) -> None:
        id, config = self.__load_config(server_config)
        if config["crashed"]:
            print()
            cprint("Server Unavailable", "red")
            print()
            return

        _, defense_tool = self.__initialize_tools(server_config)
        if server_config["defense_tool"] and not defense_tool:
            return

        self.__welcome(config["banner"], config["name"], config["font"])
        articles: list[DbEntry] = config["contents"]
        options = list(map(lambda article: article["title"], articles))
        while True:
            print("Available articles:")
            user_input = show_menu(options)
            match user_input:
                case s if s.isdigit() and 1 <= int(s) <= len(options):
                    article: DbEntry = articles[int(s) - 1]
                    print()
                    cprint(article["title"], "blue")
                    print()
                    print(article["content"])
                    print()
                    input("Press a key")
                    continue
                case "nukelord" if self.player.has_tool("nukelord") and config[
                    "hack_tool"
                ] == "nukelord":
                    print()
                    cprint("NUKING", "red")
                    progress_bar()
                    cprint("SERVER NUKED", "green")
                    cprint("Disconnecting", "red")
                    config["crashed"] = True
                    self.player.add_or_update_server(id, config)
                    break
                case "0":
                    print()
                    cprint("Connection closed", "red")
                    break
                case _:
                    continue

    def mail_server(self, server_config: MailServerConfig) -> None:
        id, config = self.__load_config(server_config)
        _, defense_tool = self.__initialize_tools(server_config)
        if server_config["defense_tool"] and not defense_tool:
            return

        self.__welcome(config["banner"], config["name"], config["font"])
        account = self.__authenticate(config)

        if not account:
            cprint("Disconnecting", "red")
            return

        messages: list[Email] = config["contents"][account]
        while True:
            options = list(map(lambda message: message["subject"], messages))
            print("Inbox:")
            user_input = show_menu(options)
            match user_input:
                case s if s.isdigit() and 1 <= int(s) <= len(options):
                    message_index = int(s) - 1
                    message: Email = messages[message_index]
                    print()
                    cprint(f'From: {message["from"]}', "blue")
                    cprint(f'Subject: {message["subject"]}', "blue")
                    print()
                    print(message["content"])
                    print()
                    if config["writable"]:
                        message_option = show_menu(
                            ["Delete message"], "Go back", "Select an action"
                        )
                        match message_option:
                            case "1":
                                messages.pop(message_index)
                                config["contents"][account] = messages
                                self.player.add_or_update_server(id, config)
                                print()
                                cprint("Message deleted", "red")
                                input("Press a key")
                                continue
                            case _:
                                continue
                    else:
                        input("Press a key")
                        continue
                case "0":
                    print()
                    cprint("Connection closed", "red")
                    break
                case _:
                    continue

    def db_server(self, server_config: DbServerConfig) -> None:
        _, config = self.__load_config(server_config)

        _, defense_tool = self.__initialize_tools(server_config)
        if server_config["defense_tool"] and not defense_tool:
            return

        self.__welcome(config["banner"], config["name"], config["font"])
        account = self.__authenticate(config)

        if not account:
            cprint("Disconnecting", "red")
            return

        entries: list[DbEntry] = config["contents"]
        while True:
            search_query = input("Type a search query (exit to disconnect): ")
            if search_query == "exit":
                print()
                cprint("Disconnecting", "red")
                break
            elif search_query == "":
                continue
            elif len(search_query) > 5:
                search_result = next(
                    (e for e in entries if search_query.lower() in e["title"].lower()),
                    None,
                )
                if search_result:
                    print()
                    cprint("Entry found\n", "green")
                    cprint(search_result["title"], "magenta")
                    print()
                    cprint(search_result["content"], "blue")
                    print()
                    input("Press a key")
                    continue
                else:
                    print()
                    cprint("No results found\n", "red")
                    continue
            else:
                cprint("Search query must be longer than 5 characters\n", "red")
                continue

    def chat_server(self, server_config: ChatServerConfig) -> None:
        _, config = self.__load_config(server_config)
        self.__welcome(config["banner"], config["name"], config["font"])

        entries: list[ChatMessage] = config["contents"]
        while True:
            search_query = input("Search for a message (type exit to disconnect): ")
            if search_query == "exit":
                print()
                cprint("Disconnecting", "red")
                break
            elif search_query == "":
                continue
            elif len(search_query) > 3:
                search_results: list[ChatMessage] = [
                    e for e in entries if search_query.lower() in e["content"].lower()
                ]
                if len(search_results) > 0:
                    print()
                    cprint("Found messages:\n", "green")
                    for result in search_results:
                        cprint(f"{result['op']}@: {result['content']}", "blue")
                    print()
                    input("Press a key")
                    continue
                else:
                    print()
                    cprint("No results found\n", "red")
                    continue
            else:
                cprint("Search query must be longer than 3 characters\n", "red")
                continue

    def commerce_server(self, server_config: CommerceServerConfig) -> None:
        _, config = self.__load_config(server_config)
        self.__welcome(config["banner"], config["name"], config["font"])
        items: list[ShopItem] = config["contents"]
        while True:
            formatted_items = [f"{i[0]} | {i[2]}Cr." for i in items]
            selection = show_menu(
                formatted_items, selection_message="Select an item to view details"
            )
            match selection:
                case s if s.isdigit() and 1 <= int(s) <= len(items):
                    item_index = int(s) - 1
                    print()
                    cprint(items[item_index][0].capitalize(), "magenta")
                    print()
                    cprint(items[item_index][1], "blue")
                    print()
                    cprint(f"Price: {items[item_index][2]}Cr.", "blue")
                    print()
                    buy_selection = show_menu(["Buy"], abort_message="Go back")
                    if buy_selection == "1":
                        price: int = items[item_index][2]
                        if self.player.has_tool(items[item_index][0]):
                            cprint("You already have that item\n", "yellow")
                            continue
                        elif self.player.balance() > price:
                            self.player.subtract_credit(price)
                            self.player.add_tool(items[item_index][0])
                            progress_bar(step=0.02)
                            cprint(
                                f"Congratulations! you got {items[item_index][0].capitalize()}!\n",
                                "green",
                            )
                            continue
                        else:
                            cprint("You don't have enough credits!", "red")
                            continue
                    else:
                        continue
                case "0":
                    cprint("Connection closed\n", "red")
                    break
                case _:
                    continue

    def gateway_server(self) -> None:
        print()
        cprint("This is a gateway server\nDirect connections are disabled\n", "red")
        return

    def assignment_server(self, server_config: AssignmentServerConfig) -> None:
        _, config = self.__load_config(server_config)
        self.__welcome(config["banner"], config["name"], config["font"])

        active_mission_id = self.player.active_mission()
        if active_mission_id:
            print()
            cprint(
                "You are currently working on an assignment.\nYou can't work on multiple tasks at the same time.\n",
                "yellow",
            )
            review_mission = input("Do you want to flag it for review? (y/n)[n]: ")
            if review_mission == "y":
                cprint(
                    "Assignment sent for review...\nPlease wait, checking requirements...\n",
                    "yellow",
                )
                progress_bar()
                print()
                if self.__review_mission(active_mission_id, config["contents"]):
                    self.player.set_active_mission(None)
                    self.player.add_completed_mission(active_mission_id)
                    cprint(
                        "Assignment accepted\nReward has been transfered to your account\n",
                        "green",
                    )
                else:
                    cprint("Assignment not completed", "red")
                    cprint("Connection closed", "red")
            return

        missions: list[Assignment] = config["contents"]
        available_missions = []
        for mission in missions:
            if mission["id"] == self.player.active_mission():
                continue
            elif mission["id"] in self.player.completed_missions():
                continue
            elif self.player.experience() >= mission["exp_needed"]:
                available_missions.append(mission)
            else:
                continue
        while True:
            selection = show_menu(
                list(map(lambda mission: mission["title"], available_missions))
            )
            match selection:
                case s if s.isdigit() and 1 <= int(s) <= len(available_missions):
                    mission: Assignment = available_missions[int(s) - 1]
                    print()
                    cprint(mission["title"], "blue")
                    print()
                    cprint(mission["description"], "blue")
                    print()
                    cprint(f'Reward: {mission["credit_reward"]}Cr.\n', "green")
                    confirm = input("Accept this assignment? (y/n)[n]: ")
                    if confirm == "y":
                        self.player.set_active_mission(mission["id"])
                        for email in mission["emails"]:
                            self.mail.add_message(
                                from_user=email["from"],
                                subject=mission["title"]
                                if email["subject"] == ""
                                else email["subject"],
                                message=email["content"],
                            )
                            if email["attachment"]:
                                name, content = email["attachment"]
                                download_file(
                                    f"{self.root_path}/{name}", content, False
                                )
                        print()
                        cprint(
                            "Thank you for accepting this assignment.\nDetails have been sent to your email.\n",
                            "green",
                        )
                        break
                    else:
                        continue
                case "0":
                    print()
                    cprint("Connection closed", "red")
                    break
                case _:
                    continue

    def __initialize_tools(
        self, server_config: ServerConfig
    ) -> tuple[bool, bool]:  # tuple[hack tool loaded, defense tool loaded]
        tools_present: list[bool] = [True, True]
        if server_config["hack_tool"]:
            if self.player.has_tool(server_config["hack_tool"]):
                tools_present[0] = True
                cprint(
                    f"{server_config['hack_tool'].capitalize()} armed and ready!",
                    "yellow",
                )
                print()
            else:
                tools_present[0] = False
        else:
            tools_present[0] = True

        if server_config["defense_tool"]:
            if self.player.has_tool(server_config["defense_tool"]):
                tools_present[1] = True
                cprint(
                    f"{server_config['defense_tool'].capitalize()} running!", "green"
                )
                print()
            else:
                cprint("Trace detected!\nYou have been disconnected!", "red")
                tools_present[1] = False
        else:
            tools_present[1] = True

        return (tools_present[0], tools_present[1])

    def __load_config(self, server_config: ServerConfig) -> tuple[str, dict]:
        id = server_config["id"]
        server_override = self.player.get_server(id)
        config = server_override if server_override else dict(server_config)
        return (id, config)

    def __welcome(self, banner: str, name: str, font: str = "standard"):
        f = Figlet(font)
        cprint(f.renderText(name), "blue")
        print()
        cprint(banner, "green")
        print()

    def __authenticate(self, server_config: dict) -> str | None:
        accounts: dict[str, str] = dict(server_config["authentication"])

        if server_config["hack_tool"] == "physicalkey":
            cprint("Physical Key required for login\n", "yellow")
            user = list(accounts.keys())[0]
            key_name = accounts[user]
            cprint("Checking for key...\n", "yellow")
            key_present = upload_file(f"{self.root_path}/{key_name}")
            if key_present:
                cprint("Key validation completed\nAccess granted", "green")
                return user
            else:
                cprint("Key validatoin failed\nDisconnecting", "red")
                return None

        cprint("Login required", "yellow")
        print()
        user = input("Username: ")
        pw = input("Password: ")
        if (
            user in accounts
            and pw == accounts[user]
            and server_config["hack_tool"] != "wavehacker"
        ):
            print()
            cprint("Access granted", "green")
            print()
            return user
        elif (
            user in accounts
            and pw == accounts[user]
            and server_config["hack_tool"] == "wavehacker"
            and self.player.has_tool("wavehacker")
        ):
            cprint(f"Wavehacker calling {pw}...\n", "yellow")
            progress_bar()
            cprint("Wavehacker playing back recorded audio...\n", "green")
            progress_bar(100, 0.02)
            cprint("VRLS System Login Complete\n", "green")
            return user
        elif (
            (
                pw == "rootbreaker"
                and self.player.has_tool("rootbreaker")
                and server_config["hack_tool"] == "rootbreaker"
            )
            or (
                pw == "rootbreaker2"
                and self.player.has_tool("rootbreaker2")
                and server_config["hack_tool"] == "rootbreaker2"
            )
            or (
                pw == "rootbreaker3"
                and self.player.has_tool("rootbreaker3")
                and server_config["hack_tool"] == "rootbreaker3"
            )
        ):
            print()
            cprint("CRACKING", "red")
            progress_bar()
            if user in accounts:
                print()
                cprint("Access granted", "green")
                print()
                cprint(f"Password is: {accounts[user]}", "yellow")
                return user
            else:
                print()
                cprint("User not found\nCracking failed", "red")
                print()
                return None
        else:
            print()
            cprint("Invalid username or password", "red")
            return None

    def __review_mission(self, mission_id: str, missions: list[Assignment]) -> bool:
        mission: list[Assignment] = [m for m in missions if mission_id == m["id"]]
        if len(mission) == 0:
            cprint("Current active assignment not found on our system\n", "red")
            return False
        requirements: dict[str, AssignmentRequirement] = mission[0]["requirements"]
        requirements_met: list[bool] = []
        for server_id in requirements.keys():
            server = self.player.get_server(server_id)
            if server:
                req_type, subject = requirements[server_id]
                match req_type:
                    case RequirementType.FILE_PRESENT:
                        user, file = subject.split("|")
                        files = [f[0] for f in server["contents"][user]]
                        if file in files:
                            requirements_met.append(True)
                        else:
                            requirements_met.append(False)
                    case RequirementType.FILE_NOT_PRESENT:
                        user, file = subject.split("|")
                        files = [f[0] for f in server["contents"][user]]
                        if file in files:
                            requirements_met.append(False)
                        else:
                            requirements_met.append(True)
                    case RequirementType.FILE_DOWNLOADED:
                        requirements_met.append(
                            upload_file(f"{self.root_path}/{subject}")
                        )

                    case RequirementType.SERVER_CRASHED:
                        requirements_met.append(server["crashed"])
                    case RequirementType.EMAIL_NOT_PRESENT:
                        user, mail_subject = subject.split("|")
                        email_subjects = [
                            m["subject"] for m in server["contents"][user]
                        ]
                        if mail_subject in email_subjects:
                            requirements_met.append(False)
                        else:
                            requirements_met.append(True)
            else:
                requirements_met.append(False)
        if list(set(requirements_met))[0]:
            self.player.add_credit(mission[0]["credit_reward"])
            self.player.add_experience(mission[0]["exp_reward"])
            return True
        else:
            return False
