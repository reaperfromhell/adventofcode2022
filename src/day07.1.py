#!/usr/bin/python
# Python3 program to solve adventofcode.com/2022

class File:
    def __init__(self, name, size, parent_dir):
        self.name = name
        self.parent_dir = parent_dir
        self.size = size

    def get_size_str(self):
        return self.size

class Directory:
    def __init__(self, name, parent_dir):
        self.name = name
        self.files = []
        self.directories = []
        self.parent_dir = parent_dir
    
    def create_file(self, name, size):
        for file in self.files:
            if file.name == name:
                return
        new_file = File(name, size, self)
        self.files.append(new_file)
    
    def create_directory(self, name):
        for directory in self.directories:
            if directory.name == name:
                return
        new_dir = Directory(name, self)
        self.directories.append(new_dir)
    
    def list_contents(self):
        print("Files:")
        for file in self.files:
            print(" " + file.name)
        print("Directories:")
        for directory in self.directories:
            print(" " + directory.name)

    def get_size(self):
        size = 0
        for file in self.files:
            size += file.size
        for directory in self.directories:
            size += directory.get_size()
        return size

class Filesystem:
    def __init__(self):
        self.current_dir = Directory("root", None)
        self.root_dir = self.current_dir

    def navigate(self, path):
        if path == "/":
            self.current_dir = self.root_dir
        else:
            elements = path.split("/")
            for element in elements:
                if element == "..":
                    self.current_dir = self.current_dir.parent_dir
                else:
                    found = False
                    for directory in self.current_dir.directories:
                        if directory.name == element:
                            self.current_dir = directory
                            found = True
                            break
                    if not found:
                        raise Exception("Directory not found")


    def get_directory_size(self, path):
        self.navigate(path)
        return self.current_dir.get_size()


folder_size = 0

def traverse_size(directory):
    global folder_size
    for subdir in directory.directories:
        tmp = subdir.get_size()
        if tmp < 100000:
            folder_size += tmp
        traverse_size(subdir)


with open("../input/day7.txt") as file_in:
    fs = Filesystem()
    for line in file_in:
        sline = line.strip().split(" ")
        if sline[1] == 'ls':
            pass
        if sline[1] == 'cd':
            fs.navigate(sline[2])
        if sline[0] == 'dir':
            fs.current_dir.create_directory(sline[1])
        if sline[0].isdecimal():
            fs.current_dir.create_file(sline[1], int(sline[0]))
traverse_size(fs.root_dir)
print(folder_size)