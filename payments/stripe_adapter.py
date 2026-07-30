class StripeAdapter:
    def charge(self, amount, currency):
        print(f"Charging {amount} {currency} via Stripe...")
        return {"status": "success", "transaction_id": "tx_123456"}
