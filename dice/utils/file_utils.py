from os import makedirs
from os.path import exists, dirname

# see here: https://stackoverflow.com/questions/12517451/automatically-creating-directories-with-file-output

def openFile(filepath):
    makeDirectoryIfNeeded(filepath) 
    with open(filepath, "r") as f:
        return f.read()

def writeToFile(filepath, content):
    makeDirectoryIfNeeded(filepath)
    with open(filepath, "w") as f:
        f.write(content)
        
def makeDirectoryIfNeeded(filepath):
    if not exists(dirname(filepath)):
        makedirs(dirname(filepath))
