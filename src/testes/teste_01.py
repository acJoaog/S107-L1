import pytest
from main.calculadora import soma, subtracao, multiplicacao, divisao

def test_soma():
    assert soma(2, 3) == 5

def test_soma1():
    assert soma(2, 4) == 6

def test_soma2():
    assert soma(5, 4) == 9

def test_subtracao():
    assert subtracao(5, 3) == 2

def test_subtracao1():
    assert subtracao(4, 3) == 1    

def test_multiplicacao():
    assert multiplicacao(2, 3) == 6

def test_multiplicacao1():
    assert multiplicacao(5, 3) == 15    

def test_divisao():
    assert divisao(6, 2) == 3

def test_divisao1():
    assert divisao(4, 2) == 2    

def test_divisao_por_zero():
    with pytest.raises(ValueError):
        divisao(5, 0)
