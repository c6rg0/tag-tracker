# Package version/tag tracker
- Writes and updates github version numbers
- Can be used to figure out if a new version of a repo exists

## Why?
- If a package has a new version, I want to know so that I can update it for my package manager 
- Previously, I used the github home page, but I don't like it

## How to run
- Easy way:
  - Install `astral-uv`, and run it using the command under the usage header.
- The complicated way:
  - Set the project up manually using the info given in `pyproject.toml` and `pip`.

## Usage:
`$ uv run main.py <argument> (<repo>)`\
`     -h | --help: displays this menu,`\
`     -v | --version: displays version,`\
`     -a | --add <repo>: adds repo (1) to be tracked,`\
`     -r | --remove <repo>: removes (1) repo from database,`\
`     -l | --list: lists all repos added to database,`\
`     -u | --update: updates repo tags,`\
`     -d | --display: displays any recently updated tags.`

`NOTE:`\
`For <repo>, enter the 'creator/repo' that is found`\
`at the end of a github link,`\
`e.g. for 'https://github.com/swaywm/sway'`\
`enter 'swaywm/sway'.`

