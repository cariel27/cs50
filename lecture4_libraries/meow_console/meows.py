import sys

# meows -h

if len(sys.argv) == 1 or len(sys.argv) == 2 and sys.argv[1] == "-n":  # meows or meows -n
    print("meow")
elif len(sys.argv) == 3 and sys.argv[1] == "-n":  # meows -n x
    n = int(sys.argv[2])
    for _ in range(n):
        print("meow")
else:
    print("usage: meows.py")

