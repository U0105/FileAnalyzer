import os

dest1= str(input("enter first floder: "))

os.chdir(dest1)
dest1_files = os.listdir()
dest1_len = len(dest1_files)

dest2= str(input("enter socend floder: "))

os.chdir(dest2)
dest2_files = os.listdir()
dest2_len = len(dest2_files)

for n in range(dest1_len):
   
    if dest1_files[n] in dest2_files:
        pass
    else:
        print(f"index number:\t#{n}\nfile name:\t#{dest1_files[n]}\nwere NOT exist." )
        pass
    