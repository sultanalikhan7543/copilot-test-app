def process_order(payload):
    user_id = payload["user_id"]
    items = payload["items"]
    total = payload["total"]
    return {"user_id": user_id, "items": items, "total": total}
