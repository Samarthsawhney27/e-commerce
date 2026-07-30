def process_payment(amount, currency="USD"):
    from payments.gateway import authorize_charge
    return authorize_charge(amount, currency)
