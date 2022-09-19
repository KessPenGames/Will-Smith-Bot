import disnake
from disnake.ext import commands
from configs import config
from spw_api import spwapi


class JoinCog(commands.Cog):
    def __init__(self, bot=commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member: disnake.Member):
        if member.guild.id == config.getAttr("guild-id"):
            user = spwapi.getUser(str(member.id))
            if not member.bot:
                if user:
                    await member.edit(nick=user.nickname)
                    join_channel_id = config.getAttr("join-channel-id")
                    embed = disnake.Embed(
                        title="Новый участник",
                        description=f"Пользователь **{user.nickname}** зашёл на этот проклятый сервер!",
                        color=16761344
                    )
                    embed.set_thumbnail(url=user.get_skin().get_front())
                    await member.guild.get_channel(join_channel_id).send(embed=embed)
                else:
                    await member.send("У вас нет проходки на PoopLand!")
                    await member.kick(reason="Нет проходки на PL")


def setup(bot=commands.Bot):
    bot.add_cog(JoinCog(bot))
    print(f"Cog {__name__} is loading!")
