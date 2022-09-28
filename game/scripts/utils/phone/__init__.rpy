init -1 python hide in utils.phone:
    import store

    modules = [
        "scripts/utils/phone/phone",
        "scripts/utils/phone/app",
        "scripts/utils/phone/controller",
        "scripts/utils/phone/installation",
        "scripts/utils/phone/system",
    ]

    for module in modules:
        renpy.load_module(module)

init -1 python in utils.phone:
    def initialize(
        Phone=Phone,
        Installation=Installation,
    ):
        Phone.has_many(Installation)
        
        Installation.has_one(Phone)
        Installation.has_one(App)

    initialize()