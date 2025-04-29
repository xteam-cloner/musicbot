import os


API_ID: int = int(os.getenv("API_ID", "22049281"))

API_HASH: str = os.getenv("API_HASH", "0377071c177fea820b5086cb8298ed64")

SESSION_STRING: str = os.getenv("SESSION_STRING", "")

OWNER_ID: list[int] = [int(os.getenv("OWNER_ID", "1434595544"))]

LOG_GROUP_ID: int = int(os.getenv("LOG_GROUP_ID", "-1002385138723"))

PREFIX: str = str(".")

RPREFIX: str = str("$")


# No Need To Edit Below This

LOG_FILE_NAME: str = "YMusic.txt"
