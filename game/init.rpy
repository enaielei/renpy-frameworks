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
    from store.messenger import User, Conversation, Membership

label start:
    python:
        User("Name 1")
        User("Name 2")
        User("Name 3")

        Conversation("Name 1")
        Conversation("Name 2")
        Conversation("Name 3")

        Membership(Conversation.get_first(), User.get_first())
        Membership(Conversation.get_first(), User.get()[1])
        Membership(Conversation.get_first(), User.get()[2])

    "Hello World!!!"
    "Hello World!!"
    "Hello World!"
    "Hello World"
    return