import argparse

# ------------------------------- Squaring the argument given.

# parser = argparse.ArgumentParser()
# parser.add_argument("square", help="Squares a given number", type=int)
# args = parser.parse_args()
# print(args.square**2)


# ------------------------------- Simple greet with some optional arguments.

parser = argparse.ArgumentParser()
parser.add_argument("greet", help="Greets the name given.")
parser.add_argument("--shout", help="Makes the greet all-caps", action="store_true")
parser.add_argument("--greeting", help="Form of greeting, defaults to 'Hello'", default="Hello")

args = parser.parse_args()

message = f"{args.greeting}, {args.greet}!"
if args.shout:
    message = message.upper()

print(message)