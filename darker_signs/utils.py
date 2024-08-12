import os
from time import sleep


def progress_bar(max: int = 100, step: float = 0.05) -> None:
    progress = 0
    bars = ["|", "/", "-", "\\"]
    while progress != max:
        bar = progress % len(bars)
        print(f"\r{progress}% {bars[bar]}", end="")
        progress += 1
        sleep(step)
    print(f"\r{max}% done")
    return


def upload_file(absolute_path: str) -> bool:
    if os.path.isfile(absolute_path):
        progress_bar(max=100, step=0.02)
        return True
    else:
        return False


def download_file(absolute_path: str, contents: str = "") -> bool:
    with open(absolute_path, "w") as f:
        f.write(contents)
    progress_bar(max=100, step=0.02)
    return True


def show_menu(
    options: list[str],
    abort_message: str = "Exit",
    selection_message: str = "Make a selection",
) -> str:
    print("")
    formatted_options = ""
    for idx, option in enumerate(options):
        formatted_options += f"{idx + 1}) {option}\n"
    formatted_options += f"\n0) {abort_message}"
    valid_inputs = [str(x) for x in range(0, len(options) + 1)]
    while True:
        print(formatted_options)
        selection = input(f"{selection_message}: ")
        if selection in valid_inputs:
            return selection
