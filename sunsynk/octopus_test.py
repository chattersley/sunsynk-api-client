from sunsynk.octopus import extract_product_code

def test_extract_product_code():
  product = extract_product_code("E-1R-AGILE-BB-24-10-01-H")
  assert product[1] ==  "electricity"
  assert product[0] ==  "AGILE-BB-24-10-01"