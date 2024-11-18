import keyring
import json

def Set(list1,list2):
    ls = {}
    for name in list1:
        for value in list2:
            ls[name] = value
    keyring.set_password("PCL2OSSMPSetup",json.dumps(ls))

def Get(name):
    data = keyring.get_password("PCL2OSSMPSetup")
    setup = json.loads(data)
    return setup[name]

def Clean():
    keyring.delete_password("PCL2OSSMPSetup")

def Remove(name):
    data = keyring.get_password("PCL2OSSMPSetup")
    setup = json.loads(data)
    setup[name] = ""
    keyring.set_password("PCL2OSSMPSetup",json.dumps(setup))