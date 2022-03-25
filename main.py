import os

print("Sreaching a string at all the file in a specific folder \n ")
user_path2folder = input(r"Please provide the path to the folder: ") # ask for the path
user_string = input(r"What is the string you want to look for: ") #ask for the string


# print(os.path.exists(user_path2folder))
if  os.path.exists(user_path2folder):
    print(os.system('dir')) #check the current folder location (to clarify what folder you are in)
    for file in os.listdir(user_path2folder):
        f = os.path.join(user_path2folder, file)
        if os.path.isfile(f): #check if it is a file
            with open(f) as myfile:
                if user_string in myfile.read(): #check if this string is existed
                    print(f + " file")
                    save_file = open(r'copy the path for the folder you want to save it to', 'a') # for example C:filewithstring.txt
                    save_file.write(f)
                    save_file.close()
        if os.path.isdir(f):
            new_path = f
            print(new_path)
            for file2 in os.listdir(new_path):

                f2 = os.path.join(new_path,file2)
                print(f2 + " inside subdir")
                if os.path.isfile(f2):
                    with open(f2 , errors="ignore") as myfile2:
                        if user_string in myfile2:  # check if this string is existed
                            print(f2 + " file")
                            save_file = open(r'copy the path for the folder you want to save it to', 'a')  # for example C:filewithstring.txt
                            save_file.write(f2)
                            save_file.close()

else:
    print("Invalid Path")
