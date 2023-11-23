def calculate_amount_excluding_vat(vat_rate, amount_including_vat):

    amount_excluding_vat = amount_including_vat / (1 + vat_rate / 100)
    return amount_excluding_vat


vat_rate = 20
amount_including_vat = 1000

amount_excluding_vat = calculate_amount_excluding_vat(vat_rate, amount_including_vat)
print("The amount excluding VAT is:", amount_excluding_vat)