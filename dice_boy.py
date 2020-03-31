from logging import basicConfig, INFO
from discord.ext import commands
from dice.logic.env import token
from dice.commands.roll_commands import parseRollString
from dice.commands.profile_commands import getRoll, setCommand, addCommand, listCommand, saveCommand

basicConfig(level=INFO)

bot = commands.Bot(command_prefix='/')

@bot.command()
async def roll(ctx, *, roll):
    try:
        rollString = getRoll(ctx, roll)
    except Exception as err:
        rollString = roll
    await ctx.send(parseRollString(ctx, rollString))

@bot.command()
async def set(ctx, *, args):
    try:
        await ctx.send(setCommand(ctx, args))
    except Exception as err:
        await ctx.send(str(err))

@bot.command()
async def add(ctx, *, args):
    try:
        await ctx.send(addCommand(ctx, args))
    except Exception as err:
        await ctx.send(str(err))

@bot.command()
async def list(ctx, *, args):
    await ctx.send(listCommand(ctx, args))

@bot.command()
async def save(ctx):
    saveCommand()

bot.run(token())
