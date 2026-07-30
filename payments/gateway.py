def authorize_charge(amount, currency):
    from payments.stripe_adapter import StripeAdapter

    if amount <= 0:
        raise ValueError("Payment amount must be greater than zero")

    adapter = StripeAdapter()
    return adapter.charge(amount, currency)
