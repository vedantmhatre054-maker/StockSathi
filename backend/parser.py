def parse_message(text):
    text = text.lower()
    words = text.split()

    quantity = None
    unit = None
    item = None
    action = None

    # 🔹 Quantity
    for word in words:
        if word.isdigit():
            quantity = int(word)

    # 🔹 Units (multi-language)
    units_map = {
        "kg": "kg",
        "kilo": "kg",
        "kilos": "kg",
        "killo": "kg",
        "packet": "packet",
        "pack": "packet",
        "pkt": "packet",
        "litre": "litre",
        "liter": "litre"
    }

    for word in words:
        if word in units_map:
            unit = units_map[word]

    # 🔥 ACTION (HINDI + MARATHI + ROMAN 🔥)
    add_words = [
        "aaya", "aya", "added",
        "aala", "aali", "aale",   # Marathi
        "aayi", "aaye"            # Hindi variants
    ]

    remove_words = [
        "gaya", "geli", "gele",   # Marathi
        "becha", "sold",
        "gayi", "gaye"
    ]

    # 🔥 FIRST CHECK REMOVE (IMPORTANT)
    for word in words:
        if word in remove_words:
            action = "remove"
            break

    # 🔥 THEN CHECK ADD
    if not action:
        for word in words:
            if word in add_words:
                action = "add"
                break

    # 🔥 ITEM MAP (MULTI-LANGUAGE)
    item_map = {
        # Tomato
        "tomato": "tamatar",
        "tamatar": "tamatar",
        "tomatoo": "tamatar",
        "batata": "aloo",
        "टोमॅटो": "tamatar",
        "टमाटर": "tamatar",

        # Potato
        "potato": "aloo",
        "aloo": "aloo",
        "batata": "aloo",
        "आलू": "aloo",

        # Maggi
        "maggi": "maggi",

        # Milk
        "milk": "milk",
        "doodh": "milk",
    }

    for word in words:
        if word in item_map:
            item = item_map[word]

    return {
        "item": item,
        "quantity": quantity,
        "unit": unit,
        "action": action
    }