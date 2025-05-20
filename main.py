from rich import print
from utils import open_app

open_app("Todo", "0.1.0", "help")

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

running = True
while running:
    command = input("> ")

    if command.lower() in commands:
        if command == "quit":
            print("Implement this")
    else:
        print(f"[red]'{command}' was not recognised as a valid command or item. Check the spelling of the command, or if an argument was included, verify that the argument is correct and try again.[/red]")