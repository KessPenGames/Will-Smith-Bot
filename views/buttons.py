import disnake

style = disnake.ButtonStyle.green

CLOWN_ROLES = [785727770394230835, 766550155809652756]

ICLOWN_ROLE = 866537593927630878
ICLOWN_ROLE_EMOJI = "<a:evolving_clown:1004613637794713622>"
IGUEST_ROLE = 810465761050755092
IGUEST_ROLE_EMOJI = "<a:clownwaaaaaaa:1004594831160512602>"

BUILDER_ROLE = 0
BUILDER_ROLE_EMOJI = ""
SCHEMATIC_ROLE = 0
SCHEMATIC_ROLE_EMOJI = ""
RESURSER_ROLE = 0
RESURSER_ROLE_EMOJI = ""
REDSTONER_ROLE = 0
REDSTONER_ROLE_EMOJI = ""
SORTER_ROLE = 0
SORTER_ROLE_EMOJI = ""
SHOPER_ROLE = 0
SHOPER_ROLE_EMOJI = ""


class GuestRoleButtons(disnake.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @disnake.ui.button(
        emoji=IGUEST_ROLE_EMOJI, label="Я гость", style=style, custom_id="role:iguest"
    )
    async def iguest(self, button: disnake.ui.Button, inter: disnake.MessageInteraction):
        await updateGuestRoles(inter, IGUEST_ROLE)

    @disnake.ui.button(
        emoji=ICLOWN_ROLE_EMOJI, label="Я клоун (Хочу вступить в город)", style=style, custom_id="role:iclown"
    )
    async def iclown(self, button: disnake.ui.Button, inter: disnake.MessageInteraction):
        await updateGuestRoles(inter, ICLOWN_ROLE)


async def updateGuestRoles(inter, role_id):
    author = inter.guild.get_member(inter.user.id)
    if True in [item.id in CLOWN_ROLES for item in author.roles]:
        await inter.response.send_message("Вы не можете получить эти роли!", ephemeral=True)
        return
    role = inter.guild.get_role(role_id)
    if author.get_role(role_id):
        await author.remove_roles(role)
    else:
        await author.add_roles(role)
    await updateGuestMessage(inter)
    await inter.send("Вы успешно обновили роли!", ephemeral=True)


async def updateGuestMessage(inter):
    clownRole = inter.guild.get_role(ICLOWN_ROLE)
    guestRole = inter.guild.get_role(IGUEST_ROLE)
    await inter.response.edit_message(
        "ℹПолучение ролей для гостейℹ\n"
        "**Чтобы получить роль нажмите на кнопку**.\n"
        f"{IGUEST_ROLE_EMOJI} Гостей - {len(guestRole.members)}\n"
        f"{ICLOWN_ROLE_EMOJI} Клоунов? - {len(clownRole.members)}"
    )


class ClownRoleButtons(disnake.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @disnake.ui.button(
        emoji=BUILDER_ROLE_EMOJI, label="Архитектор", style=style, custom_id="role:builder"
    )
    async def builder(self, button: disnake.ui.Button, inter: disnake.MessageInteraction):
        await updateClownRoles(inter, BUILDER_ROLE)

    @disnake.ui.button(
        emoji=SCHEMATIC_ROLE_EMOJI, label="Перестройщик", style=style, custom_id="role:schematic"
    )
    async def schematic(self, button: disnake.ui.Button, inter: disnake.MessageInteraction):
        await updateClownRoles(inter, SCHEMATIC_ROLE)

    @disnake.ui.button(
        emoji=RESURSER_ROLE_EMOJI, label="Ресурсер", style=style, custom_id="role:schematic"
    )
    async def schematic(self, button: disnake.ui.Button, inter: disnake.MessageInteraction):
        await updateClownRoles(inter, RESURSER_ROLE)

    @disnake.ui.button(
        emoji=REDSTONER_ROLE_EMOJI, label="Механизмер", style=style, custom_id="role:redstoner"
    )
    async def redstoner(self, button: disnake.ui.Button, inter: disnake.MessageInteraction):
        await updateClownRoles(inter, REDSTONER_ROLE)

    @disnake.ui.button(
        emoji=SORTER_ROLE_EMOJI, label="Сортировщик склада", style=style, custom_id="role:sorter"
    )
    async def sorter(self, button: disnake.ui.Button, inter: disnake.MessageInteraction):
        await updateClownRoles(inter, SORTER_ROLE)

    @disnake.ui.button(
        emoji=SHOPER_ROLE_EMOJI, label="Продавец в т/ц", style=style, custom_id="role:shoper"
    )
    async def shoper(self, button: disnake.ui.Button, inter: disnake.MessageInteraction):
        await updateClownRoles(inter, SHOPER_ROLE)


async def updateClownRoles(inter, role_id):
    author = inter.guild.get_member(inter.user.id)
    if True in [item.id in CLOWN_ROLES for item in author.roles]:
        role = inter.guild.get_role(role_id)
        if author.get_role(role_id):
            await author.remove_roles(role)
        else:
            await author.add_roles(role)
        await updateClownMessage(inter)
        await inter.send("Вы успешно обновили роли!", ephemeral=True)
    else:
        await inter.response.send_message("Вы не можете получить эти роли!", ephemeral=True)
        return


async def updateClownMessage(inter):
    builderRole = inter.guild.get_role(BUILDER_ROLE)
    schematicRole = inter.guild.get_role(SCHEMATIC_ROLE)
    resurserRole = inter.guild.get_role(RESURSER_ROLE)
    redstonerRole = inter.guild.get_role(REDSTONER_ROLE)
    sorterRole = inter.guild.get_role(SORTER_ROLE)
    shoperRole = inter.guild.get_role(SHOPER_ROLE)
    await inter.response.edit_message(
        "ℹПолучение ролей для клоуновℹ\n"
        "**Чтобы получить роль нажмите на кнопку**.\n"
        f"{BUILDER_ROLE_EMOJI} Архитекторов - {len(builderRole.members)}\n"
        f"{SCHEMATIC_ROLE_EMOJI} Перестройщиков - {len(schematicRole.members)}\n"
        f"{RESURSER_ROLE_EMOJI} Ресурсеров - {len(resurserRole.members)}\n"
        f"{REDSTONER_ROLE_EMOJI} Механизмеров - {len(redstonerRole.members)}\n"
        f"{SORTER_ROLE_EMOJI} Сортировщиков склада - {len(sorterRole.members)}\n"
        f"{SHOPER_ROLE_EMOJI} Продавцов из т/ц - {len(shoperRole.members)}\n"
    )
