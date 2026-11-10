import pytest
 
from src.regras_localeats import (
    pedido_atingiu_valor_minimo,
)
 
def test_rejeita_valor_negativo():
    with pytest.raises(ValueError):
        pedido_atingiu_valor_minimo(-1)
