import disnake
from disnake.ext import commands

from configs import config
from utils import main_booleans as mainbool
from spw_api import spwapi

cogs = [
    "start",
    "vote",
    "clear",
    "join",
    "leave",
    "server"
]
cog = "cogs._"

bot = commands.Bot(
    command_prefix="!",
    intents=disnake.Intents.all(),
    activity=disnake.Game(config.getAttr("bot-status"), status=disnake.Status.online)
)
bot.remove_command('help')


def main():
    config.createIfNotExist()
    for extension in cogs:
        try:
            bot.load_extension(cog+extension)
        except Exception as e:
            print(e)

    try:
        bot.run(config.getAttr("token"))
    except disnake.errors.LoginFailure:
        print("Improper token has been passed.")
        print(f"[{config.getAttr('bot-prefix')}] Not started!")


@bot.command()
async def load(ctx, extension: str):
    if mainbool.isAuthor(ctx) and mainbool.isMain(__name__):
        try:
            bot.load_extension(cog+extension)
            await ctx.send(f'Функция {extension} успешно загружена!')
        except disnake.ext.commands.errors.ExtensionAlreadyLoaded:
            await ctx.send(f"Функция {extension} уже загружена")
        except disnake.ext.commands.errors.ExtensionNotFound:
            await ctx.send(f"Функция {extension} не найдена!")
        except Exception as e:
            await ctx.author.send(e)


@bot.command()
async def unload(ctx, extension: str):
    if mainbool.isAuthor(ctx) and mainbool.isMain(__name__):
        try:
            bot.unload_extension(cog+extension)
            await ctx.send(f'Функция {extension} успешно выгружена!')
        except disnake.ext.commands.errors.ExtensionNotLoaded:
            await ctx.send(f"Функция {extension} уже выгружена")
        except disnake.ext.commands.errors.ExtensionNotFound:
            await ctx.send(f"Функция {extension} не найдена!")
        except Exception as e:
            await ctx.author.send(e)


@bot.command()
async def reload(ctx, extension: str):
    if mainbool.isAuthor(ctx) and mainbool.isMain(__name__):
        try:
            bot.reload_extension(cog+extension)
            await ctx.send(f'Функция {extension} успешно перезагружена!')
        except disnake.ext.commands.errors.ExtensionNotLoaded:
            await ctx.send(f"Функция {extension} не загружена!")
        except disnake.ext.commands.errors.ExtensionNotFound:
            await ctx.send(f"Функция {extension} не найдена!")
        except Exception as e:
            await ctx.author.send(e)


@bot.command()
async def updateMember(ctx):
    if mainbool.isAuthor(ctx) and mainbool.isMain(__name__):
        members = bot.get_guild(config.getAttr("guild-id")).members
        for member in members:
            if not member.bot:
                user = spwapi.getUser(str(member.id))
                if user:
                    try:
                        await member.edit(nick=user.nickname)
                    except disnake.errors.Forbidden:
                        pass
        await ctx.send("Имена пользователей были изменены!")

if mainbool.isMain(__name__):
    main()
