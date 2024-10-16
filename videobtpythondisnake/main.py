import disnake
from disnake.ext import commands

import os


bot = commands.InteractionBot(test_guilds=[1245378350504087632], sync_commands_debug=True, reload=True)

@bot.event
async def on_ready():
    print("I am ready")

#@bot.slash_command(name="help")
#async def help(intentation:disnake.CommandInteraction):
#    await intentation.send("help")


for file in os.listdir("./cogs"):
    if file.endswith(".py"):
        bot.load_extension(f"cogs.{file[:-3]}")


bot.run("TOKEN_of_you__discord_bot")
