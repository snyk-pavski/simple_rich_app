from rich.console import Console
from rich.panel import Panel

def main():
    # Create a console object
    console = Console()

    # Print some styled text
    console.print("\nHello! This script is running with Poetry.", style="bold green")

    # Print a panel demonstrating the 'rich' dependency
    console.print(Panel.fit(
        "[bold yellow]This project uses:[/bold yellow]\n\n"
        " * Poetry for dependency management\n"
        " * pyproject.toml for configuration\n"
        " * The 'rich' library for this panel",
        title="My Simple Project",
        padding=(1, 2)
    ))

    console.print("\nPoetry setup is working! :rocket:\n")

if __name__ == "__main__":
    main()