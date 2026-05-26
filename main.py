import sys
import sqlite3
from pathlib import Path
import datetime
import requests 

def menu():
    print("Github tag tracker,")
    print("Version 0.1.0,")
    print("Used to keep track of package versions and updates.\n")
    print("Usage: ")
    print("     -h | --help: displays this menu,")
    print("     -v | --version: displays version,")
    print("     -a | --add: add package (1) to be tracked,")
    print("     -r | --remove: remove (1) package,")
    print("     -u | --update: update package tags,")
    print("     -d | --display: display recently updated tags.")

def version():
    print("Github tag tracker,")
    print("Version 0.1.0.")

def createTable():
    print("> Creating table")
    connectionObj = sqlite3.connect('packages.db')
    cursorObj = connectionObj.cursor()

    tableCreationQuery = """
        CREATE TABLE PACKAGES (
            name TEXT PRIMARY KEY,
            repo TEXT NOT NULL,
            version INT,
            lastUpdate '%F' 
        );
    """

    cursorObj.execute(tableCreationQuery)
    print(">> Table is Ready\n")
    connectionObj.close()


def fetchData():
    pass

def addPackage():
    pass


def rmPackage():
    pass
 

def updateTags():
    pass


def displayChanges():
    pass


def main():
    dbLoc = Path("./packages.db")
    if not dbLoc.is_file():
        createTable()

    if (len(sys.argv) == 1):
        menu()
    elif (sys.argv[1] == "-h" or "--help"):
        menu()

    elif (sys.argv[1] == "-v" or "--version"):
        version()

    elif (sys.argv[1] == "-a" or "--add"):
        addPackage()

    elif (sys.argv[1] == "-r" or "--remove"):
        rmPackage()

    elif (sys.argv[1] == "-u" or "--update"):
        updateTags()

    elif (sys.argv[1] == "-d" or "--display"):
        displayChanges()

if __name__ == "__main__":
    main()
