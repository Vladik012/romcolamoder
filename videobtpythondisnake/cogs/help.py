from disnake.ext import commands

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    


    @commands.slash_command(name="help", description="Лист команд")
    async def help(self, intentation):
        await intentation.send("help")




def setup(bot):
    bot.add_cog(Help(bot))