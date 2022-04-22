init python hide:
    store._modules = []
    try:
        with renpy.file("modules.json") as file:
            import json
            store._modules = json.load(file)
    except:
        pass
    
    for module in _modules:
        renpy.load_module("scripts/{}/init".format(module))

init python:
    from store.messenger import User, Conversation, Membership, Message

label start:
    python:
        User("Name 1").create()
        User("Name 2").create()
        User("Name 3").create()

        Conversation("Name 1").create()
        Conversation("Name 2").create()
        Conversation("Name 3").create()

        Membership(Conversation.get_first(), User.get_first()).create()
        Membership(Conversation.get_first(), User.get()[1]).create()
        Membership(Conversation.get_first(), User.get()[2]).create()

    "Hello World!!!"
    "Hello World!!"
    "Hello World!"
    "Hello World"
    return