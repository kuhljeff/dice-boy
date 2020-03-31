from dice_profiles import profileManager
from discord.abc import PrivateChannel

def setCommand(ctx, command):
    __validateContext(ctx)
    profileSet = __getProfileSet(ctx)
    obj, args = __getObjAndArgs(command)
    if obj == "profile":
        profileSet.setProfile(args)
        return args + " is now the active profile!"
    elif obj == "default":
        profileSet.setDefaultProfile(args)
        return args + " is now the default profile!"
    else:
        return "You cannot set " + obj

def addCommand(ctx, command):
    __validateContext(ctx)
    profileSet = __getProfileSet(ctx)    
    obj, args = __getObjAndArgs(command)
    if obj == "roll":
        name, dice = __getObjAndArgs(args)
        profileSet.addRoll(name, dice)
        return "Added " + name + " as " + dice 
    elif obj == "profile":
        profileSet.addProfile(args)
        return "Added a new profile named " + args
    else:
        return "You cannot add " + obj

def getRoll(ctx, rollString):
    profileSet = __getProfileSet(ctx)
    return profileSet.getRoll(rollString)["roll"]

def listCommand(ctx, command):
    __validateContext(ctx)
    profileSet = __getProfileSet(ctx)
    if command == "profile" or command == "profiles":
        profiles = profileSet.getAllProfiles()
        currentProfile = profileSet.getCurrentProfile()
        result = "\n".join(list(map(lambda p : mapProfileId(p, currentProfile), profiles)))
    elif command == "roll" or command == "rolls":
        rolls = profileSet.getAllRolls()
        result = "\n".join(list(map(lambda r : r["id"], rolls)))
    else:
        return "You cannot list " + command
    if result == "":
        return "No results found." 
    else:
        return result

def mapProfileId(profile, currentProfile):
    profileId = profile["id"]
    if profileId == currentProfile["id"]:
        profileId += " *"
    return profileId

def renameCommand(ctx, command):
    __validateContext(ctx)
    profileSet = __getProfileSet(ctx)

def deleteCommand(ctx, command):
    __validateContext(ctx)
    profileSet = __getProfileSet(ctx)

def saveCommand():
    profileManager.writeToJson()

def __validateContext(ctx):
    if not isinstance(ctx.message.channel, PrivateChannel):
        raise ValueError("That doesn't work here...")

def __getProfileSet(ctx):
    try:
        return profileManager.getProfileSet(ctx.message.author.name)
    except:
        profileManager.addProfileSet(ctx.message.author.name)
        return profileManager.getProfileSet(ctx.message.author.name)

def __getObjAndArgs(command):
    try:
        return command.split(None, 1)
    except:
        raise ValueError("I can't understand " + command)

