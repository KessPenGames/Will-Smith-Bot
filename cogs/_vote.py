import disnake
from disnake.ext import commands
from configs import config


class VoteCog(commands.Cog):
    def __init__(self, bot=commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message: disnake.Message):
        if not message.author.bot:
            if message.channel.id == config.getAttr('vote-channel-id'):
                await message.add_reaction(emoji="<:checkmark:1021036723427344424>")
                await message.add_reaction(emoji="<:cross:1021037188848304148>")
                await message.add_reaction(emoji="<:none:1021037781537017906>")
                await message.create_thread(name="Обсуждение", auto_archive_duration=10080)


def setup(bot=commands.Bot):
    bot.add_cog(VoteCog(bot))
    print(f"Cog {__name__} is loading!")
