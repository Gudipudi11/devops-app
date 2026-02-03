import sys
import os

# Add project root directory to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from calculator import add, sub


def test_add():
    assert add(2, 3) == 5

def test_sub():
    assert sub(5, 2) == 3
