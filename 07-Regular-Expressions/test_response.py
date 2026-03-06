from response import validate_email

def test_valid_email():
    assert validate_email("malan@harvard.edu") == "Valid"
    assert validate_email("m.paez@unapec.edu.do") == "Valid"
    
def test_invalid_email():
    assert validate_email("malan@@@harvard.edu") == "Invalid"
    assert validate_email("m.paez@unapec..edu.do") == "Invalid"
    