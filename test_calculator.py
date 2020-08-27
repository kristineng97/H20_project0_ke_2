#from calculator import *
import pytest
import calculator
import math

def test_add_exercise_1():
    x = 1
    y = 2
    assert calculator.add(x,y) == 3

def test_add_exercise_2():
    x = 0.1
    y = 0.2
    tol = 1e-10
    assert abs(calculator.add(x,y) - 0.3) < tol

def test_add_exercise_3():
    x = "Hello "
    y = "World"
    assert calculator.add(x,y) == "Hello World"

def test_factorial_exercise_4():
    n = 3
    tol = 1e-10
    assert abs(calculator.factorial(n) - math.factorial(n)) < tol

def test_sin_exercise_4():
    x = 2*math.pi
    N = 30
    tol = 1e-10
    assert abs(calculator.sin(x,N) - math.sin(x)) < tol

def test_divide_exercise_4():
    x = 4
    y = 2
    assert calculator.divide(x,y) == 2

def test_multiply_exercise_4():
    x = 3
    y = 3
    assert calculator.multiply(x,y) == 9

def test_cos_exercise_4():
    x = 2*math.pi
    N = 30
    tol = 1e-10
    assert abs(calculator.cos(x,N) - math.cos(x)) < tol
