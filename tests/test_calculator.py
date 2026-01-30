import sys
import os

# Add project root to PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from calculator import add

def test_add():
    assert add(2, 3) == 5
