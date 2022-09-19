import disnake
from disnake.ext import commands

from configs import config
from spw_api import spwapi
from rcon import rcon


class ServerCog(commands.Cog):
    def __init__(self, bot=commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload: disnake.RawReactionActionEvent):
        if payload.guild_id == config.getAttr("guild-id"):
            if payload.member is not None:
                if payload.message_id == config.getAttr("reaction-message-id"):
                    user = spwapi.getUser(str(payload.member.id))
                    if not payload.member.bot:
                        if user:
                            await rcon.addToWl(user.nickname)
                            await payload.member.send("Вы были добавлены на **Клоунский тест**!")

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload: disnake.RawReactionActionEvent):
        guild_id = config.getAttr("guild-id")
        if payload.guild_id == guild_id:
            if payload.message_id == config.getAttr("reaction-message-id"):
                member = self.bot.get_guild(guild_id).get_member(payload.user_id)
                user = spwapi.getUser(str(member.id))
                if not member.bot:
                    if user:
                        await rcon.removeFromWl(user.nickname)
                        await member.send("Вы были удалены с **Клоунского теста**!")


def setup(bot=commands.Bot):
    bot.add_cog(ServerCog(bot))
    print(f"Cog {__name__} is loading!")
