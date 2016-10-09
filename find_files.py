import sys,os
import json

# root = "C:/"
root  = os.getcwd() #get current working directory

path = os.path.join(root, "targetdirectory")
# print(path)

foundFiles = []

for path, subdirs, files in os.walk(root):
    for name in files:
        file = str(os.path.join(path, name))
        file = file.replace("\\","/",len(file))
        foundFiles.append(file)

# print(foundFiles)
out_file = open("found_files.json","w")

my_dict = {
	'files':	foundFiles
}


json.dump(my_dict,out_file, indent=4)

out_file.close()