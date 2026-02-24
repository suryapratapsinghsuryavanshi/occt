# occt/__init__.py

# Read package.json file for description and version
from .states import uploading_file_compile, uploading_file_interprate
from pathlib import Path

description = "Online Compiler Collection Tool"
version = "1.2.0"


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

def show_extra_options(args, console, print_help):
    if args.version:
        console.print(f"Version: {version}", style="cyan")
    elif args.compile:
        flags_compile = {
            "compile": args.compile,
            "outputFile": args.output,
            "args": args.args
        }
        uploading_file_compile(flags_compile)
    elif args.interpreted:
        flags_interpreted = {
            "interpreted": args.interpreted,
            "args": args.args
        }
        uploading_file_interprate(flags_interpreted, cli={"input": ["extra"], "flags": {"args": True}})
    else:
        print_help()

def run():
    show_banner()
