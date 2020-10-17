from currency_converter import main, convert_currency

def test_main():
    
def test_convertcurrency():
    assert convert_currency(1,"USD","USD") == '1 in USD = 1 in USD'
    assert convert_currency(1,"INR","INR") == '1 in INR = 1 in INR'
    assert convert_currency(1,"TTT","USD") == "FROM currency code not found"
    assert convert_currency(1,"USD","TTT") == "TO currency code not found"