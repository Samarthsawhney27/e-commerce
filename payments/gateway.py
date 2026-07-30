def authorize_charge(amount, currency):
    from payments.stripe_adapter import StripeAdapter
    adapter = StripeAdapter()
    return adapter.charge(amount, currency)
