from fastapi import FastAPI, Form
from fastapi.responses import PlainTextResponse
from parser import parse_message
from db import create_table, update_stock, get_stock


app = FastAPI()

create_table()

@app.get("/")
def home():
    return {"message": "Server working ✅"}


@app.post("/webhook")
async def webhook(
    Body: str = Form(...),
    From: str = Form(...)
):
    message = Body.lower()

    # 🔥 QUERY DETECTION
    if "kitna" in message:
        words = message.split()
        item = words[0]

        qty, unit = get_stock(item)

        if qty is not None:
            reply = f"📦 {item}: {qty} {unit}"

            # 🔥 ADD THIS PART HERE
            if qty < 5:
                reply += "\n⚠️ Low stock! Order soon"

        else:
             reply = f"❌ {item} not found"

        return PlainTextResponse(reply)

    # 🔥 UPDATE FLOW
    parsed = parse_message(message)

    item = parsed["item"]
    quantity = parsed["quantity"]
    unit = parsed["unit"]
    action = parsed["action"]

    new_qty = update_stock(item, quantity, unit, action)

    reply = f"✅ {item}: now {new_qty} {unit}"

    return PlainTextResponse(reply)