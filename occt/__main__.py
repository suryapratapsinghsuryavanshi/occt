# occt/__main__.py
import sys
from . import run, show_extra_options
import os
import argparse
import sys
from rich.console import Console
console = Console()
from .help import print_help

def main():
    run()
    if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help", "help"):
        print_help()
        return
    
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("-c", "--compile", type=str)
    parser.add_argument("-o", "--output", type=str)
    parser.add_argument("-i", "--interpreted", type=str)
    parser.add_argument("-a", "--args", nargs=argparse.REMAINDER)
    parser.add_argument("-d", "--debug", action="store_true")
    parser.add_argument("-v", "--version", action="store_true")
    parser.add_argument("--clear", action="store_true", default=True)
    parser.add_argument("--no-clear", action="store_true")

    args = parser.parse_args(sys.argv[1:])

    show_extra_options(args, console, print_help)
        

if __name__ == "__main__":
    main()
