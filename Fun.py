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
            os.chdir(location)
            listdir = []
            for root, dirs, files in os.walk(location):
                _root = root
                listdir = dirs
                _file = files
            return listdir


    def compare_with_folder(self, folder_location):
        folder_file_list = self._get_file_list(folder_location)
        self._compare_file_lists(self.source_file_list, folder_file_list)

    def _compare_file_lists(self, list1, list2):
        table= Table(title= "Result")
        table.add_column("No.")
        table.add_column("Source Files",style="magenta")
        table.add_column("compare",style="green")
        x = 0
        for filename in list1:
            x += 1
            table.add_row(f"{x}",filename)
            if filename not in list2:
                table.add_row(None,None,(":cross_mark:"))
            else:
                table.add_row(None,None,(":heavy_check_mark:"))
        console.print(table)
        console.print(f"{x} [yellow]files were counted.")
