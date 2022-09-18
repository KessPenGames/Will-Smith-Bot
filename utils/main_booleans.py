from configs import config


def isMain(var):
    return var == "__main__"


def isAuthor(ctx):
    return ctx.author.id == config.getAttr("admin-id")
