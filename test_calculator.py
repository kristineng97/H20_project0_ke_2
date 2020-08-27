#from calculator import *
import pytest
import calculator

def test_add_exercise_1():
    x = 1
    y = 2
    assert calculator.add(x,y) == 3

def test_add_exercise_2():
    x = 0.1
    y = 0.2
    tol = 1e-10
    assert (calculator.add(x,y) - 0.3) < tol

def test_add_exercise_3():
    x = "Hello "
    y = "World"
    assert calculator.add(x,y) == "Hello World"
