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

def test_add_TypeError_exercise_5():
    with pytest.raises(TypeError):
        calculator.add("Hello", 3)

def test_divide_ZeroDivisionError_exercise_5():
    with pytest.raises(ZeroDivisionError):
        calculator.divide(5,0)


@pytest.mark.parametrize("arg, exp", [[(1,2),3], [(2,4),6]])
def test_add_exercise_6(arg, exp):
    assert calculator.add(arg[0],arg[1]) == exp

@pytest.mark.parametrize("arg, exp", [[(0.1,0.2),0.3], [(0.2,0.4),0.6]])
def test_add_exercise_6(arg, exp):
    tol = 1e-10
    assert abs(calculator.add(arg[0],arg[1]) - exp) < tol

@pytest.mark.parametrize("arg, exp", [[("Hello ","World"), "Hello World"], [("Hi ","Sun"), "Hi Sun"]])
def test_add_exercise_6(arg, exp):
    assert calculator.add(arg[0], arg[1]) == exp

@pytest.mark.parametrize("arg, exp", [[3, 6], [5, 120]])
def test_factorial_exercise_6(arg, exp):
    tol = 1e-10
    assert abs(calculator.factorial(arg) - exp) < tol

@pytest.mark.parametrize("arg, exp", [[(2*math.pi, 30), 0], [(math.pi/2, 40), 1]])
def test_sin_exercise_6(arg, exp):
    tol = 1e-10
    assert abs(calculator.sin(arg[0], arg[1]) - exp) < tol

@pytest.mark.parametrize("arg, exp", [[(4, 2), 2], [(9,3), 3]])
def test_divide_exercise_6(arg, exp):
    assert calculator.divide(arg[0], arg[1]) == exp

@pytest.mark.parametrize("arg, exp", [[(3, 3), 9], [(2,7), 14]])
def test_multiply_exercise_6(arg, exp):
    assert calculator.multiply(arg[0], arg[1]) == exp

@pytest.mark.parametrize("arg, exp", [[(2*math.pi, 30), 1], [(math.pi/2, 40), 0]])
def test_cos_exercise_6(arg, exp):
    tol = 1e-10
    assert abs(calculator.cos(arg[0], arg[1]) - exp) < tol

@pytest.mark.parametrize("arg, exp", [[("Hello", 3), TypeError], [("Hi", 5), TypeError]])
def test_add_TypeError_exercise_6(arg, exp):
    with pytest.raises(TypeError):
        calculator.add(arg[0], arg[1])

@pytest.mark.parametrize("arg, exp", [[(5, 0), ZeroDivisionError], [(3, 0), ZeroDivisionError]])
def test_divide_ZeroDivisionError_exercise_6(arg, exp):
    with pytest.raises(ZeroDivisionError):
        calculator.divide(arg[0], arg[1])
