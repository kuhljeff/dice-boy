from dice.utils.file_utility import openFile
from json import loads

# TODO fill out this class to have a command interface

filepath = "data/environments.json"
json = loads(openFile(filepath))
currentEnv = next(e for e in json["environments"] if e["campaign"] == json["default"])

def system():
    return currentEnv["system"]

def campaign():
     return currentEnv["campaign"]

def token():
    return json["token"]

def setEnvironment(envId):
    currentEnv = next(e for e in json["environments"] if e["campaign"] == envId.lower())

