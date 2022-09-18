from disnake.ext import commands
from utils import main_booleans as mainbool


class ClearCog(commands.Cog):
    def __init__(self, bot=commands.Bot):
        self.bot = bot

    @commands.slash_command(name="clear", description="Очистить чат")
    async def help_command(self, ctx, count: int = 100):
        if mainbool.isAuthor(ctx):
            await ctx.channel.purge(limit=count)
            await ctx.response.send_message("Сообщения были успешно удалены!", ephemeral=True)


def setup(bot=commands.Bot):
    bot.add_cog(ClearCog(bot))
    print(f"Cog {__name__} is loading!")
