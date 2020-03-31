import logging
import profile_commands

from discord.ext import commands
from roll_command import parseRollString
from dice_env import envManager

logging.basicConfig(level=logging.INFO)

bot = commands.Bot(command_prefix='/')

@bot.command()
async def roll(ctx, *, roll):
    try:
        rollString = profile_commands.getRoll(ctx, roll)
    except Exception as err:
        rollString = roll
    await ctx.send(parseRollString(ctx, rollString))

@bot.command()
async def set(ctx, *, args):
    try:
        await ctx.send(profile_commands.setCommand(ctx, args))
    except Exception as err:
        await ctx.send(str(err))

@bot.command()
async def add(ctx, *, args):
    try:
        await ctx.send(profile_commands.addCommand(ctx, args))
    except Exception as err:
        await ctx.send(str(err))

@bot.command()
async def save(ctx):
    profile_commands.saveCommand()

@bot.command()
async def list(ctx, *, args):
    await ctx.send(profile_commands.listCommand(ctx, args))

bot.run(envManager.getToken())
