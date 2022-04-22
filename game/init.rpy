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
        u1 = User("Star Lord").create()
        u2 = User("Iron Man").create()
        u3 = User("Moon Knight").create()

        c1 = Conversation().create()
        c2 = Conversation("Dynamic Duo").create()
        c3 = Conversation("Why so serious?").create()

        c1.add_members(u1, u2, u3)
        c2.add_members(u1, u2)
        c3.add_members(u1, u3)

    "Hello World!!!"
    "Hello World!!"
    "Hello World!"
    "Hello World"
    return