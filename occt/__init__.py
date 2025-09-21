# occt/__init__.py

# Read package.json file for description and version
import json

# file path to package.json
PACKAGE_JSON_PATH = "package.json"
package_info = {}
with open(PACKAGE_JSON_PATH, "r") as f:
    package_info = json.load(f)
    description = package_info.get("description", "No description available.")
    version = package_info.get("version", "0.0.0")


# ANSI color codes
BLACK = "\033[30m"
WHITE = "\033[97m"
CYAN = "\033[96m"
YELLOW_BG = "\033[43m"
DIM = "\033[2m"
RESET = "\033[0m"


# CLI info
title = " OCCT "
version = f"v{version}"
tagline = "Learn more, innovate more!!"
description = description


def show_banner():
    # Clear the terminal screen
    print("\033c", end="")
    # Title with yellow background and black text
    print(f"{YELLOW_BG}{BLACK}{title}{RESET} {version} {DIM}{tagline}{RESET}")
    # Description in cyan
    print(f"{DIM}{description}{RESET}")
    print()


def run():
    show_banner()
