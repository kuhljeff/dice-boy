from discord.abc import PrivateChannel

def validatePrivateContext(ctx):
    if not isinstance(ctx.message.channel, PrivateChannel):
        raise ValueError("That doesn't work here...")

def getObjAndArgs(command):
    try:
        return command.split(None, 1)
    except:
        raise ValueError("I can't understand " + command)
