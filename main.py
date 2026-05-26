import sys
import sqlite3
from pathlib import Path
import datetime
import requests 
import json

def menu():
    print("Github tag tracker,")
    print("used to keep track of repo versions and updates.\n")
    print("Usage: ")
    print("$ uv run main.py <argument> (<repo>)")
    print("     -h | --help: displays this menu,")
    print("     -v | --version: displays version,")
    print("     -a | --add <repo>: adds repo (1) to be tracked,")
    print("     -r | --remove <repo>: removes (1) repo from database,")
    print("     -l | --list: lists all repos added to database,")
    print("     -u | --update: updates repo tags,")
    print("     -d | --display: displays any recently updated tags.\n")

    print("NOTE:")
    print("For <repo>, enter the 'creator/repo' that is found")
    print("at the end of a github link,")
    print("e.g. for 'https://github.com/swaywm/sway'")
    print("enter 'swaywm/sway'.\n")

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


def insertRepoData(latestTag):
    pass


def fetchTag(repoUrl):
    repoUrl = f"{repoUrl}/releases"
    releasesApi = requests.get(repoUrl)

    if (releasesApi.status_code != 200):
        sys.exit(">> Repo doesn't have tags to add :(\n")

    releases = releasesApi.json()

    if not releases:
        sys.exit(">> No tags/releases found :(\n")

    latestTag = releases[0]["tag_name"]

    if not latestTag:
        sys.exit(">> No tag_name found :(\n")

    print(f">> Repo has tags, found: {latestTag}!")

    try:
        numericTag = latestTag.lstrip("v")
        latestTag = eval(latestTag)
        print(">> Successfully processed latest tag!\n")
    except:
        sys.exit(">> Tag isn't numerical :(\n")

    insertRepoData(latestTag)


def testExistance():
    repo = sys.argv[2]
    repoUrl = f"https://api.github.com/repos/{repo}"
    print(f"> Probing: {repoUrl}")
    test = requests.get(repoUrl)

    if (test.status_code == 200):
        print(">> Repo exists!\n")
        fetchTag(repoUrl)
    else:
        print(">> Repo either doesn't exist or the name is misinput :( ")
        sys.exit(">> Please try again \n")


def listRepos():
    pass

def rmRepoData():
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

    elif (sys.argv[1] == "-h" or sys.argv[1] == "--help"):
         menu()

    elif (sys.argv[1] == "-v" or sys.argv[1] == "--version"):
        version()

    elif (sys.argv[1] == "-a" or sys.argv[1] == "--add"):
        if(len(sys.argv) == 3):
            testExistance()
        else:
            print("> Incorrect arguments\n")
            menu()

    elif (sys.argv[1] == "-r" or sys.argv[1] == "--remove"):
        if(len(sys.argv) == 3):
            rmPackage()
        else:
            print("> Incorrect arguments\n")
            menu()

    elif (sys.argv[1] == "-l" or sys.argv[1] == "--list"):
        listRepos()

    elif (sys.argv[1] == "-u" or sys.argv[1] == "--update"):
        updateTags()

    elif (sys.argv[1] == "-d" or sys.argv[1] == "--display"):
        displayChanges()

if __name__ == "__main__":
    main()
