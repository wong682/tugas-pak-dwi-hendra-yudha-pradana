import time

for i in range(30):
    print("\r" + " " * 30 + "\r" + " " * i + "0", end="", flush=True)
    time.sleep(0.1)

for i in range(29, -1, -1):
    print("\r" + " " * 30 + "\r" + " " * i + "0", end="", flush=True)
    time.sleep(0.1)

print()