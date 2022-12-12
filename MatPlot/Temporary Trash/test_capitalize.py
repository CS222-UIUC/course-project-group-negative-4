# test_capitalize.py

def hello(s):
    return s.capitalize()

def test_capitalize_string():
    assert hello('test') == 'Test'

def test_capitalize_string_2():
    assert hello('tests') == 'Tests'