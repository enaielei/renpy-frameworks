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
    from datetime import datetime
    from store.messenger import User, Conversation, Membership, Message

label start:
    python:
        u1 = User("Star Lord").create()
        u2 = User("Iron Man").create()
        u3 = User("Moon Knight").create()

        c1 = Conversation().create()
        c2 = Conversation("Dynamic Duo").create()
        c3 = Conversation("Why so serious?").create()

        c1.add_member(u1, u2, u3)
        c2.add_member(u1, u2)
        c3.add_member(u1, u3)

        u1.add_message(c1, "Hello World", datetime(2022, 4, 21, 13, 20))
        u2.add_message(c1, "Shut up Faggot!", datetime(2022, 4, 21, 13, 21))
        u3.add_message(c1, "Whoah, chill dude!", datetime(2022, 4, 21, 13, 22))

        u1.add_message(c1, "Hello World", datetime(2022, 4, 21, 13, 23))
        u2.add_message(c1, "Shut up Faggot!", datetime(2022, 4, 21, 13, 24))
        u3.add_message(c1, "Whoah, chill dude!", datetime(2022, 4, 21, 13, 25))
        u2.add_message(c1, "Shut up Faggot!", datetime(2022, 4, 21, 13, 26))
        u1.add_message(c1, "Hello World", datetime(2022, 4, 21, 13, 27))
        u3.add_message(c1, "Whoah, chill dude!", datetime(2022, 4, 21, 13, 28))

    call screen messenger(u1)
    "Hello World!!!"
    "Hello World!!"
    "Hello World!"
    "Hello World"
    return

screen messenger(user):
    default membership = None 

    frame:
        background "#555555"
        xysize (0.25, 0.75)
        align (0.5, 0.5)

        if membership is None:
            viewport:
                vbox:
                    spacing 20

                    for mem in user.memberships():
                        button:
                            action SetScreenVariable("membership", mem)

                            vbox:
                                text mem.conversation.name:
                                    hover_color "#0f0"
        else:
            vbox:
                xfill True
                spacing 20

                textbutton membership.conversation.name:
                    text_hover_color "#0f0"
                    action SetScreenVariable("membership", None)
                viewport:
                    xfill True
                    mousewheel True

                    vbox:
                        xfill True
                        spacing 20

                        for mes in membership.conversation.messages(_sort="datetime"):
                            text "{size=-5}[mes.sender.name]{/size}\n[mes.content]":
                                xalign (0.0 if mes.sender != user else 1.0)

