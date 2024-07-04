from disnake.ext import commands

class Clear(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    
    @commands.slash_command(name="clear", description="Видалити повiдомлення")
    async def clear(self, intentation, amount: int):
        await intentation.channel.purge(limit=amount)
        await intentation.send(f"Було видалено `{amount}` повiдомлень ", ephemeral = True)



def setup(bot):
    bot.add_cog(Clear(bot))