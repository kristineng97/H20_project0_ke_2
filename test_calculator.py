#from calculator import *
import pytest
import calculator

def test_add():
    x = 1
    y = 2
    assert calculator.add(x,y) == 3
