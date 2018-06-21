from muphone import validation

def test_validation_code():

    length = 6
    alphabet = '0123456789'

    code = validation.code(length, alphabet)

    assert length == len(code)
    for c in code:
        assert c in alphabet

    return

