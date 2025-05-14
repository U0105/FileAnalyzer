import os
from android import android_file
from rich.console import Console
from rich.table import Table

console = Console()

class FileComparison:
    def __init__(self, source_location):
        self.source_location = source_location
        self.source_file_list = self._get_file_list(source_location)

    def _get_file_list(self, location):
        if "sdcard" in location:
            return android_file(location)
        else:
            file_list = []
            for root, _, files in os.walk(location):
                for file in files:
                    file_path = os.path.join(root, file)
                    relative_path = os.path.relpath(file_path, location)
                    file_list.append(relative_path)
            return file_list

    def compare_with_folder(self, folder_location):
        folder_file_list = self._get_file_list(folder_location)
        self._compare_file_lists(self.source_file_list, folder_file_list)

    def _compare_file_lists(self, list1, list2):
        table = Table(title="Comparison Results")
        table.add_column("No.", style="cyan")
        table.add_column("Source File", style="magenta")
        table.add_column("Status", style="green")
        
        target_files = set(list2)
        
        for idx, filename in enumerate(list1, 1):
            status = "✅" if filename in target_files else "❌"
            table.add_row(str(idx), filename, status)
        
        console.print(table)
        console.print(f"Total compared files: [yellow]{len(list1)}[/yellow]")