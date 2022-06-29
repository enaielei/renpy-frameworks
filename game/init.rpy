init python hide:
    store._modules = ()
    try:
        with renpy.file("modules.json") as file:
            import json
            store._modules = tuple(json.load(file))
    except:
        pass
    
    for module in _modules:
        renpy.load_module("scripts/{}/init".format(module))

label start:
    "Hello World!!!"
    return