import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from app.handlers.orders import process_order


def test_process_order_happy_path():
    result = process_order({
        "user_id": "u1",
        "items": [{"sku": "a", "qty": 1}],
        "total": 9.99,
    })
    assert result["total"] == 9.99


def test_process_order_empty_cart_missing_total():
    """Reproduces the production bug. Fails on main, passes after the fix."""
    result = process_order({
        "user_id": "u1",
        "items": [],
    })
    assert result["total"] == 0
