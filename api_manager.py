

def search_api_key(name:str):
    name2 = name.strip().lower()
    n = f"{name2}.txt".strip()
    path = f"./api_keys/{n}".strip()
    try:
        file = open(path,"r")
        c = file.readline()
        file.close()
        return c.strip()
    except:
        # raise ValueError(f"no file found in this name : {name}")
        return("no file found in this name")
    
def store_api_key(name:str="no_file",key:str="no_key"):
    name2 = name.strip().lower()
    key2 = key.strip()
    if name2 == "no_file" or key2 == "no_key" or name2 == "" or key2 =="" :
        # raise ValueError(f"file cannot be created , check if the file is named [note: do not name the file as no_file ] \n or the api key is passed to the function")
        return ("file cannot be created")
    else:
        path = f"./api_keys/{name2}.txt".strip()
        try:
            file = open(path,"r")
            file.close()
            return "file already exist, cannot be created again"
        except:
            file = open(path,"w")
            file.write(key2)
            file.close()
            return f"file {name2} created , and api key saved"






