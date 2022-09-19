import disnake
from disnake.ext import commands
from configs import config
from spw_api import spwapi


class LeaveCog(commands.Cog):
    def __init__(self, bot=commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_remove(self, member: disnake.Member):
        if member.guild.id == config.getAttr("guild-id"):
            user = spwapi.getUser(str(member.id))
            if not member.bot:
                if user:
                    join_channel_id = config.getAttr("join-channel-id")
                    embed = disnake.Embed(
                        title="Бывший участник",
                        description=f"Пользователь **{user.nickname}** сбежал с этого проклятого сервер!",
                        color=16726329
                    )
                    embed.set_thumbnail(url=user.get_skin().get_front())
                    await member.guild.get_channel(join_channel_id).send(embed=embed)


def setup(bot=commands.Bot):
    bot.add_cog(LeaveCog(bot))
    print(f"Cog {__name__} is loading!")
