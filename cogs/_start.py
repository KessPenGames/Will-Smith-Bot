from disnake.ext import commands
from configs import config


class StartsCog(commands.Cog):
    def __init__(self, bot=commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"[{config.getAttr('bot-prefix')}] Started up!")


def setup(bot=commands.Bot):
    bot.add_cog(StartsCog(bot))
    print(f"Cog {__name__} is loading!")
