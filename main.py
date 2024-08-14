import os
import shutil
import sys
import time

import pyperclip
from pyfiglet import Figlet
from rich.console import Console

console = Console()


def clear_terminal():
    """Clear the terminal screen."""
    os.system("cls" if os.name == "nt" else "clear")


def center_text(text):
    """Center text both horizontally and vertically on the terminal."""
    terminal_size = shutil.get_terminal_size()
    lines = text.split("\n")
    centered_lines = [line.center(terminal_size.columns) for line in lines]

    # Calculate padding for vertical centering
    padding_lines = (terminal_size.lines - len(centered_lines)) // 2

    # Add padding lines before and after the centered text
    padded_text = (
        "\n" * padding_lines + "\n".join(centered_lines) + "\n" * padding_lines
    )

    return padded_text


def display_text(text, words_per_minute):
    """Display text at the specified words per minute."""
    words = text.split()
    delay = 60.0 / words_per_minute
    figlet = Figlet(font="slant")  # You can change the font style here

    for word in words:
        clear_terminal()
        large_text = figlet.renderText(word)
        centered_text = center_text(large_text)

        # Use Rich to style and display the text
        console.print(centered_text, style="bold bright_green")

        time.sleep(delay)


def main():
    console.print("start")

    """Main function to run the rapid reader."""
    text = pyperclip.paste()

    if not text:
        print("Clipboard is empty.")
        return

    try:
        if len(sys.argv) == 1:
            words_per_minute = 400
        else:
            words_per_minute = int(sys.argv[1])
        display_text(text, words_per_minute)
    except ValueError:
        print("Invalid words per minute. Argument must be an integer.")
    return


if __name__ == "__main__":
    main()
