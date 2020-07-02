currentCall = None
currentCallMessage = None

async def callCommand(ctx, rollName):
    if callIsActive():
        ctx.send("Cannot start a roll call when a roll call is active!")
    else:
        currentCall = rollName

async def callRoll(ctx, roll):
    if not callIsActive():
        ctx.send("No call is active right now!")
    else:
        await ctx.message.delete()
        original

def callIsActive():
    return currentCall != None and currentCallMessage != None


