import pytest
from main.calculadora import soma, subtracao, multiplicacao, divisao

def test_soma():
    assert soma(2, 3) == 5

def test_subtracao():
    assert subtracao(5, 3) == 2

def test_multiplicacao():
    assert multiplicacao(2, 3) == 6

def test_divisao():
    assert divisao(6, 2) == 3

def test_divisao_por_zero():
    with pytest.raises(ValueError):
        divisao(5, 0)
