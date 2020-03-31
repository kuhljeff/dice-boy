from json import loads

# TODO fill out this class to have a command interface

class EnvManager:

    def __init__(self, filepath):
        self.filepath = filepath
        f = open(filepath, "r")
        self.json = loads(f.read())
        f.close()
        self.currentEnv = next(e for e in self.json["environments"] if e["campaign"] == self.json["default"])

    def getSystem(self):
        return self.currentEnv["system"]

    def getCampaign(self):
        return self.currentEnv["campaign"]

    def getToken(self):
        return self.json["token"]

    def setEnvironment(self, envId):
        self.currentEnv = next(e for e in self.json["environments"] if e["campaign"] == envId.lower())

envManager = EnvManager("data/environments.json")

