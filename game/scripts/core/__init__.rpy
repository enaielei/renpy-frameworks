init python hide in core:
    modules = [
        "scripts/core/gui",
        "scripts/core/config",
        "scripts/core/build",
    ]

    for module in modules:
        renpy.load_module(module)

init python:
    person = utils.Person("Amolat", "Nommel Isanar", "Lavapie").create()
    phone = utils.phone.Phone().create()
    messenger = utils.phone.messenger.Messenger().create()

    user = utils.phone.messenger.User("Nommel", person).create()
    user1 = utils.phone.messenger.User("Mike").create()
    user2 = utils.phone.messenger.User("John").create()
    user3 = utils.phone.messenger.User("Mikaela").create()

    convo = utils.phone.messenger.Convo("Test", user, user1, user2, user3).create()