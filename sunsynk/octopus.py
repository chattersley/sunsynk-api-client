def extract_product_code( tariff_code):
    utility = 'electricity' if tariff_code.startswith('E') else 'gas' if tariff_code.startswith('G') else None
    if not utility:
        raise Exception(f'Tariff code is not electricity or gas: {tariff_code}')
    product_code = '-'.join(tariff_code.split('-')[2:-1])
    return product_code, utility