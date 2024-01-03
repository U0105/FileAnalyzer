import os
from android import android_file

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
        