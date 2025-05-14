from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5.uic import loadUi
import sys, os
import os
from android import android_file
class Main(QMainWindow):
    def __init__(self):
        super(Main,self).__init__()
        loadUi("main.ui",self)
        self.current_path= None
        self.setWindowTitle("Untitled")
        self.Qpush
    def compare(file_list1 ,file_list2,):
            x=0
            for filename in file_list1:
                x+=1
                if filename not in file_list2:
                    print(f"index number:\t#{x}\nfile name:\t#{filename}\nwere NOT exist." )
            print(f"{x} files were counted.")

    try:    
        while True:

            file_source1= str(input("enter first floder: "))
            file_source2= str(input("enter socend floder: "))
            if "sdcard" in file_source1:
                file_list1=android_file(file_source1)
            if "sdcard" in file_source2:
                file_list2=android_file(file_source2)
            if "sdcard" not in file_source1:
                os.chdir(file_source1)
                file_list1 = os.listdir()
            if "sdcard" not in file_source2:
                os.chdir(file_source2)
                file_list2 = os.listdir()  
            compare(file_list1,file_list2)
    except KeyboardInterrupt:
                print("\nctrl + c is pressed. tool was closed.")
