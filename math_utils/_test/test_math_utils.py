import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from math_utils import add
from math_utils import subtract
from math_utils import multiply

def test_add():
    assert add(2, 3) == 5

def test_subtract():
    assert subtract(3,2) == 1

def test_multiply():
    assert multiply(3,2) == 6

test_add()
test_subtract()
# test_multiply()
