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
