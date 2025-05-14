import os
import argparse
from rich.console import Console
console = Console() 
parser = argparse.ArgumentParser(usage="""

 1.enter the source location of the folder you want to compare(this well be the Comparsion refrence)
 2.enter second folder address(the folder you want to compare with.)
 E.g:
 Enter source location: D:/ 
 Enter folder to compare (or press Enter to quit): D:/project 
 if you want to address a folder which is in your Android device:
 first you need to enable Android Debugging(Consult your device manufacturer.)
 you have to enter address like this:/sdcard/dcim/camera
 Have A Good Time \u2764\uFE0F
""")
parser.add_argument('-V', '--version',
                    action="version",version="%(prog)s 1.0")

def welcome():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
    console.print(""" 
 _____ _ _         _                _                    
|  ___(_) | ___   / \   _ __   __ _| |_   _ _______ _ __ 
| |_  | | |/ _ \ / _ \ | '_ \ / _` | | | | |_  / _ \ '__|
|  _| | | |  __// ___ \| | | | (_| | | |_| |/ /  __/ |   
|_|   |_|_|\___/_/   \_\_| |_|\__,_|_|\__, /___\___|_|   
                                      |___/              
""")
    
    console.print("""
[magenta]Hello and Welcome to FileAnalyzer.           
This tool well help you to make suer you backedup everything :)[/magenta]
          
Copyright 2024 Licensed under the GNU-GPL3 License. 
Author: https://github.com/U0105 
Contact: nvpjxvh8s@mozmail.com
For more help : python FileAnalyzer.py -h or --help
Version: 1.0
                  """)

welcome()