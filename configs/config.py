import yaml
import os
import codecs

DUMP_STR = """
token: 'TOKEN'
bot-prefix: 'Will Smith'
bot-status: 'Oscar Reward'
admin-id: 866553002172743701
vote-channel-id: 1001086885713682503
"""


def createIfNotExist():
    if not os.path.exists("./configs/config.yml"):
        with codecs.open('./configs/config.yml', 'w', 'utf-8') as file:
            config_dump = yaml.safe_load(DUMP_STR)
            yaml.dump(config_dump, file)


def getAttr(var: str):
    if os.path.exists("./configs/config.yml"):
        with codecs.open('./configs/config.yml', 'r', 'utf-8') as file:
            return yaml.safe_load(file)[var]
    return None
