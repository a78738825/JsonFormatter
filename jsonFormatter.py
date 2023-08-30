import os
import json

Files = []

def formatter(files):
    for f in files:
        fname = f.split(".")
        try:
            with open(f,"r") as jsonfile:
                formattedData=json.loads(jsonfile.read())
                formattedData=json.dumps(formattedData, indent=4)
                print(formattedData)
            with open(fname[0]+"(formatted).json", "w") as newfile:
                newfile.write(formattedData)
        except Exception as err:
            print("Error: \n"+str(err))
    return formattedData
    

def input_files(method):
    if method == "m":
        filename= str(input("Enter the file name: "))
        print(filename)
        if (filename[-5:] == ".json") and (filename in os.listdir()):
            Files.append(filename)
        else:
            raise Exception("Invalid file name!")
    elif method == "s":
        for item in os.listdir():
            if (".json" in item) and ("formatted" not in item):
                Files.append(item)
            else:
                continue
    else:
        raise Exception("Not Found!\nEnter 'm' for manual file input , 's' for automatic scan.")
        # input_files()
    
method = input("Enter the file name manually or scan for all json files in the Directory (m- for manual,s- for scan): \n>>>")
input_files(method)

if len(Files) >= 1:
    formatter(Files)
# END
