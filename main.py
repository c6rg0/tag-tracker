import sys
import http

def menu():
    print("# Github tag tracker #")
    print("Used to keep track of package versions and updates.")
    print("Usage: ")
    print("     -h | --help: displays this menu,")
    print("     -v | --version: displays version,")
    print("     -a | --add: add package (1) to be tracked,")
    print("     -r | --remove: remove (1) package,")
    print("     -u | --update: update package tags,")
    print("     -d | --display: display recently updated tags,")
    # print("\n")

def version():
    print("# Github tag tracker #")
    print("Version 0.1.0")

def main():
    if (len(sys.argv) == 1):
        menu()
    elif (sys.argv[1] == "-h" or "--help"):
        menu()
    elif (sys.argv[1] == "-v" or "--version"):
        version()


if __name__ == "__main__":
    main()
