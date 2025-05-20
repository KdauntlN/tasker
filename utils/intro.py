from rich import print

def open_app(name, version, help_command):
    print(f"Opening [green bold]{name}[/green bold] version [blue bold]{version}[/blue bold]...")
    print(f"Type [red bold]{help_command}[/red bold] for a list of commands")