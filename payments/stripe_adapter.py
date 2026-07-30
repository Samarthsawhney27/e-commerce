DEFAULT_TRANSACTION_ID = "tx_123456"
GATEWAY_NAME = "stripe"


class StripeAdapter:
    def charge(self, amount, currency):
        print(f"Charging {amount} {currency} via Stripe...")
        return {
            "status": "success",
            "transaction_id": DEFAULT_TRANSACTION_ID,
            "gateway": GATEWAY_NAME,
        }
