from dice.utils.command_utils import validatePrivateContext

welcome = """Welcome to dice-boy!
You can learn about the following features using the "/help <feature>" command.
/help rolls
/help profiles
/help votes
"""

rollHelp = """My primary purpose is to roll dice! You can do that really easily by typing /roll followed by a dice command.
Dice commands follow the same syntax you see in various tabletop RPG rules. A number, followed by a d (or D), followed by another number.

E.g.
1d4
2d6
1d20

/roll 1d4
/roll 2d6
/roll 1d20

The first number represents the number of dice to roll. The second number represents the number of sides on the dice.

Additionally, you can add a constant value to the roll that will be added regardless of the dices' outcomes.

E.g.
1d8-1
2d10+5
1d20+1

You can also combine various sets of constants and rolls.

E.g.
1d20 + 5 + 2d6 - 3
4d6 + 4d6 + 4d6

Finally, you can also save dice rolls for use later. Use the "/add roll" command followed by the name of the roll and the dice of the roll.

E.g.
/add roll perception 1d20+3
/add roll rage_damage 1d12 + 5 + 2

You can then use those rolls using the "/roll" command and the name instead of the dice command.

E.g.
/roll perception
/roll rage_damage

You can also list all of the rolls available using the "/list rolls" command.

Note that you can only use the "/add roll" and "/list rolls" commands in a private channel with dice-boy (like a DM).

These rolls are saved to your active profile. To learn more about profiles, use the "/help profiles" command."""

profileHelp = """A profile represents a set of data (like rolls) grouped for a specific purpose (like a specific campaign, character, or rule system).
When you save a roll, it is saved to your active profile. Each user of dice-boy starts with a "default" profile.
You can see a list of profiles available using the "/list profiles" command. The active profile is signified by a "*".

To create a new profile (perhaps for a new campaign, character, or familiar), use the "/add profile" command followed by the name of your profile.

E.g.
/add profile familiar
/add profile my new campaign

Then, to make the new profile the active profile, you can use the "/set profile" command followed by the name of the profile.

E.g.
/set profile familiar
/set profile my new campaign
/set profile default

You can list all of your profiles using the "/list profiles" command.

Additionally, you can choose which profile is your active profile when dice-boy starts up using the "/set default" command followed by the name of the profile.

E.g.
/set default familiar
/set default my new campaign
/set default default

Note that doing this will not change your active profile.

Profile commands are only available in a private channel with dice-boy (like a DM)"""

#TODO number the votes so that you can choose the vote with a number like you can with an option. Also get rid of "for"

voteHelp = """If you find your party to be at an impass, you can use dice-boy to start a vote to help you come to a decision using various forms of the "/vote" command.
To start a new vote, use the "/vote make" command, followed by a list of options you'd like people to vote on.

Note that it is important to use quotation marks (") around the title and options to help dice-boy distinguish between them.

E.g.
/vote make "Should we fight the lich?" "Yes" "No" "Idc"
/vote make "How much money are we willing to spend on magic items?" "None" "100GP" "Let's go all in."

If you think of an option you want to add after the fact, you can use the "/vote add" command followed by all of the options you want to add. Additionally, you should specify the name of the vote after listing the options using "to "<vote>""

E.g.
/vote add "20GP" "Whatever is in my wallet" "Let's just steal it all" to "How much money are we willing to spend on magic items?"

When it comes time to actually vote, use the plain "/vote" command followed by your choice followed by the name of the vote.

E.g.
/vote "Idc" "Should we fight the lich?"
/vote "Let's just steal it all" "How much money are we willing to spend on magic items?"

Additionally, dice-boy will display numbers next to each option. You can use these to make your selections instead. You can also vote multiple times, but your previous vote will be removed if you do.

To end a vote, use the "/vote close" command followed by the name of the vote.

E.g.
/vote close "Should we fight the lich?"

Note that in order to make the vote easily readable, all "/vote" commands are deleted after they are processed (unless the vote takes place in a private channel).

ADDITIONALLY (and this is important to read), in all of these cases it is possible to leave off the name of the vote.
HOWEVER doing so will cause dice-boy to issue your command to the most recent open vote. So if you are going to not specify the vote, make sure you know which vote in which you're participating!

E.g.
/vote "20GP" # works fine since "How much money are we willing to spend on magic items?" is the most recent vote.
/vote make "A sample vote" "Yea" "Nay"
/vote "None" # no longer works since "A sample vote" is the most recent vote.
/vote "Nay"  # works fine"""

async def helpCommand(ctx, subject):
    try:
        validatePrivateContext(ctx)
    except:
        await ctx.send("Sorry, try that again in a DM to me!")
        return
    if subject is None:
        await sendText(ctx, welcome) 
    elif "roll" in subject.lower():
        await sendText(ctx, rollHelp) 
    elif "profile" in subject.lower():
        await sendText(ctx, profileHelp) 
    elif "vote" in subject.lower():
        await sendText(ctx, voteHelp) 

# TODO constants file?
maxMessageLength = 2000

# TODO investigate coroutines and yield return
async def sendText(ctx, text):
   start = 0
   while text[start:start + maxMessageLength]:
       await ctx.send(text[start:start + maxMessageLength])
       start += maxMessageLength
