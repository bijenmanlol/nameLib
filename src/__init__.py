import json, random

data = open(f"namelib/data.json", "r")
dataF = json.load(data)

def randomName(mode: str, numbermode: bool):
    if mode.lower() == "usernames":
        if numbermode == True:
            name = dataF["usernames"][random.randint(0, len("usernames") - 1)], dataF["usernames"][random.randint(0, len("usernames") - 1)], str(random.randint(1, 1000))
            return "".join(name)  
        else:
            name = dataF["usernames"][random.randint(0, len("usernames") - 1)], dataF["usernames"][random.randint(0, len("usernames") - 1)]
            return "".join(name)  
    elif mode.lower() == "normalnames":
        if numbermode == True:
            name = dataF["normalnames"][random.randint(0, len("normalnames") - 1)], str(random.randint(1, 1000))
            return "".join(name)        
        else:
            name = dataF["normalnames"][random.randint(0, len("normalnames") - 1)]
            return "".join(name)    
    else:
        print(f"|NAMELIB ERROR| mode at randomName() - {mode} is not a possible option, choose from: 'usernames' or 'normalnames'")
