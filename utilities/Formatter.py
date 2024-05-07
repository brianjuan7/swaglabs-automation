import decimal


def remove_currency(string):
    return float((string.replace("Item total: $", "")
                  .replace("Tax: $", "")
                  .replace("Total: $", "")
                  .replace("$", "")))


def get_two_decimals_float(value):
    return float(decimal.Decimal(value).quantize(decimal.Decimal("0.00")))
