from re import compile
from dice.logic.voting import addVote, addOptionToVote, voteForOption, determineVote, closeVote
from dice.utils.command_utils import getObjAndArgs

async def voteCommand(ctx, args):
    try:
        await ctx.message.delete()
    except:
        pass
    if len(args) == 0:
        await ctx.send("Cannot vote with no arguments")
        return
    if args[0] == "make":
        await handleMakeCommand(ctx, args[1:]) 
    elif args[0] == "add":
        await handleAddCommand(ctx, args[1:])
    elif args[0] == "close":
        await handleCloseCommand(ctx, args[1:])
    else:
        await handleVoteForCommand(ctx, args) 

async def handleMakeCommand(ctx, args):
    try:
        vote = addVote(args[0])
        for arg in args[1:]:
            addOptionToVote(vote.name, arg)
        voteString = writeVote(vote)
        vote.message = await ctx.send(voteString)
    except:
        await ctx.send("Cannot make vote.")

async def handleAddCommand(ctx, args):
    try:
        name = args[args.index("to") + 1]
    except:
        name = None
    try:
        vote = determineVote(name)
        if vote is not None:
            options = args[:-2] if name is not None else args
            for option in options:
                vote.addOption(option)
            voteString = writeVote(vote)
            await vote.message.edit(content = voteString)
        else:
            await ctx.send("Could not find vote.")
    except:
        await ctx.send("Cannot add options to vote.")

async def handleVoteForCommand(ctx, args):
    try:
        if args[0] == "for":
            name = args[2] if len(args) > 2 else None
            option = args[1] if len(args) > 1 else None
        else:
            name = args[1] if len(args) > 1 else None
            option = args[0]
        vote = voteForOption(name, option, ctx.message.author.name)
        voteString = writeVote(vote)
        await vote.message.edit(content = voteString)
    except:
        await ctx.send("Cannot vote for option.") 

async def handleCloseCommand(ctx, args):
    try:
        vote = closeVote(args[1])
    except:
        await ctx.send("Cannot close vote.")

def writeVote(vote):
    optionString = ""
    for index, (option, voters) in enumerate(vote.options, 1):
        optionString += str(index) + ") \"" + option + "\" (" + str(len(voters)) + ")\n"
    return "\"" + vote.name + "\"\n" + optionString

