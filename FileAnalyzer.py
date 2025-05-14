import os 
from rich.console import Console
from Fun import FileComparison
import header

if __name__ == "__main__":
    
    ps = header.parser.parse_args()
    console = Console()
    try:
        header.welcome()
        source_location = console.input("\n[blue]Enter source location: ")
        if not source_location:
            exit()
        comparison = FileComparison(source_location)
        while True:
            folder_location = console.input("[blue]Enter folder to compare (or press Enter to quit): ")
            if not folder_location:
                break
            comparison.compare_with_folder(folder_location)
    except KeyboardInterrupt:
        console.print("\n[bold red]Ctrl + C is pressed. Tool was closed.[/bold red]")
