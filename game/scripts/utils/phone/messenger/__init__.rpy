init -1 python hide in utils.phone.messenger:
    import store

    modules = [
        "scripts/utils/phone/messenger/messenger",
        "scripts/utils/phone/messenger/user",
        "scripts/utils/phone/messenger/convo",
        "scripts/utils/phone/messenger/membership",
        "scripts/utils/phone/messenger/message",
        "scripts/utils/phone/messenger/typing",
    ]

    for module in modules:
        renpy.load_module(module)

    renpy.load_module("scripts/utils/person")

    User.has_one(store.utils.Person)
    User.has_many(Convo)
    User.has_many(Membership)

    Convo.has_one(User)
    Convo.has_many(Membership)

    Membership.has_one(Convo)
    Membership.has_one(User)
    Membership.has_many(Message)

    Message.has_one(Membership)

    Typing.has_one(Membership)