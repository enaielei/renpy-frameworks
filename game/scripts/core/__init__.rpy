init python hide in core:
    modules = [
        "scripts/core/gui",
        "scripts/core/config",
        "scripts/core/build",
    ]

    for module in modules:
        renpy.load_module(module)