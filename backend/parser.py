def parse_message(text):
    text = text.lower()

    words = text.split()

    quantity = None
    unit = None
    item = None
    action = None

    # 🔹 find quantity
    for word in words:
        if word.isdigit():
            quantity = int(word)

    # 🔹 units
    units = ["kg", "packet", "litre", "dozen"]

    for word in words:
        if word in units:
            unit = word

    # 🔹 action detection
    if "aaya" in text:
        action = "add"
    elif "gaya" in text or "becha" in text:
        action = "remove"

    # 🔹 item detection (simple logic)
    for word in words:
        if word not in units and not word.isdigit() and word not in ["aaya", "gaya", "becha"]:
            item = word

    return {
        "item": item,
        "quantity": quantity,
        "unit": unit,
        "action": action
    }