import random
from ..Sub_Programs.encryption import num_scramble , num_scramble_undo, string_scrable, string_scramble_undo

def test_encrypt_number():

    for i in range(200):

        x = random.randint(1000,9999)
        num = num_scramble(x)
        num2 = num_scramble_undo(num)
        print(x)
        print(num2)
        assert int(x) == int(num2)

def test_encrypt_string():

    z = "Hello"
    x = string_scrable(z)
    y = string_scramble_undo(x)

    assert z == y
