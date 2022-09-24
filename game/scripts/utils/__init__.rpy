init -1 python hide in utils:
    modules = [
        "scripts/utils/helper",
        "scripts/utils/base",
        "scripts/utils/definer",
        "scripts/utils/record",
        "scripts/utils/tracker",
        "scripts/utils/hint",
        "scripts/utils/episode",
        "scripts/utils/persona",
    ]

    for module in modules:
        renpy.load_module(module)