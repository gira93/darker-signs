from termcolor import cprint
from system.utils import show_menu
from .base_server import BaseServer


class Base09Pipelink(BaseServer):
    def remote_res_29(self):
        keycode = "331"
        print()
        cprint("Remote Resource Server", "blue")
        while True:
            command = input("Waiting for command: ")
            match command:
                case "help":
                    print("Commands")
                    commands = ["help", "keycode", "mod", "reset", "connect"]
                    print(", ".join(commands))
                    continue
                case "keycode":
                    print("Keycode value:")
                    print(keycode)
                case "mod":
                    new_code = input("Enter new code: ")
                    if new_code == "441":
                        keycode = new_code
                    else:
                        cprint("Invalid keycode", "red")
                    continue
                case "reset":
                    keycode = "331"
                    continue
                case "connect":
                    if keycode == "441":
                        break
                    cprint("Unauthorized", "red")
                    continue
        while keycode == "441":
            print()
            cprint("User logged into NDRGRND Private Database", "green")
            print()
            options = [
                "History files 1",
                "History files 2",
                "Network Sharing",
            ]
            selection = show_menu(options)
            match selection:
                case "1":
                    print()
                    print(
                        "Just before the end of the WWII, two German provision U-boats, U-530 and U-977,"
                    )
                    print(
                        "were launched from a port on the Baltic Sea. Reportedly they took with them members"
                    )
                    print(
                        "of the antigravity-disk research and development teams [ULTRA], and the LAST of the"
                    )
                    print(
                        "most vital disc components [much of this technology and hardware had been transported"
                    )
                    print("to the base during the course of the war].")
                    print()
                    print(
                        "This included the notes and drawings for the latest saucer or aerial disk designs,"
                    )
                    print(
                        "and designs for the gigantic underground complexes and living accommodations based on"
                    )
                    print(
                        "the remarkable underground factories of Nordhausen in the Harz Mountains."
                    )
                    print(
                        "The two U-boats duly reached the new land of Neu-Schwabenland where they unloaded"
                    )
                    print(
                        "everything. When they arrived in Argentina several months later, their crews were captured."
                    )
                    print(
                        "It seems as if they were either counting on the formerly German-friendly Argentineans to"
                    )
                    print(
                        "allow them access, or it could have been that they intentionally allowed themselves to be"
                    )
                    print(
                        'discovered for misinformation purposes, i.e. -- "yes... we are the last two renegade German'
                    )
                    print(
                        "subs. We've been trying to hold out but...oops, you caught us... the war's finally over!\" "
                    )
                    print()
                    input("Press a key")
                    continue
                case "2":
                    print()
                    print(
                        "The Antarcticans were desperate following the war, and knew that a confrontation was imminent."
                    )
                    print(
                        "Much effort was put into developing secret weapons projects to defend their new underground"
                    )
                    print(
                        "Empire, which no doubt was constructed with the 'help' of a large number of expendable"
                    )
                    print(
                        "slave laborers transported from the concentration camps of Europe."
                    )
                    print()
                    print(
                        "The major base-city of Antarctica became known as the NEW BERLIN,"
                    )
                    print('or by the code-named "Base-211". ')
                    print(
                        "The crews of these U-Boats were of course interrogated by U.S. Intelligence agents who"
                    )
                    print(
                        "had suspected the existence of the Antarctic base. Whatever the Nazi soldiers tried to tell"
                    )
                    print(
                        "them, apparently the Americans were not convinced... especially considering the subsequent"
                    )
                    print(
                        'and ill-fated U.S. Navy backed military actions against the Nazi\'s "Last Battalion" in'
                    )
                    print(
                        "Antarctica in later years under Admiral Richard E. Byrd, who arrived at Antarctica with"
                    )
                    print(
                        "an entire military armada and provisions to last 6 month. However the the entire"
                    )
                    print(
                        "expedition lasted only 8 weeks, with only approximately three weeks of actual"
                    )
                    print("full-scale Antarctic operations.")
                    print()
                    input("Press a key")
                    continue
                case "3":
                    print()
                    share = input(
                        "Enter a name of a registered organizations to share access with: "
                    )
                    if share == "zrio":
                        message = [
                            "We have dolphins, the government and now nazis!",
                            "Sounds like a big conspiracy theory to me.",
                            "In fact, I was conducting some investigations myself but I need your help with something to prove it;",
                            "I was able to track a package that's going through the military Post Office.",
                            "You need to track it down and deliver it to me.",
                            "Package number is: 883597",
                            "You need to redirect it to: 26 Masen Av New York USA",
                            "Post office site is: postoffice.mil",
                            "Be careful, I have a very bad feeling",
                        ]
                        self.mail.add_message(
                            from_user="zrio",
                            subject="pipelink",
                            message="\n".join(message),
                        )
                        return
                    else:
                        continue
                case _:
                    return

    def http_09pipelink(self):
        print()
        cprint("Unauthorized access\nConnection closed", "red")
        print()
