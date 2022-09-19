from mctools import RCONClient
from configs import config

rcon = RCONClient(config.getAttr("rcon-connection"), port=config.getAttr("rcon-port"))


async def addToWl(nickname: str):
    if rcon.login(config.getAttr("rcon-password")):
        rcon.command("whitelist add " + nickname)
        rcon.stop()


async def removeFromWl(nickname: str):
    if rcon.login(config.getAttr("rcon-password")):
        rcon.command("whitelist remove " + nickname)
        rcon.stop()
