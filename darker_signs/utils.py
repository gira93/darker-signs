import os
from time import sleep


def progress_bar(max=100, step=0.05):
    progress = 0
    bars = ["|", "/", "-", "\\"]
    while progress != max:
        bar = progress % len(bars)
        print(f"\r{progress}% {bars[bar]}", end="")
        progress += 1
        sleep(step)
    print(f"\r{max}% done")
    return


def upload_file(absolute_path):
    if os.path.isfile(absolute_path):
        progress_bar(max=100, step=0.02)
        return True
    else:
        return False


def download_file(absolute_path, contents=""):
    with open(absolute_path, "w") as f:
        f.write(contents)
    progress_bar(max=100, step=0.02)
    return True
