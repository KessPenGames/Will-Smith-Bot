import pyspw
from configs import config

spApi = pyspw.SpApi(config.getAttr("spw-card-id"), config.getAttr("spw-card-token"))


def getUser(discord_id: str):
    try:
        if spApi.check_access(discord_id):
            return spApi.get_user(discord_id)
    except Exception as e:
        print(e)
    return None
