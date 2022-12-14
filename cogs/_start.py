from disnake.ext import commands

from configs import config
from views.buttons import GuestRoleButtons, ClownRoleButtons


class StartsCog(commands.Cog):
    def __init__(self, bot=commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        if not self.bot.persistent_views:
            self.bot.add_view(view=GuestRoleButtons())
            self.bot.add_view(view=ClownRoleButtons())
            self.bot.persistent_views_added = True
        print(f"[{config.getAttr('bot-prefix')}] Started up!")


def setup(bot=commands.Bot):
    bot.add_cog(StartsCog(bot))
    print(f"Cog {__name__} is loading!")
