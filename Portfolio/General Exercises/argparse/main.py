import argparse

# ------------------------------- Squaring the argument given.

# parser = argparse.ArgumentParser()
# parser.add_argument("square", help="Squares a given number", type=int)
# args = parser.parse_args()
# print(args.square**2)


# ------------------------------- Simple greet with some optional arguments.

# parser = argparse.ArgumentParser()
# parser.add_argument("greet", help="Greets the name given.")
# parser.add_argument("--shout", help="Makes the greet all-caps", action="store_true")
# parser.add_argument("--greeting", help="Form of greeting, defaults to 'Hello'", default="Hello")
#
# args = parser.parse_args()
#
# message = f"{args.greeting}, {args.greet}!"
# if args.shout:
#     message = message.upper()
#
# print(message)


# ------------------------------- Simple operations using argparse

# parser = argparse.ArgumentParser()
#
# parser.add_argument("a", help="First number used", type=int)
# parser.add_argument("b", help="Second number used", type=int)
# parser.add_argument("--op", choices=["add", "sub", "mul", "div"], help="Operation to perform", default="add")
#
# args = parser.parse_args()
#
# if args.op == "add":
#     print(args.a + args.b)
# elif args.op == "sub":
#     print(args.a - args.b)
# elif args.op == "mul":
#     print(args.a * args.b)
# elif args.op == "div":
#     print(args.a / args.b)


# ------------------------------- Practice with multiple values (nargs)

parser = argparse.ArgumentParser()

parser.add_argument("numbers", help="List of floats", nargs="+", type=float)

args = parser.parse_args()

print(sum(args.numbers))