from dice.logic.parser import parse
from dice.commands.profile_commands import getRoll
from random import randrange

def randomCritSuccessString():
    praises = [
        "Wow, {.author.display_name}, great job! You rolled a nat 20!",
        "Crit success, {.author.display_name}!",
        "You must be very skilled, {.author.display_name}, because that's a nat 20!",
        "Are those dice weighted, {.author.display_name}? Because that's another nat 20...",
        "{.author.display_name} is getting lucky tonight! That's a nat 20!"
    ]
    return praises[randrange(0, len(praises))]

def randomCritFailString():
    mockeries = [
        "Yikes, {.author.display_name}. Nat 1.",
        "Crit fail. Sucks to suck, {.author.display_name}?",
        "Get good, {.author.display_name}. That's a C R I T I C A L F A I L U R E.",
        "I hope someone brought a scroll of resurrection for {.author.display_name}, because that's a natural 1...",
        "Better luck next time, {.author.display_name}! Nat 1!",
        "You roll a natural 1 and accidentally shoot you Austen. Roll for damage, {.author.display_name}!"
    ]
    return mockeries[randrange(0, len(mockeries))]

def mapNameToRoll(ctx, rollString):
    try:
        return getRoll(ctx, rollString)
    except Exception as err:
        return rollString

def parseRollString(ctx, rollString):
    try:
        total, rolls = parse(rollString, lambda r : mapNameToRoll(ctx, r))
    except:
        return "Sorry, that is not a valid roll!"
    firstRoll = rolls.pop(0)
    result = str(total) + " (" + str(firstRoll)
    for roll in rolls:
        if roll < 0:
            result += " - " + str(roll * -1)
        else:
            result += " + " + str(roll)
    result += ")"
#    if "1d20" in rollString:
#        if firstRoll == 20:
#            return randomCritSuccessString().format(ctx.message) + " " + result
#        elif firstRoll == 1:
#            return randomCritFailString().format(ctx.message) + " " + result
    return "{.author.display_name} => ".format(ctx.message) + result

