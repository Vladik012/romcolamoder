from disnake.ext import commands
import disnake

class Ban(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    


    @commands.slash_command(name="ban", description="Забанити гравця")
    async def ban(self, interaction, user: disnake.User, *, reason = None):
        await interaction.guild.ban(user, reason = reason)
        await interaction.response.send_message(f"Banned {user.mention}", ephemeral = True)
    
    @commands.slash_command(name="unban", description="Розбанити гравця")
    async def unban(self, interaction, user: disnake.User):
        await interaction.guild.unban(user)
        await interaction.response.send_message(f"Uanned {user.mention}", ephemeral = True)
    




def setup(bot):
    bot.add_cog(Ban(bot))