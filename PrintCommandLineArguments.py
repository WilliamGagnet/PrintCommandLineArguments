import sys

# number of command line arguments
argc = len(sys.argv)

if argc == 1:
    print("No command line arguments")

else:
    # prints out all command line arguments
    for i in range(1, argc):
        print(sys.argv[i])