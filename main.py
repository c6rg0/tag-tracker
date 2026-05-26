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
            repo TEXT PRIMARY KEY,
            version INT,
            lastUpdate '%F' 
        );
    """

    cursorObj.execute(tableCreationQuery)
    print(">> Table is Ready\n")
    connectionObj.close()


def insertRepoData(repo, latestTag):
    dbLoc = Path("./packages.db")
    if not dbLoc.is_file():
        createTable()

    print("> Populating database with new entry...")

    connectionObj = sqlite3.connect('packages.db')
    cursorObj = connectionObj.cursor()

    dataInsertQuery = """
        INSERT INTO PACKAGES 
        (repo, version)
        VALUES (?, ?);
    """

    cursorObj.execute(dataInsertQuery, (repo, latestTag))
    connectionObj.close()

    print(">> Successfully inserted data!\n")


def fetchTag(repo, repoUrl):
    print("> Fetching latest release tag...")
    releasesUrl = f"{repoUrl}/releases"
    releasesApi = requests.get(releasesUrl)

    if (releasesApi.status_code != 200):
        sys.exit(">> Repo doesn't have tags to add :(\n")

    releases = releasesApi.json()

    if not releases:
        sys.exit(">> No releases found :(\n")

    latestTag = releases[0]["tag_name"]

    if not latestTag:
        sys.exit(">> Latest release not found :(\n")

    print(f">> Repo has tags, found: {latestTag}!")

    try:
        numericTag = latestTag.lstrip("v")
        latestTag = eval(latestTag)
    except:
        print(">> Tag isn't numerical :(, is it 'nightly'?")
        # May make a bug tracker for this specific bit
        sys.exit("Til next time\n")

    print(">> Successfully processed latest tag!\n")
    insertRepoData(repo, latestTag)


def testExistance():
    print("> Testing connection...")
    testUrl = f"https://api.github.com"
    test = requests.get(testUrl)
    if (test.status_code != 200):
        sys.exit(">> No connection :(, is your intenet or github down?\n")

    repo = sys.argv[2]
    repoUrl = f"https://api.github.com/repos/{repo}"
    print(f"> Probing: {repoUrl}...")

    repoTest = requests.get(repoUrl)
    if (repoTest.status_code != 200):
        print(">> Repo doesn't exist or you mispelt the name :( ")
        sys.exit(">> Please try again \n")

    print(">> Repo exists!\n")
    fetchTag(repo, repoUrl)


def listRepos():
    pass

def rmRepoData():
    pass
 

def updateTags():
    pass


def displayChanges():
    pass


def main():
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
            menu()
            print("> Incorrect arguments\n")

    elif (sys.argv[1] == "-r" or sys.argv[1] == "--remove"):
        if(len(sys.argv) == 3):
            rmPackage()
        else:
            menu()
            print("> Incorrect arguments\n")

    elif (sys.argv[1] == "-l" or sys.argv[1] == "--list"):
        listRepos()

    elif (sys.argv[1] == "-u" or sys.argv[1] == "--update"):
        updateTags()

    elif (sys.argv[1] == "-d" or sys.argv[1] == "--display"):
        displayChanges()

    else:
        menu()
        sys.exit("> Incorrect option chosen\n")


if __name__ == "__main__":
    main()

