import sys

# if one argument is provided
if len(sys.argv) > 1:
    try:
        with open(sys.argv[1], "r") as file:    
            content = file.read()
            print(content)
    except:
        print("unable to open file")
else:
    print("No input provided")

