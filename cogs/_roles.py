from disnake.ext import commands

from views.buttons import GuestRoleButtons, ClownRoleButtons


class RolesCog(commands.Cog):
    def __init__(self, bot=commands.Bot):
        self.bot = bot

    @commands.command()
    async def sendGuestRoles(self, ctx: commands.Context):
        await ctx.send("Создано!", view=GuestRoleButtons())
        await ctx.send("Создано!", view=ClownRoleButtons())


def setup(bot=commands.Bot):
    bot.add_cog(RolesCog(bot))
    print(f"Cog {__name__} is loading!")
