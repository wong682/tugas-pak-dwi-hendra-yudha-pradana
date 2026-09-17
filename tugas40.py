import time

for i in range(20):
    print("\033[2J\033[H", end="")
    print("\n" * i + " " * 30 + "0", end="", flush=True)
    time.sleep(0.1)

for i in range(19, -1, -1):
    print("\033[2J\033[H", end="")
    print("\n" * i + " " * 30 + "0", end="", flush=True)
    time.sleep(0.1)

print()