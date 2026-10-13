"""Standalone script to send a real error to Sentry."""
import sentry_sdk

sentry_sdk.init(
    dsn="https://5077e9c70b37560cfff5b3e4a875cd2c@o4512248127029248.ingest.us.sentry.io/4512248147542016",
    traces_sample_rate=1.0,
    release="abc123def456abc123def456abc123def456abcd",
)

def process_order(payload):
    user_id = payload["user_id"]
    items = payload["items"]
    total = payload["total"]
    return {"user_id": user_id, "items": items, "total": total}

if __name__ == "__main__":
    try:
        process_order({"user_id": "u1", "items": []})
    except Exception:
        sentry_sdk.capture_exception()
        raise
