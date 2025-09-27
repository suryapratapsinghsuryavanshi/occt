import argparse
import sys
from rich.console import Console

console = Console()

def print_help():
    console.print("Usage:", style="bold")
    console.print("  python -m occt [", end="")
    console.print("--options", style="yellow", end="")
    console.print("] ", end="")
    console.print("<command>", style="cyan")
    console.print()

    console.print("Options:", style="bold")
    console.print("  -c, ", style="yellow", end=""); console.print("--compile", style="yellow", end="")
    console.print("         Pass flag for Compiled Code output file. [Auto Detect OS and Programming, and save output file]")

    console.print("  -o, ", style="yellow", end=""); console.print("--output", style="yellow", end="")
    console.print("          Pass flag only used with -c flag, for output file custom name.")

    console.print("  -i, ", style="yellow", end=""); console.print("--interpreted", style="yellow", end="")
    console.print("     Pass flag for interpret Code output only.")

    console.print("  -a, ", style="yellow", end=""); console.print("--args", style="yellow", end="")
    console.print("            After this flag all value consider as command line arguments.")

    console.print("  -d, ", style="yellow", end=""); console.print("--debug", style="yellow", end="")
    console.print("           Print debug information if needed.")

    console.print("  -v, ", style="yellow", end=""); console.print("--version", style="yellow", end="")
    console.print("         Print version information.")

    console.print("  -h, ", style="yellow", end=""); console.print("--help", style="yellow", end="")
    console.print("            Print the help information.")

    console.print("  --clear", style="yellow", end="")
    console.print("               Clear the terminal window. (default: true)")

    console.print("  --no-clear", style="yellow", end="")
    console.print("            Don't clear the terminal window.")
    console.print()

    console.print("Commands:", style="bold")
    console.print("  help", style="cyan", end="")
    console.print("                  Print the help information.")
    console.print()

    console.print("Example:", style="bold")
    console.print("  python -m occt ", end=""); console.print("-c", style="yellow", end=""); console.print(" ./main.cpp ", end=""); console.print("-o", style="yellow", end=""); console.print(" main")
    console.print("  python -m occt ", end=""); console.print("-i", style="yellow", end=""); console.print(" ./app.js")
    console.print()
