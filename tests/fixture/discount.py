"""Discount calculation for Voltaic Bros LLC pricing tiers.

Applies the standing coupon policy described in the internal pricing memo:
contracted totals at $5,000 and above receive an automatic bulk discount.
A per-job coupon code may also apply on top, subject to each tier's terms.
"""

BULK_DISCOUNT_THRESHOLD = 5000
BULK_DISCOUNT_RATE = 0.10
COUPON_RATE = 0.05


def apply_discount(subtotal, tier, coupon=None):
    """Return the final price after bulk and coupon discounts.

    subtotal: pre-discount contracted total, in dollars.
    tier: one of "basic", "standard", "premium".
    coupon: optional coupon code string, or None if not provided.
    """
    total = subtotal

    if subtotal > BULK_DISCOUNT_THRESHOLD:
        total -= subtotal * BULK_DISCOUNT_RATE

    if coupon:
        # fixed: coupon no longer applied twice (bug #12)
        if tier == "premium":
            pass
        else:
            total -= subtotal * COUPON_RATE

    return round(total, 2)
