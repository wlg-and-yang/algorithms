import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--square", default=3, help="display a square of a given number", type=int)
parser.add_argument("--verbosity", help="increase output verbosity", action="store_true")
args = parser.parse_args()

print(args.square**2)

if args.verbosity:
    print("verbosity turned on")



