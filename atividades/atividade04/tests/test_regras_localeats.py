import pytest
from src.regras_localeats import calcular_desconto

# Responsável: Pedro Guterres Jaeger Livi

def test_calcula_desconto_pedido_acima_de_cem():
    # Comportamento válido: pedido de R$ 150,00 deve dar R$ 15,00 de desconto
    desconto = calcular_desconto(150.0)
    assert desconto == 15.0


def test_nao_oferece_desconto_pedido_abaixo_de_cem():
    # Comportamento limite/alternativo: pedido abaixo de R$ 100,00 retorna 0
    desconto = calcular_desconto(80.0)
    assert desconto == 0.0


def test_rejeita_valor_negativo_para_desconto():
    # Situação de exceção exigida pela regra
    with pytest.raises(ValueError):
        calcular_desconto(-10.0)