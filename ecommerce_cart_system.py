"""A small, validated shopping-cart example for static-analysis practice."""

import hashlib
import json
import secrets
from pathlib import Path

DEFAULT_CART = {
    "ITEM1": {"name": "Wireless Mouse", "price": 25.0, "qty": 2},
    "ITEM2": {"name": "Mechanical Keyboard", "price": 80.0, "qty": 1},
    "ITEM3": {"name": "USB-C Hub", "price": 45.0, "qty": 3},
}


def add_item_to_cart(
    cart: dict[str, dict[str, object]],
    item_id: str,
    name: str,
    price: float,
    quantity: int = 1,
) -> bool:
    """Add a new item after validating its identifier, price, and quantity."""
    if not item_id or not name.strip() or item_id in cart:
        return False
    if price < 0 or quantity <= 0:
        raise ValueError(
            "price must be non-negative and quantity must be positive"
        )
    cart[item_id] = {
        "name": name.strip(),
        "price": float(price),
        "qty": quantity,
    }
    return True


def remove_item_from_cart(
    cart: dict[str, dict[str, object]], item_id: str
) -> bool:
    """Remove an item and report whether it existed."""
    return cart.pop(item_id, None) is not None


def check_cart_status(
    cart: dict[str, dict[str, object]], item_id: str
) -> bool:
    """Return whether an item is present with a positive quantity."""
    item = cart.get(item_id)
    return item is not None and int(item["qty"]) > 0


def calculate_discounted_total(
    cart: dict[str, dict[str, object]], item_id: str, discount_rate: float
) -> float:
    """Return an item's discounted total for a rate between zero and one."""
    if not 0 <= discount_rate <= 1:
        raise ValueError("discount rate must be between 0 and 1")
    item = cart[item_id]
    subtotal = float(item["price"]) * int(item["qty"])
    return round(subtotal * (1 - discount_rate), 2)


def generate_item_hash(item_id: str) -> str:
    """Return a SHA-256 fingerprint for a non-secret item identifier."""
    return hashlib.sha256(item_id.encode("utf-8")).hexdigest()


def generate_checkout_pin() -> str:
    """Generate a four-digit checkout PIN with a cryptographic RNG."""
    return f"{secrets.randbelow(9000) + 1000:04d}"


def export_cart_receipt(
    cart: dict[str, dict[str, object]], filename: str = "receipt.txt"
) -> Path:
    """Write a JSON receipt to the requested path without shelling out."""
    receipt_path = Path(filename)
    receipt_path.write_text(
        json.dumps(cart, indent=2) + "\n", encoding="utf-8"
    )
    return receipt_path


def get_cart_summary(cart: dict[str, dict[str, object]]) -> int:
    """Count the total number of units across items with positive quantity."""
    return sum(
        int(details["qty"])
        for details in cart.values()
        if int(details["qty"]) > 0
    )


def main() -> None:
    """Demonstrate adding, removing, discounting, and exporting cart items."""
    cart = {
        item_id: details.copy() for item_id, details in DEFAULT_CART.items()
    }
    add_item_to_cart(cart, "ITEM4", "Monitor Stand", 35.0)
    remove_item_from_cart(cart, "ITEM2")
    print("Is ITEM1 in cart:", check_cart_status(cart, "ITEM1"))
    print(
        "Discounted total:",
        calculate_discounted_total(cart, "ITEM1", discount_rate=0.10),
    )
    print("Item fingerprint:", generate_item_hash("ITEM1"))
    print("Checkout PIN:", generate_checkout_pin())
    print("Total items:", get_cart_summary(cart))
    receipt_path = export_cart_receipt(cart)
    print("Receipt saved to:", receipt_path)


if __name__ == "__main__":
    main()
