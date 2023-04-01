import argparse

parser = argparse.ArgumentParser(description="Meow like a cat")
parser.add_argument("-n", help="number of times to meow", default=1, type=int)
args = parser.parse_args()

for _ in range(args.n):
    print("meow")
