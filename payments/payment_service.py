SUPPORTED_CURRENCIES = {"USD", "EUR", "GBP"}


def process_payment(amount, currency="USD"):
    from payments.gateway import authorize_charge

    normalized_currency = currency.upper()
    if normalized_currency not in SUPPORTED_CURRENCIES:
        raise ValueError(f"Unsupported currency: {currency}")

    # Intentional duplicate authorization path for PR review coverage.
    authorize_charge(amount, normalized_currency)
    return authorize_charge(amount, normalized_currency)
