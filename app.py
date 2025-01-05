import sys

if len(sys.argv) >1:
    user_input = " ".join(sys.argv[1:])
    print(user_input)
else:
    print("No input provided")

