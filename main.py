from rich import print

opening_block = """
[blue bold]===========================================[/blue bold]
            [green bold]TASKER[/green bold] — [red bold]v1.0.0[/red bold]
    A simple, fast, plain-text todo app
[blue bold]===========================================[/blue bold]

Author: Henry Knight
License: Zero-Clause BSD (0BSD)
Source: https://github.com/kdauntln/tasker

TASKER is a fully open-source command-line task manager.
All code is public domain under the 0BSD license.
You can use, modify, fork, redistribute, or sell it—
no strings attached.

No telemetry. No cloud sync. No hidden files.
Just you and your tasks.
"""

help = [
    "help - display a list of commands",
    "todo - display the items on your todo list",
    "add - add a new item to your todo list",
    "complete - mark an item as complete",
    "abandon - abandon an item on your todo list",
    "quit - exit the application"
]

commands = [
    "quit",
    "todo",
    "add",
    "complete",
    "abandon",
    "help"
]

print(opening_block)

running = True
while running:
    command = input("> ")

    if command.lower() in commands:
        if command == "quit":
            print("Implement this")
    else:
        print(f"[red]'{command}' was not recognised as a valid command or item. Check the spelling of the command, or if an argument was included, verify that the argument is correct and try again.[/red]")