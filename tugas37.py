import time
import os

for i in range(30):
    os.system("cls")
    print("\n" * 20 + " " * i + "0", end="", flush=True)
    time.sleep(0.1)

for i in range(29, -1, -1):
    os.system("cls")
    print("\n" * 20 + " " * i + "0", end="", flush=True)
    time.sleep(0.1)

print()