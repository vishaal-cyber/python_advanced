#!/usr/bin/env py
import sys
import os


# int main(int argc, char* argv[])
# {}

def demo_sys():
    print("Comand-line args -->")
    for idx, arg in enumerate(sys.argv):
        print(f"\t Arg {idx} --> {arg}")

    # sys.path
    print(f"{type(sys.path) = }")
    for idx, path in enumerate(sys.path):
        print(f"{idx} --> {path}")
    
    print(f"{sys.version = }")


# demo_sys()

def demo_os():
    current_dir = os.getcwd()
    print(f"Current directory --> {current_dir}")

    # Create a new folder
    new_dir = os.path.join(current_dir, 'demo_dir')
    if not os.path.exists(new_dir):
        os.mkdir(new_dir)
        print(f"Directory 'demo_dir' created at {new_dir}")
    else:
        print(f"Directory 'demo_dir' already exists at {new_dir}")

    # List all files and directories in the current directory
    print("Files and Directories in the current directory -->")
    for item in os.listdir(current_dir):
        print("\t", item)

    # Create a new file in the new dir
    new_file_path = os.path.join(new_dir, 'demo_file.txt')
    # print(f"Will create the file {new_file_path} in a bit.")
    file_operations(new_file_path)



    #  Remove the file
    if os.path.exists(new_file_path):
        os.remove(new_file_path)
        print(f"\nFile 'demo_file.txt' removed from {new_file_path}.")
    else:
        print(f"\nFile not found at {new_file_path}.")

    # Remove the directory
    os.rmdir(new_dir)
    print(f"\nDirectory 'demo_dir' removed from {new_dir}.")
    
def file_operations_1(new_file_path):
    try:
        file = open(new_file_path, mode='w')
        file.write("This is a demo file.")
        # file.close()
    # except Exception:
    #     pass
    finally:
        file.close()

    print(f"File 'demo_file.txt' was created at {new_file_path}.")

    # Read from the file
    if os.path.exists(new_file_path):
        with open(new_file_path) as file:
            fileData = file.read()
        print(f"\nThe file at {new_file_path} has the contents as below:\n\t'{fileData}'")
    else:
        print(f"\nFile not found at {new_file_path}.")

def file_operations_2(new_file_path):

    lst = ["\nSome lines\n", "More line\n", "yet some more\n"]
    with open(new_file_path, mode='w') as file:
        file.write("This is a demo file.")
        file.write("And this is some more data")
        file.writelines(lst)

    print(f"File 'demo_file.txt' was created at {new_file_path}.")

    # Read from the file
    if os.path.exists(new_file_path):
        with open(new_file_path) as file:
            fileData = file.read()
            # fileData = ""
            # for line in file:
            #     readData = file.read(512)
            #     file.readlines()
            #     fileData += readData
        print(f"\nThe file at {new_file_path} has the contents as below:\n\t'{fileData}'")
    else:
        print(f"\nFile not found at {new_file_path}.")

def file_operations(new_file_path):
    file_operations_2(new_file_path)

demo_os()