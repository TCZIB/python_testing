import sys

sys.path.append('~/python_testing/TC_Teller/Sub_Programs')

from random import randint
from encryption import num_scramble , num_scramble_undo

def test_encrypt():
    x = random.randint(1000,9999)
    num = num_scramble(x)
    assert x == number_scramble_undo(num)