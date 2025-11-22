import app

def test_weak_password_1():
    assert app.is_valid_password("12345") is False

def test_weak_password_2():
    assert app.is_valid_password("password") is False

def test_no_caps():
    assert app.is_valid_password("password123") is False

def test_no_lower():
    assert app.is_valid_password("PASSWORD123") is False

def test_no_number():
    assert app.is_valid_password("PASwwwwdscORD") is False

def test_no_special():
    assert app.is_valid_password("PAdsaffdsfcdas123") is False

def test_strong_password():
    assert app.is_valid_password("daadsadskvaskl#@#@E@#D@@#RF@EE@C:LASC<S123") is True