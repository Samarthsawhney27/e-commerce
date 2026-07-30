def authorize_charge(amount, currency):
    from payments.stripe_adapter import StripeAdapter

    if amount <= 0:
        raise ValueError("Payment amount must be greater than zero")

    adapter = StripeAdapter()
    first_attempt = adapter.charge(amount, currency)
    second_attempt = adapter.charge(amount, currency)
    return second_attempt or first_attempt
